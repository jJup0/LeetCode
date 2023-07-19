import asyncio
import logging
import os
import re
import subprocess

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# import requests
# import time
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

MAX_LINE_LENGTH = 90
TEMP_HTML_FILE_NAME = "temp_leetcode_page.html"
TEMP_FULL_HTML_FILE_NAME = "temp_leetcode_full_page.html"
ZERO_WIDTH_SPACE = "\u200b"


def replace_multiple_whitespace_single_space_strip(string: str):
    return replace_multiple_whitespace_single_space(string).strip()


def replace_multiple_whitespace_single_space(string: str):
    return re.sub(r"\s+", " ", string)


def replace_multiple_whitespace_single_space_except_newline(string: str):
    return re.sub(r"\s+", " ", string)


SPECIAL_NEWLINE_CHAR_PLACEHOLDER = (
    "\u0011"  # device control 1 should not be present in html
)
SPECIAL_UNREMOVEABLE_SPACE_PLACEHOLDER = (
    "\u0012"  # device control 2 should not be present in html
)


def replace_multiple_whitespace_single_space_replace_special_newling(string: str):
    return (
        re.sub(r"([^\S\n])+", " ", string)
        .replace(SPECIAL_NEWLINE_CHAR_PLACEHOLDER, "\n")
        .replace(SPECIAL_UNREMOVEABLE_SPACE_PLACEHOLDER, " ")
    )


def regular_tag_to_string(tag: bs4.Tag, joiner: str = "", list_depth: int = 0):
    res_str_list: list[str] = []
    for child in tag.contents:
        if isinstance(child, bs4.NavigableString):
            if child.text.strip():
                res_str_list.append(
                    replace_multiple_whitespace_single_space_except_newline(child.text)
                )
        elif isinstance(child, bs4.Tag):
            child_type_str = child.name
            str_to_add = ""
            if child_type_str == "sup":
                if child.text.strip().isnumeric():
                    str_to_add += "^"
            elif child_type_str == "sub":
                str_to_add += "_"
            elif child_type_str == "li":
                str_to_add += (
                    SPECIAL_UNREMOVEABLE_SPACE_PLACEHOLDER * 2 * list_depth + "- "
                )
            elif child_type_str == "ul":
                str_to_add += SPECIAL_NEWLINE_CHAR_PLACEHOLDER + regular_tag_to_string(
                    child, SPECIAL_NEWLINE_CHAR_PLACEHOLDER, list_depth + 1
                )
                res_str_list.append(str_to_add)
                continue

            child_to_str_replaced = (
                replace_multiple_whitespace_single_space_replace_special_newling(
                    regular_tag_to_string(child)
                )
            )
            str_to_add += child_to_str_replaced
            res_str_list.append(str_to_add)
        else:
            print(f"child is other type of page element: {type(child)=}")
    res = joiner.join(res_str_list)
    if tag.name == "ul":
        pass
    # print(res)
    # print("-------------------------")
    return res


def get_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--headless")  # type: ignore # unknown
    options.add_experimental_option("prefs", {"browser.tabs.warnOnClose": False})  # type: ignore # unknown
    # options.add_argument("--window-size=1920,1200")  # type: ignore # unknown

    driver = webdriver.Chrome(options)
    return driver


async def get_default_python_code(
    driver: webdriver.Chrome, url: str
) -> tuple[list[str], str, str]:
    # navigate to url
    logger.info("trying to get page")
    driver.get(url)
    logger.info("got page")
    try:
        wait = WebDriverWait(driver, 5)  # Maximum wait time in seconds
        # button to select language
        button: WebElement = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mr-auto button")))  # type: ignore # unknown
        logger.info("found code language button")

        line_limited_description_list, python_filename = get_description(
            bs4.BeautifulSoup(driver.page_source.encode("utf-8"), "html.parser")
        )
        logger.info("got description")

        button.click()  # type: ignore # unknown
        logger.info("clicked language button")

        # select python as language
        li_option: WebElement = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[contains(@class, "relative") and contains(@class, "flex") and contains(@class, "h-8") and contains(@class, "cursor-pointer") and contains(@class, "select-none")]//div[text()="Python3"]')))  # type: ignore # unknown
        li_option.click()  # type: ignore # unknown
        logger.info("selected language")

        # get lines of default code
        await asyncio.sleep(0.5)
        default_code_lines: WebElement = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".view-lines")))  # type: ignore # unknown
        logger.info("got code lines")
    finally:
        # by this time the full page should be loaded, store as file in case something goes wrong
        with open(TEMP_FULL_HTML_FILE_NAME, "wb") as f:
            f.write(driver.page_source.encode("utf-8"))

    # code is stored with raw "\" + "n" characters, replace by newline
    default_code = str(default_code_lines.text).replace(r"\n", "\n")  # type: ignore # unknown

    return line_limited_description_list, python_filename, default_code  # type: ignore # unknown


def get_daily_challenge_url() -> str:
    ...


