class Solution:
    class ListNode():
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1, l2):
        
        dummy = self.ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = self.ListNode(num)
            dummy = dummy.next
        
        return res.next