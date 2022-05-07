class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # a stack of all previous character streaks, and indexes of neighboring occurances, which may not be contiguous,
        # as deleting the characters fully (shifting the entire string) is only done at the end
        streak_stack = []

        # turn string into character array to make it mutable, to "delete" characters in O(1)
        char_arr = list(s)

        # current streak character, and its position, basically like top of streak_stack
        streak_char = ''
        char_positions = []
        for i, char in enumerate(s):
            if char == streak_char:
                # if character is the same as previous one, add current index to positions list
                char_positions.append(i)
                # if k characters in a row
                if len(char_positions) == k:
                    # delete all characters at neighboring positions
                    for i_ in char_positions:
                        char_arr[i_] = ''
                    # get previous character and streak from stack, guaranteed to at least have the item ['', 0]
                    streak_char, char_positions = streak_stack.pop()

            else:
                # if current character is different to previous one, push current character and neighboring indexes to stack
                streak_stack.append((streak_char, char_positions))
                # update current char, reset char positions
                streak_char = char
                char_positions = [i]

        # join char array, virtually delete all character streaks as they are replaced by ''
        return ''.join(char_arr)
