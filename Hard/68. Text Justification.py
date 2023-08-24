class Solution:
    """
    Given an array of strings words and a width maxWidth, format the text such
    that each line has exactly maxWidth characters and is fully (left and right)
    justified.

    You should pack your words in a greedy approach; that is, pack as many words
    as you can in each line. Pad extra spaces ' ' when necessary so that each line
    has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the
    number of spaces on a line does not divide evenly between words, the empty
    slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, and no extra space
    is inserted between words.

    Note:
    - A word is defined as a character sequence consisting of non-space characters only.
    - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    - The input array words contains at least one word.

    Constraints:
    - 1 <= words.length <= 300
    - 1 <= words[i].length <= 20
    - words[i] consists of only English letters and symbols.
    - 1 <= maxWidth <= 100
    - words[i].length <= maxWidth
    """

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # greedily place words into lines
        lines: list[list[str]] = [[]]
        curr_line_width = 0
        # when inserting a word, always make sure there is enough space for a
        # space character. Using this strategy, we must increment maxWidth, in
        # order to correctly check whether a line is full yet
        max_w_plus_1 = maxWidth + 1
        for word in words:
            # include space with word length
            wlen = len(word) + 1
            curr_line_width += wlen
            if curr_line_width > max_w_plus_1:
                # if the line is full, start a new line
                lines.append([])
                curr_line_width = wlen
            lines[-1].append(word)

        # format lines
        res: list[str] = []
        # only iterate up to second last line, last line has different formatting
        for line_idx in range(len(lines) - 1):
            line = lines[line_idx]
            word_count = len(line)
            char_count = sum(len(w) for w in line)
            spaces_to_distribute = maxWidth - char_count
            if word_count > 1:
                # space_count := minimum/standard amount of spaces between each word
                # the first `extra_spaces` words should have one extra space
                space_count, extra_spaces = divmod(spaces_to_distribute, word_count - 1)
            else:
                # if only one word in the line, fully pad it
                space_count = maxWidth - len(line[0])
                # hacky: spaces are always appended after words, even after
                # the last word to avoid an extra if-block, and then the last
                # spacing is popped off. `extra_spaces` = 1 ensures that a
                # single extra space, that should not be there in the
                # first place will be popped off, instead of the actual spacing
                extra_spaces = 1
            standard_spaces = " " * space_count

            # build the resulting line
            res_line_str_builder: list[str] = []
            for word_idx, word in enumerate(line):
                # append the current word and the standard spaces
                res_line_str_builder.append(word)
                res_line_str_builder.append(standard_spaces)
                if word_idx < extra_spaces:
                    # if there are still extra spaces to be distributed, do so
                    res_line_str_builder.append(" ")

            # pop off extra spacing
            res_line_str_builder.pop()
            # build the string
            res.append("".join(res_line_str_builder))

        # last line is left justified, so just join the words, and ljust() the resulting line
        res.append(" ".join(lines[-1]).ljust(maxWidth))
        return res
