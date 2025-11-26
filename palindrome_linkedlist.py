

class Solution(object):
    def isPalindrome(self, head):
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return l == l[::-1]
        