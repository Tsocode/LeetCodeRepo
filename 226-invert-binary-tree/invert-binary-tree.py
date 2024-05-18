# Psuedo Code:
# check if the root is NULL, If so return it
# store the value of the left child temporarily
# swap the left node with the right child
# swap the right child with the temp left child that was stored before
# return the root value
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        else:
            temp = root.left
            root.left = root.right
            root.right = temp

            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        