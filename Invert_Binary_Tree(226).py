class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        print("root:", root.val if root else None)
        if root == None:
            return None
        elif root.left == None:
            return root
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        temp = root.left.val
        root.left.val = root.right.val
        root.right.val = temp
        
        return root


solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
inverted_tree = solution.invertTree(root)
print(inverted_tree)  # Output: 4