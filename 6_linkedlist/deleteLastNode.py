# Problem Statement: Given a linked list, delete the tail of the linked list and print the updated linked list.

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

def delete_tail(head):
    if not head.next:
        return None
    slow,fast = head,head.next
    while(fast.next):
        slow = slow.next
        fast = fast.next
    slow.next = None
    return head

head = insert_beginning(None,50)
head = insert_beginning(head,40)
head = insert_beginning(head,30)
head = insert_beginning(head,20)
head = insert_beginning(head,10)
head = insert_beginning(head,0)
print("Before deleting tail")
print_ll(head)
head = delete_tail(head)
print("After deleting tail")
print_ll(head)