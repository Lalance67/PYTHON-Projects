# Write a function that takes the head of a linked list and a target value. 
# Return True if the value exists in the list, False if it doesn't.

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def search(head, target):
    curr = head
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False
head = node(1, node(2, node(3, node(4, node(5)))))
tar = int(input("enter target number: "))
s = search(head, tar)
if s:
    print("target is in the linkedlist")
else: print("target is not in the linkedlist")