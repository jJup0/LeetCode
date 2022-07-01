import random

import pyperclip

rint = random.randint


def int_couple_list(min_val, max_val, size):
    for _ in range(line_count):
        l = []
        for _ in range(size):
            l.append([random.randint(min_val, max_val), random.randint(min_val, max_val)])

        lines.append(str(l) + "\n")


def int_list(min_val, max_val, size):
    for _ in range(line_count):
        l = []
        for _ in range(size):
            l.append(random.randint(min_val, max_val))

        lines.append(str(l) + "\n")


def almost_non_dec(size):

    for _ in range(line_count):
        l = list(range(size))

        for _ in range(random.randint(0, 3)):
            l[random.randint(0, size-1)] = random.randint(0, size)

        lines.append(str(l) + "\n")


def two_rects():
    for _ in range(line_count):
        for _ in range(2):
            lines.append(str(rint(-10, 0)) + "\n")
            lines.append(str(rint(-10, 0)) + "\n")
            lines.append(str(rint(0, 10)) + "\n")
            lines.append(str(rint(0, 10)) + "\n")


if __name__ == "__main__":
    lines = []
    line_count = 50
    
    two_rects()

    s = ''.join(lines)
    print(s)
    pyperclip.copy(s)
    print("^ copied to clipboard")
