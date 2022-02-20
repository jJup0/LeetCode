
from collections import defaultdict


class strSolution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root, depth, path):
            if root:
                paths[depth].append(path)
                depth += 1
                dfs(root.left, depth, path+'l')
                dfs(root.right, depth, path+'r')
        paths = defaultdict(list)
        dfs(root, 0, "")
        selection = paths[max(paths.keys())]
        ref = selection.pop()
        breakflag = False
        if selection:
            for i, c in enumerate(ref):
                for word in selection:
                    if word[i] != c:
                        breakflag = True
                if breakflag:
                    break
        else:
            i = len(ref)
        for p in ref[:i]:
            if p == "l":
                root = root.left
            else:
                root = root.right
        return root
