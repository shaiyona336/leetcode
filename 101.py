class Solution:
    def getPreorder(self, root: Optional[TreeNode]) -> List:
        return self.helper(root,root)


    def helper(self, leftTree, rightTree):
        if leftTree == None and rightTree == None:
            return True
        if leftTree == None or rightTree == None:
            return False
        if leftTree.val != rightTree.val:
            return False
        return self.helper(leftTree.left,rightTree.right) and self.helper(leftTree.right,rightTree.left)
