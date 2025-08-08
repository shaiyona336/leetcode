def get_size(self, head):
  count = 0
  currNode = head
  while currNode != None:
    count += 1
    currNode = currNode.next

  return count
    

  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    size = get_size()
    self.current = head
    self.create_tree(head,0,size-1)

  
  def create_tree(self,left,right):
    if left < right:
      return None

    middle = (left+right) // 2
    leftChild = self.create_tree(left,middle-1)
    centerNode = TreeNode()
    centerNode.left = leftChild
    rightChile = self.create_tree(middle+1,right)

    return centerNode
    