def deleteDuplicates(head):
    if head == None:
        return
    alreadySeen = set()
    alreadySeen.add(head.val)
    currNode = head
    nextNode = currNode.next

    while nextNode != None:
        if nextNode.val in alreadySeen:
            temp = nextNode
            currNode.next = nextNode.next
            nextNode = nextNode.next
            del temp
        else:
            alreadySeen.add(nextNode.val)
            currNode = currNode.next
            nextNode = nextNode.next

    return head


