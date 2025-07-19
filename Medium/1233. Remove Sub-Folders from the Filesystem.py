"""
Given a list of folders folder, return the folders after removing all
sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder
of it. A sub-folder of folder[j] must start with folder[j], followed by a"/".
For example,"/a/b" is a sub-folder of"/a", but"/b" is not a sub-folder of"/a/b/c".

The format of a path is one or more concatenated strings of the form:'/'
followed by one or more lowercase English letters.
- For example,"/leetcode" and"/leetcode/problems" are valid paths while an
  empty string and"/" are not.

Constraints:
- 1 <= folder.length <= 4 * 10^4
- 2 <= folder[i].length <= 100
- folder[i] contains only lowercase letters and'/'.
- folder[i] always starts with the character'/'.
- Each folder name is unique.
"""


class Solution:
    def removeSubfolders(self, folders: list[str]) -> list[str]:
        """
        Sort folder and simply check if previous folder is a prefix
        Complexity:
            n := sum(map(len, folders))
            Time: O(n * log(n))
            Space: O(n)
        """
        folders.sort()
        res: list[str] = []
        prev = "$"
        for folder in folders:
            if folder.startswith(prev):
                continue
            res.append(folder)
            prev = folder
        return res
