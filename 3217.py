
class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while (curr.next != None):
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next