def get_description(parsed_content: bs4.BeautifulSoup) -> tuple[list[str], str]:
    # get problem name
    problem_name_tag = parsed_content.find(
        "span",
        {"class": "mr-2 text-label-1 dark:text-dark-label-1 text-lg font-medium"},
    )
    if problem_name_tag is None:
        raise Exception("Could not find problem name tag")
    problem_title = replace_multiple_whitespace_single_space_strip(
        problem_name_tag.text
    )

    # get difficulty
    difficulty_div_classes = ".".join(
        "div inline-block font-medium capitalize".split(" ")
    )
    logger.info(f"{difficulty_div_classes=}")
    difficulty_div = parsed_content.select_one(difficulty_div_classes)
    if difficulty_div is None:
        raise Exception("Could not find difficulty")
    difficulty = difficulty_div.text.strip()
    if difficulty not in ("Easy", "Medium", "Hard"):
        raise Exception(f'Diffulty "{difficulty}" does not exist')

    # construct filename and check if exists
    python_file_path = os.path.join(difficulty, problem_title + ".py")
    if os.path.exists(python_file_path):
        raise Exception(f"{python_file_path} already exists")

    # get problem description
    description_div = parsed_content.find("div", {"class": "_1l1MA"})
    if description_div is None:
        raise Exception("Could not find description")

    if not isinstance(description_div, bs4.Tag):
        raise Exception("Somehow description is not a tag")

    full_description_list: list[str] = []
    add_to_list = True
    for description_child in description_div.contents:
        if isinstance(description_child, bs4.NavigableString):
            if not add_to_list:
                continue
            text = description_child.text.strip()
            if text:
                full_description_list.append(text)
            continue
        elif isinstance(description_child, bs4.Tag):
            tag_type_str = description_child.name
            if tag_type_str == "p":
                # p tags containing no text separate description from examples from constraints.
                # do not include examples in the parsed description
                if description_child.text.strip() == "":
                    add_to_list = not add_to_list
                    continue

                if not add_to_list:
                    continue
                full_description_list.append(regular_tag_to_string(description_child))
                full_description_list.append("")
            elif tag_type_str == "ul":
                if not add_to_list:
                    continue
                if full_description_list and full_description_list[-1] == "":
                    full_description_list.pop()
                to_str = regular_tag_to_string(description_child, "\n").split("\n")
                full_description_list.extend(to_str)
                full_description_list.append("")
            elif tag_type_str == "pre" or tag_type_str == "img":
                pass
            else:
                print(f"parsing tag type <{tag_type_str}> not implemented!")

        else:
            print(
                f"description_child is other type of page element: {type(description_child)=}"
            )
    full_description_list.pop()  # pop "" which should be automatically places after constraints <ul>

    line_limited_description_list: list[str] = []
    indent_size = 4
    for line in full_description_list:
        if len(line) + indent_size <= MAX_LINE_LENGTH:
            line_limited_description_list.append("    " + line)
            continue

        list_depth = 0
        if line.startswith("- "):
            list_depth = 2
        if line.startswith("  - "):
            list_depth = 4

        breaks = 0
        curr_indent_size = indent_size
        while len(line) + indent_size > MAX_LINE_LENGTH:
            curr_indent_size = indent_size + list_depth * (breaks > 0)
            split_idx = line.rfind(" ", 0, MAX_LINE_LENGTH - curr_indent_size)
            line_limited_description_list.append(
                " " * curr_indent_size + line[:split_idx]
            )
            line = line[split_idx + 1 :]
            breaks += 1

        line_limited_description_list.append(" " * curr_indent_size + line)

    return line_limited_description_list, python_file_path


async def main(driver: webdriver.Chrome, url: str):
    online = True
    if online:
        # Create an event loop
        async_io_loop = asyncio.get_event_loop()
        # Call the async function and obtain a coroutine object
        coroutine = get_default_python_code(driver, url)
        # Schedule the coroutine to run asynchronously
        get_default_code_task = async_io_loop.create_task(coroutine)

    #     # avoid rate limit
    #     time.sleep(1)
    #     response = requests.get(url)
    #     with open(TEMP_HTML_FILE_NAME, "wb") as f:
    #         f.write(response.content)

    # with open(TEMP_HTML_FILE_NAME, "rb") as f:
    #     parsed_content = bs4.BeautifulSoup(f.read(), "html.parser")

    # line_limited_description_list, python_filename = get_description(parsed_content)

    if online:
        print("waiting on task")
        line_limited_description_list, python_filename, default_code_unformatted = await get_default_code_task  # type: ignore # may be unbound (not true)
        assert isinstance(line_limited_description_list, list)
        assert isinstance(python_filename, str)
        default_code_lines: list[str] = [l.strip() for l in default_code_unformatted.split("\n")]  # type: ignore # may be unbound (not true)
        class_solution_idx = -1
        for i, line in enumerate(default_code_lines):
            if line.startswith("class"):
                class_solution_idx = i
                break
        assert (
            class_solution_idx != -1
        ), f'Could not find "class" in {default_code_lines}'

        # split off and storethe rest of the code
        code_remainder = default_code_lines[class_solution_idx + 1 :]
        # limit code to `class Solution` so docstring can be appended in the right place
        default_code_lines = default_code_lines[: class_solution_idx + 1]

        # add docstring to code
        default_code_lines.append('    """')
        for line in line_limited_description_list:
            default_code_lines.append(line)
        default_code_lines.append('    """')

        # empty new line between doctring and function
        default_code_lines.append("")

        # function signature, for some reason code_remainder sometimes split across
        # several lines, probably something to do with the way the page is rendered
        default_code_lines.append(
            "    " + "".join(code_remainder).replace("List", "list")
        )
        # empty new line at the end of file
        default_code_lines.append("")

        with open(python_filename, "w") as f:
            f.writelines("\n".join(default_code_lines).replace(ZERO_WIDTH_SPACE, ""))

        try:
            # open file
            subprocess.run(["code", f'"{python_filename}"'])
        except Exception as err:
            logging.error(err)
            print(f"Could not open {python_filename} with vscode")


if __name__ == "__main__":
    get_by_stdio = True
    if get_by_stdio:
        url = input("Enter URL:\n")
        # url = "https://leetcode.com/problems/total-cost-to-hire-k-workers/"
    else:
        url = get_daily_challenge_url()

    driver = get_driver()
    asyncio.run(main(driver, url))

    # x = requests.get("https://leetcode.com/problemset/all/")
    # with open("x.html", "wb") as f:
    #     f.write(x.content)
