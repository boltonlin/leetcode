# 230419

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        traversal = [root]
        s1 = []
        s2 = []

        while traversal:
            r = traversal.pop()
            if r:
                traversal.append(r.left)
                traversal.append(r.right)
            if r and r.val == subRoot.val:
                s1.append(r)
                s2.append(subRoot)
            while s1 and s2: 
                sub1 = s1.pop()
                sub2 = s2.pop()

                if sub1 and sub2:
                    if sub1.val == sub2.val:
                        s1.append(sub1.left)
                        s1.append(sub1.right)
                        s2.append(sub2.left)
                        s2.append(sub2.right)
                    else:
                        s1, s2 = [], []
                elif not sub1 and not sub2:
                    if len(s1) == len(s2) == 0:
                        return True
                else:
                    s1, s2 = [], []

        return False

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        traversal = [root]

        while traversal:
            r = traversal.pop()
            if r:
                traversal.append(r.left)
                traversal.append(r.right)
            if r and r.val == subRoot.val:
                if self.isSameTree(r, subRoot): return True

        return False
    
    def isSameTree(self, p, q) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
