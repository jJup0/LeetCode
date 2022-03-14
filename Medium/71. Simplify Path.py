class Solution:
    def simplifyPath(self, path: str) -> str:
        path_str_size = len(path)
        i = 0
        # stack of current directory traversal
        curr_directory_stack = []
        while i < path_str_size:

            # find next directory
            while i < path_str_size:
                if path[i] == '/':
                    i += 1
                else:
                    break
            else:
                break

            # directory name goes until next '/'
            new_i = path.find("/", i)
            if new_i == -1:
                new_i = path_str_size

            directory = path[i:new_i]
            if directory == ".":
                # . does nothing
                pass
            elif directory == "..":
                # check if not currently in root folder, else remove one directory from stack
                if curr_directory_stack:
                    curr_directory_stack.pop()
            else:
                curr_directory_stack.append(directory)

            i = new_i + 1

        return "/" + '/'.join(curr_directory_stack)
