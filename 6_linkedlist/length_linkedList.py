#Problem Statement: Given the head of a linked list, print the length of the linked list.


from Node import Node
def insert_beginning(head,val):
    #insert a new node at the beg
    if not head:
        return Node(val)
    node = Node(val)
    node.next = head
    head = node
    return head

def print_ll(head):
    if not head:
        return "The list is empty"
    q = head
    while(q):
        print(q.value,end=" ")
        q = q.next
    print()

def find_length(head):
    q = head
    length = 0
    while(q):
        length+=1
        q = q.next
    return length

head = insert_beginning(None,50)
head = insert_beginning(head,40)
head = insert_beginning(head,30)
head = insert_beginning(head,20)
head = insert_beginning(head,10)
head = insert_beginning(head,0)
print(f"Length of the linked list is: {find_length(head)}")