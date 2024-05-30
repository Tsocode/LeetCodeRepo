# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):  # Defines the isBalanced method
        return (self.Height(root) >= 0)  # Checks if the tree is balanced by calling Height method
    
    def Height(self, root):  # Defines the Height method
        if root is None:  return 0  # Returns 0 if the tree is empty
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)  # Calculates heights of left and right subtrees
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1  # Checks if the tree is unbalanced
        return max(leftheight, rightheight) + 1  # Returns the height of the tree if balanced

        