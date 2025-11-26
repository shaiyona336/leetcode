
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return
        dummy = ListNode(0)
        dummy.next = head
        lastLessIndex = dummy
        currNode = dummy
        
        while currNode and currNode.next:
            if currNode.next.val < x:
                if currNode.next == lastLessIndex.next:
                    lastLessIndex = lastLessIndex.next
                    currNode = currNode.next
                else:
                    temp = currNode.next
                    currNode.next = temp.next
                    temp.next = lastLessIndex.next
                    lastLessIndex.next = temp
                    lastLessIndex = lastLessIndex.next
            else:
                currNode = currNode.next

        return dummy.next
