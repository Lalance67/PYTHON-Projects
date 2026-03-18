# Write a function that takes the head of a linked 
# list and reverses it in place. Return the new head.

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def rev(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

head = node(1, node(2, node(3, node(4, node(5)))))
head = rev(head)

curr = head
while curr:
    print(curr.val)
    curr = curr.next