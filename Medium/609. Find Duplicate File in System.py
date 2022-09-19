from collections import defaultdict
from typing import List


class Solution:
    """
    Given a list paths of directory info, including the directory path, and all the files with
    contents in this directory, return all the duplicate files in the file system in terms of
    their paths. You may return the answer in any order.
    A group of duplicate files consists of at least two files that have the same content.
    A single directory info string in the input list has the following format:
        "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
    It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content
    ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0.
    If m = 0, it means the directory is just the root directory.
    The output is a list of groups of duplicate file paths. For each group, it contains all the
    file paths of the files that have the same content. A file path is a string that has the
    following format:
        "directory_path/file_name.txt"
    Constraints:
        1 <= paths.length <= 2 * 10^4
        1 <= paths[i].length <= 3000
        1 <= sum(paths[i].length) <= 5 * 105
        paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
        You may assume no files or directories share the same name in the same directory.
        You may assume each given directory info represents a unique directory. A single blank
        space separates the directory path and file info.
    """

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # content to paths dictionary
        c2p = defaultdict(list)
        for path in paths:
            # split path string into directory and list of files
            directory, *files = path.split(" ")
            directory += '/'

            # iterate through files and split into file name and content
            for file in files:
                # split file into name and content, content will have trailing ')', but not important
                file_name, content = file.split('(', maxsplit=1)
                # add full path to list of file with that content
                c2p[content].append(directory + file_name)

        return [_paths for _paths in c2p.values() if len(_paths) > 1]

    followUp = """
    Imagine you are given a real file system, how will you search files? DFS or BFS?
        DFS to save on RAM probably. Not sure but probably also faster harddrive acces for files in
        same directory, not sure if BFS would be better for this case.

    If the file content is very large (GB level), how will you modify your solution?
        Obviously do not store entire file as hashmap key, maybe only first couple hundred/thousand
        bytes + filesize in hashmap, if collision occurs, check for exact match.

    If you can only read the file by 1kb each time, how will you modify your solution?
        See answer 2.

    What is the time complexity of your modified solution? What is the most time-consuming part
    and memory-consuming part of it? How to optimize?
        Time complexity is still total size of duplicate files. Idk what could be optimized lol.

    How to make sure the duplicated files you find are not false positive?
        See answer 2.
    """
