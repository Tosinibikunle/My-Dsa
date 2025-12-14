def swapPairs(self, head):

    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp

    return head
