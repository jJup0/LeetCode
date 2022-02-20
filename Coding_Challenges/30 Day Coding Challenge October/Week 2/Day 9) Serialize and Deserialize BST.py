# Definition for a binary tree node.
import queue
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        retStr = ""
        nodeQueue = queue.Queue()
        nodeQueue.put_nowait(root)
        while not nodeQueue.empty():
            curNode = nodeQueue.get()
            if not curNode:
                retStr += "None,"
            else:
                retStr += f"{curNode.val},"
                nodeQueue.put(curNode.left)
                nodeQueue.put(curNode.right)
        retStr = retStr.rstrip("None,")
        return retStr

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        vals = deque(data.split(','))
        root = TreeNode(vals.popleft())
        curNodes = deque((root,))
        while vals:
            curNode = curNodes.popleft()
            l = vals.popleft() if vals else "None"
            r = vals.popleft() if vals else "None"
            if l != "None":
                curNode.left = TreeNode(int(l))
                curNodes.append(curNode.left)
            if r != "None":
                curNode.right = TreeNode(int(r))
                curNodes.append(curNode.right)
        return root
