class ListNode(object):
    def __init__(self):
        pass
#   Please ignore this ListNode class, its not part of the main code!!


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        rh = r = ListNode(0)
        c = 0
        while l1 or l2 or c:
            x = y = 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            r.next = ListNode((x+y+c)%10)
            c = (x+y+c) // 10
            r = r.next
        return rh.next