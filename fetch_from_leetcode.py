import logging
import os
import re
import subprocess
from typing import Any, TypedDict

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import bs4
import requests

MAX_LINE_LENGTH = 80


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


def leetcode_graphql_request(
    query: str, variables: dict[str, Any] | None = None
) -> dict[str, Any]:
    # LeetCode GraphQL API endpoint
    api_url = "https://leetcode.com/graphql"

    # Define the headers with required information
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/",
    }

    # Define the GraphQL query as a dictionary
    graphql_query: dict[str, Any] = {"query": query}
    if variables:
        graphql_query["variables"] = variables

    # Make the GraphQL request
    response = requests.post(api_url, headers=headers, json=graphql_query)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()

    raise Exception(
        f"Error: Failed to make GraphQL request. Status Code: {response.status_code}. Response: {response.json()}"
    )


def get_daily_question_slug():
    daily_q_query = """
    {
        activeDailyCodingChallengeQuestion {
            date
            link
            question {
                titleSlug
            }
        }
    }
    """
    result = leetcode_graphql_request(daily_q_query)
    daily_q_title_slug = result["data"]["activeDailyCodingChallengeQuestion"][
        "question"
    ]["titleSlug"]
    return daily_q_title_slug


def get_daily_question_description_html(daily_q_title_slug: str):
    question_query = """query questionContent($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content
            mysqlSchemas
            dataSchemas
        }
    }
    """
    question_variables = {
        "titleSlug": daily_q_title_slug,
    }
    result = leetcode_graphql_request(question_query, question_variables)
    problem_description_html = result["data"]["question"]["content"]
    return problem_description_html


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
    return res


def parse_description_html(description_html: str) -> str:
    description_html = f"<div>{description_html}</div>"
    soup = bs4.BeautifulSoup(description_html, "html.parser")

    description_div = soup.find("div")
    assert isinstance(description_div, bs4.Tag)

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
        if len(line) <= MAX_LINE_LENGTH:
            line_limited_description_list.append(line)
            continue

        list_depth = 0
        if line.startswith("- "):
            list_depth = 2
        if line.startswith("  - "):
            list_depth = 4

        breaks = 0
        curr_indent_size = 0
        while len(line) + indent_size > MAX_LINE_LENGTH:
            curr_indent_size = list_depth * (breaks > 0)
            split_idx = line.rfind(" ", 0, MAX_LINE_LENGTH - curr_indent_size)
            line_limited_description_list.append(
                " " * curr_indent_size + line[:split_idx]
            )
            line = line[split_idx + 1 :]
            breaks += 1

        line_limited_description_list.append(" " * curr_indent_size + line)

    return "\n".join(line_limited_description_list)


def get_daily_question_description(daily_q_title_slug: str):
    description_html = get_daily_question_description_html(daily_q_title_slug)
    description_str = parse_description_html(description_html)
    return description_str


class QuestionInfo(TypedDict):
    questionId: int
    questionFrontendId: int
    title: str
    titleSlug: str
    difficulty: str


def get_question_info(daily_q_title_slug: str) -> QuestionInfo:
    question_query = """query questionTitle($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            difficulty
        }
    }
    """
    gql_variables = {
        "titleSlug": daily_q_title_slug,
    }
    result = leetcode_graphql_request(question_query, gql_variables)
    return QuestionInfo(result["data"]["question"])


def get_default_code_unclean(title_slug: str):
    code_gql_query = """query questionEditorData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            codeSnippets {
                langSlug
                code
            }
        }
    }
    """
    code_gql_variables = {
        "titleSlug": title_slug,
    }
    result = leetcode_graphql_request(code_gql_query, code_gql_variables)
    all_code_snippets: list[Any] = result["data"]["question"]["codeSnippets"]
    for code_snippet in all_code_snippets:
        if code_snippet["langSlug"] == "python3":
            return code_snippet["code"]
    raise Exception("python3 not found in languages")


def clean_code(unclean_code: str) -> str:
    replacements = (("List", "list"),)
    for str_to_replace, replacement in replacements:
        unclean_code = unclean_code.replace(str_to_replace, replacement)
    return unclean_code


def get_default_code(title_slug: str) -> str:
    unclean_code = get_default_code_unclean(title_slug)
    return clean_code(unclean_code)


def get_question_path(question_info: QuestionInfo) -> str:
    q_number = question_info["questionFrontendId"]
    difficulty = question_info["difficulty"]
    title = question_info["title"]
    file_path = os.path.realpath(
        os.path.join(os.path.dirname(__file__), difficulty, f"{q_number}. {title}.py")
    )
    return file_path


def create_question_file(
    q_description: str, default_code: str, question_info: QuestionInfo
):
    file_path = get_question_path(question_info)
    if os.path.isfile(file_path):
        logger.info("File already exists")
        return

    with open(file_path, "w") as f:
        f.write('"""\n')
        f.write(q_description)
        f.write('\n"""\n')
        f.write(default_code)
        f.write("...")


def open_question_file(question_info: QuestionInfo):
    file_path = get_question_path(question_info)
    subprocess.run(["code", file_path], shell=True)


def main():
    daily_q_slug = get_daily_question_slug()

    default_code = get_default_code(daily_q_slug)

    q_description = get_daily_question_description(daily_q_slug)

    question_info = get_question_info(daily_q_slug)

    create_question_file(q_description, default_code, question_info)

    open_question_file(question_info)


if __name__ == "__main__":
    main()
