# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

head = node(1, node(2, node(3, node(4, node(5)))))
prev = Solution()
curr = prev.reverseList(head)
while curr:
    print(curr.val)
    curr = curr.next

