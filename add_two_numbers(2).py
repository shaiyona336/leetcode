def addTwoNumbers(l1,l2):
        sum = self.addTwoNumbersHelper(l1,l2,0,1)
        return self.turnSumToList(sum)

    def addTwoNumbersHelper(l1,l2,sum,mul):
        if l1 == None and l2 == None:
            return sum
        if l1 != None:
            sum += l1.val * mul
        if l2 != None:
            sum += l2.val * mul
        
        return self.addTwoNumbersHelper(l1.next if l1 else l1,l2.next if l2 else l2,sum,mul*10)

    def turnSumToList(sum) -> ListNode:
        dummy = ListNode()
        currNode = dummy

        while sum != 0:
            newNode = ListNode(sum % 10)
            currNode.next = newNode
            currNode = currNode.next
            sum //= 10
        
        return dummy.next if dummy.next != None else ListNode(0)
