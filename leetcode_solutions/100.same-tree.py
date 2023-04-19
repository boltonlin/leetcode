# 230417

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        ps = [p]
        qs = [q]
        
        while ps and qs:
            pn = ps.pop()
            qn = qs.pop()

            if not pn or not qn:
                if pn != qn: return False
                else: continue

            if pn.val != qn.val: return False

            ps.append(pn.left)
            ps.append(pn.right)
            qs.append(qn.left)
            qs.append(qn.right)

        return True

class Solution:
    def isSameTree(self, p, q) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
