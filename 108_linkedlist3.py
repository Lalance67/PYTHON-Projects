# Write a function that takes the head of 
# a linked list and a value, creates a new 
# node with that value, and attaches it to the 
# end of the list. Return the head.

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def app(head, add):
    curr = head
    new = node(add)
    while curr:
        if curr.next:
            curr = curr.next
        else:
            curr.next = new
            break

head = node(1, node(2, node(3, node(4, node(5)))))

add = int(input("enter num: "))
app(head, add)
curr = head
while curr:
    print(curr.val)
    curr = curr.next

