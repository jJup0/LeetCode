import random

import pyperclip


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

if __name__ == "__main__":
    lines = []
    line_count = 5

    s = ''.join(lines)
    print(s)
    pyperclip.copy(s)
    print("^ copied to clipboard")
