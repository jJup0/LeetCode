import random

import pyperclip


def int_couple_list(min_val, max_val, size):
    for _ in range(line_count):
        l = []
        for _ in range(size):
            l.append([random.randint(min_val, max_val), random.randint(min_val, max_val)])

        lines.append(str(l) + "\n")


if __name__ == "__main__":
    lines = []
    line_count = 10

    int_couple_list(1, 999, 100)

    s = ''.join(lines)
    pyperclip.copy(s)
    print(s)
