# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    # Pseudo Code:
    # Using example: Input: root = [3,9,20,null,null,15,7]
                    #output: 3
    # Identify the root node (3)
    # Go to each node, btw left and right
    # Find a way to see the number from each side  (max(function))
    # Return the max number of nodes down the path and return the value
