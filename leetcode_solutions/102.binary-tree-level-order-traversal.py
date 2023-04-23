# 230423

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        d = deque([(root, 0)])
        res = []

        while d:
            (n, lvl) = d.popleft()
            if n:
                if len(res) < lvl + 1: res.insert(lvl, [])
                res[lvl].append(n.val)
                d.append((n.left, lvl+1))
                d.append((n.right, lvl+1))

        return res

# BFT with a queue and keep track of the levels.
