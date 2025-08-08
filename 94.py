class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      if root == None:
        return []
      elif root.left==None:
        return [root.val]+self.inorderTraversal(root.right)
      else:
        leftList = self.inorderTraversal(root.left)
        toReturn = leftList+[root.val]
        toReturn = toReturn + self.inorderTraversal(root.right)

      return toReturn
