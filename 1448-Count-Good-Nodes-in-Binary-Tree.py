# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, goodVal):
            if not node:
                return 0

            newVal = max(node.val, goodVal)
            return dfs(node.left, newVal) + dfs(node.right, newVal) + (1 if node.val >= goodVal else 0)
        
        return dfs(root, root.val)

            

        
        