# 230413

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative DFS
class Solution:
    def maxDepth(self, root) -> int:
        stack = [(root, 1)]
        max_depth = 1

        while stack:
            node, depth = stack.pop()

            if node.left:
                stack.append((node.left, depth+1))

            if node.right:
                stack.append((node.right, depth+1))

            max_depth = max(depth, max_depth)

        return max_depth

# Iterative BFS
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0

        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level
