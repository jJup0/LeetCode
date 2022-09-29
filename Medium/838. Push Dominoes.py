class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Replace pattern like with kontextfree grammatic.
        O(n * dominoes.count('.')) / O(n)   time / space complexity
        """
        while True:
            # replace R.L with a special letter first to preserve the R.L structure
            # then let dominoes fall onto upright standing dominoes
            new_dominoes = dominoes.replace('R.L', 'S').replace('.L', 'LL').replace('R.', 'RR')
            if new_dominoes == dominoes:
                break
            else:
                dominoes = new_dominoes

        # replace special letter with R.L
        return dominoes.replace('S', 'R.L')

    def pushDominoes_nightmare(self, dominoes: str) -> str:
        """
        Let dominoes fall to the right first, then to the left, and meet in the middle. Nightmare to understand
        O(n) / O(n)     time / space complexity
        """
        n = len(dominoes)
        # create char list copy of dominoes
        d_list = list(dominoes)
        for i, letter in enumerate(dominoes):
            if letter == 'R':
                # let domino fall to the right until L is encounted
                for i in range(i + 1, n):
                    letter2 = dominoes[i]
                    # if . is ecountered mark it with small 'r' to signify that it is pushed to the
                    # right by a domino, but not initially an 'R'
                    if letter2 == '.':
                        d_list[i] = 'r'
                    elif letter2 == 'L':
                        break

        
        i = n-1
        while i >= 0:
            letter = dominoes[i]
            if letter == 'L':
                starting_i = i
                # update i while simulating domino fall, passed dominos to not need to be examined
                # again
                for i in range(i - 1, -1, -1):
                    # let domino fall to the left
                    letter2 = d_list[i]
                    # if still standing straight domino is ecountered it will definitely fall to
                    # the left
                    if letter2 == '.':
                        d_list[i] = 'L'
                    elif letter2 == 'r':
                        # if right knocked domino encountered, find responsible 'R' domino, and 
                        # fill with L's and R's to the middle
                        starting_r = dominoes.rfind('R', 0, i)
                        length = i - starting_r
                        half_len = length >> 1
                        d_list[starting_i-half_len:starting_i] = ['L'] * half_len
                        # if gap between L and R is odd, replace 'r' with a '.'
                        if length % 2:
                            d_list[starting_i-half_len-1] = '.'
                        break
                    else:
                        i += 1
                        break

            i -= 1

        return ''.join(d_list).replace('r', 'R')
