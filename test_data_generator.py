import random

import pyperclip

rint = random.randint


def int_couple_list(lines, min_val, max_val, size):
    l = []
    for _ in range(size):
        l.append([random.randint(min_val, max_val), random.randint(min_val, max_val)])

    lines.append(str(l))


def int_list(lines, min_val, max_val, size):
    l = []
    for _ in range(size):
        l.append(random.randint(min_val, max_val))

    lines.append(str(l))


def almost_non_decreasing_int_list(lines, size):
    l = list(range(size))

    for _ in range(random.randint(0, 3)):
        l[random.randint(0, size-1)] = random.randint(0, size)

    lines.append(str(l))


def two_rects(lines):
    for _ in range(2):
        lines.append(str(rint(-10, 0)))
        lines.append(str(rint(-10, 0)))
        lines.append(str(rint(0, 10)))
        lines.append(str(rint(0, 10)))

def digits_str(lines, size):
    lines.append('"' + ''.join(str(rint(0, 9)) for _ in range(size)) + '"')

def similar_words_list(lines, line_count, word_count, max_word_len):
    for _ in range(line_count):
        l = []
        for _ in range(word_count):
            l.append(''.join(chr(rint(ord('a'), ord('e'))) for _ in range(rint(0,max_word_len))))
        lines.append(str(l))

if __name__ == "__main__":
    lines = []

    LINE_COUNT = 2
    SIZE = 4
    for _ in range(LINE_COUNT):
        similar_words_list(lines, LINE_COUNT, SIZE, 5)

    s = '\n'.join(lines).replace(" ", "").replace("'", '"')
    print(s)
    pyperclip.copy(s)
    print("^ copied to clipboard")
