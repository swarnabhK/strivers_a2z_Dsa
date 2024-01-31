#insert node at beginning of the linked list, given the head
from Node import Node
    
def insert_beginning(head,val):
    #insert a new node at the beg
    node = Node(val)
    node.next = head
    head = node
    return head

def print_ll(head):
    q = head
    while(q):
        print(q.value,end=" ")
        q = q.next
    print()

head = Node(10)
Node1 = Node(20)
Node2 = Node(30)

head.next = Node1
Node1.next = Node2

print("Before inserting the new node")
print_ll(head)
head = insert_beginning(head,0)
print("After inserting the new node")
print_ll(head)

head = insert_beginning(head,40)
head = insert_beginning(head,50)
head = insert_beginning(head,60)
head = insert_beginning(head,70)
print_ll(head)