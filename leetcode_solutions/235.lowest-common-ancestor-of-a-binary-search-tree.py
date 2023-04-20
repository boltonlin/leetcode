# 230420

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ts = [root]

        while ts:
            tn = ts.pop()
            if tn.val == p.val: return p
            elif tn.val == q.val: return q
            if tn.val < p.val and tn.val < q.val: ts.append(tn.right)
            elif tn.val > p.val and tn.val > q.val: ts.append(tn.left)
            else: return tn
