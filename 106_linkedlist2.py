# Write a function that takes the head of a 
# linked list and returns the number of nodes in it.

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def s(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

head = node(1, node(2, node(3, node(4, node(5)))))
print(s(head))




    