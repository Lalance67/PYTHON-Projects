# Write a function that takes the head of a linked list and a target value.
# Remove the first node whose value matches the target. Return the head.

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
def terminate(head, target):
    curr = head
    prev = None
    while curr:
        if curr.val == target:
            if prev:
                prev.next = curr.next
                return head
            else: 
                head = curr.next
                return head
        prev = curr
        curr = curr.next
        return head
head = node(1, node(2, node(3, node(4, node(5)))))
# head = None
head = terminate(head, 0)

curr = head
if curr:
    while curr:
        print(curr.val)
        curr = curr.next
else: print("linkedlist empty")

        