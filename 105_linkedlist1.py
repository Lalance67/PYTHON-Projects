#singly linked list

# one node
class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

#declaring node per variable
a = listNode(1)
b = listNode(2)
c = listNode(4)

#connecting variable
a.next = b
b.next = c

head = a #setting a head or the first element of the linked list

#or 

#no variables needed
#head = listNode(3, listNode(2, listNode(3)))

# traversing
curr = head #set the current to start

while curr: #while curr is not null/none
    print(curr.val) #print the val
    curr = curr.next #move the curr to next

#insert and delete

print()

#insert
new = listNode(3)
new.next = b.next
b.next = new

#append
new = listNode(5)
c.next = new


curr = head
while curr:
    print(curr.val) 
    curr = curr.next

print()


#delete node (c, val = 4) without tracking the variable

curr = head
while curr:
    if curr.val == 3:
        curr.next = new
    curr = curr.next

curr = head
while curr:
    print(curr.val)
    curr = curr.next



