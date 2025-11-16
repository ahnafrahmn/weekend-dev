class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Avoid ListNode!! its not part of the solution
# Solutin bigins from class solution below

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        rh = r = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                r.next = l1
                l1 = l1.next
            else:
                r.next = l2
                l2 = l2.next
            r = r.next
        r.next = l1 if l1 else l2 if l2 else None
        return rh.next            