class Solution:
    """
    Given a string path, which is an absolute path (starting with a slash '/') to a
    file or directory in a Unix-style file system, convert it to the simplified
    canonical path.

    In a Unix-style file system, a period '.' refers to the current directory, a
    double period '..' refers to the directory up a level, and any multiple consecutive
    slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other
     format of periods such as '...' are treated as file/directory names.

    The canonical path should have the following format:
        The path starts with a single slash '/'.
        Any two directories are separated by a single slash '/'.
        The path does not end with a trailing '/'.
        The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

    Return the simplified canonical path.

    Constraints:
        1 <= path.length <= 3000
        path consists of English letters, digits, period '.', slash '/' or '_'.
        path is a valid absolute Unix path.
    """

    def simplifyPath(self, path: str) -> str:
        """
        Simple Stack implementation.
        O(n) / O(n)     time / space complexity
        """
        # stack of current directories
        stack = []
        for directory in path.split("/"):
            if directory == "" or directory == ".":
                # starting "/", multiple slashes "///" and single dots "."
                # do not not change the current directory
                continue
            elif directory == "..":
                # double dots refers to parent directory, so pop from stack
                if stack:
                    stack.pop()
            else:
                # other wise normal directory, add to stack
                stack.append(directory)

        return "/" + "/".join(stack)
