class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # convert to list to make "deleting" characters more efficient
        char_arr = list(s)
        # store idxs of not yet closed opening brackets
        opening_br_idxs = []
        for i, c in enumerate(char_arr):
            # add idx of '(' to stack
            if c == '(':
                opening_br_idxs.append(i)
            elif c == ')':
                # if there is an open bracket to be closed, pop it off the stack
                if opening_br_idxs:
                    opening_br_idxs.pop()
                else:
                    # otherwise "delete" the closing bracket
                    char_arr[i] = ""

        # any brackets that were not closed also need to be deleted
        for i in opening_br_idxs:
            char_arr[i] = ""

        # join char array back into one string
        return "".join(char_arr)
