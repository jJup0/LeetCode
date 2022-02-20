class Solution: 
    def rob(self, root):
        def helper(root):
            if not root:
                return 0, 0 
            
            l_prev, l_rob = helper(root.left)
            r_prev, r_rob = helper(root.right)
            
            prev = max(l_prev+r_prev, l_rob+r_rob, l_prev+r_rob, l_rob+r_prev)
            rob = l_prev + r_prev + root.val
            return prev, rob
        return max(helper(root))