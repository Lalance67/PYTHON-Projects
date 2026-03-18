# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        prev = None
        curr = head
        nxt = None

        while curr:
            if val == curr.val:
                if prev:
                    prev.next = curr.next
                    nxt = curr.next
                    curr.next = None
                    curr = nxt
                else:
                    nxt = curr.next
                    curr.next = None
                    curr = nxt
                    head = curr
            else:
                prev = curr
                curr = curr.next
        return head
        