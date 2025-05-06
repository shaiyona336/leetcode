class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0,head) #help remove the head, because you want a node before of him to change next to head.next
        currNode = lastNode = dummy #i want to get with currNode to node to remove
        for i in range(n+1):
            if lastNode == None:
                return head
            lastNode = lastNode.next
        while lastNode != None:
            currNode = currNode.next
            lastNode = lastNode.next
        if currNode != None and currNode.next != None:
            currNode.next = currNode.next.next

        return dummy.next


