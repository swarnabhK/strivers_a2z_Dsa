# Problem Statement: Given a doubly linked list, and a value ‘k’, insert a node having value ‘k’ at the end of the doubly linked list.
from DLLNode import DLLNode

def convert2dtoDLL(arr):
    head = DLLNode(arr[0],None,None)
    prev = head
    for i in range(1,len(arr)):
        temp = DLLNode(arr[i],None,prev)
        prev.next = temp
        prev = temp
    return head

def print_dll(head):
    while(head):
        print(head.val,end=" ")
        head = head.next
    print()

def insert_end(head,k):
    new_node = DLLNode(k)
    if not head:
        return new_node
    tail = head
    while(tail.next):
        tail = tail.next
    tail.next = new_node
    new_node.back = tail
    return head

arr = [12,5,8,7,4]
head = convert2dtoDLL(arr)
print_dll(head)
print("The DLL after inserting node at the tail")
head = insert_end(head,99)
print_dll(head)
