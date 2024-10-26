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

from typing import Any


class OriginalSolution:
    def removeSubfolders(self, folders: list[str]) -> list[str]:
        """
        L := longest path in folders
        x := total characters in folders
        d := total directories
        O(x) / O(d)     time / space complexity
        """
        file_system = self.build_filesystem(folders)
        self.delete_subdirs(file_system)
        self.remaining_dirs: list[str] = []
        self.reconstruct_dirs([], file_system)
        return self.remaining_dirs

    def build_filesystem(self, folders: list[str]):
        """
        O(x) / O(d)     time / space complexity
        """
        file_system: dict[str, Any] = {}
        # build file system
        for folder in folders:
            curr_dir = file_system
            for dir_name in folder.split("/"):
                if dir_name not in curr_dir:
                    curr_dir[dir_name] = {}
                curr_dir = curr_dir[dir_name]
            curr_dir["$"] = True
        return file_system

    def delete_subdirs(self, curr_dir: dict[str, Any]):
        """
        O(d) / O(1)     time / space complexity
        """
        if "$" in curr_dir:
            curr_dir.clear()
            return
        for sub_dir in curr_dir.values():
            self.delete_subdirs(sub_dir)

    def reconstruct_dirs(self, curr_path: list[str], curr_dir: dict[str, Any]):
        """
        O(x) / O(L)     time / space complexity
        """
        if not curr_dir:
            self.remaining_dirs.append("/".join(curr_path))
            return

        for dir_name, subdir_obj in curr_dir.items():
            curr_path.append(dir_name)
            self.reconstruct_dirs(curr_path, subdir_obj)
            curr_path.pop()


class SolutionFromSomeoneElse:
    def removeSubfolders_simple(self, folder: list[str]) -> list[str]:
        """
        Sort paths, sub directories will follow parent directories. Slower by a factor of log(n).
        l := average length of paths in folder, n := len(folder)
        O(l * n * log(n))
        """
        folder.sort()
        res: list[str] = []
        prev = "$"
        for path in folder:
            if not path.startswith(prev + "/"):
                # new non-subdirectory
                res.append(path)
                prev = path
        return res


class Solution(OriginalSolution):
    pass
