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


def almost_non_dec(lines, size):
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

if __name__ == "__main__":
    lines = []
    line_count = 50
    for _ in range(line_count):
        digits_str(lines, 30)

    s = '\n'.join(lines)
    print(s)
    pyperclip.copy(s)
    print("^ copied to clipboard")
