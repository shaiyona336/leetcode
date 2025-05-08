class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        elif head.next == None:
            return head
        #fix with recursion the future nodes
        head.next.next = self.swapPairs(head.next.next)
        #after recursion fix current nodes
        temp = head.next
        head.next = temp.next
        temp.next = head

        return temp
