# Delete Last Node of a Doubly Linked List
# Problem Statement: Given a Doubly Linked List. Delete the last of a Doubly Linked List.

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

def delete_end(head):
    if not head:
        return "Empty list"
    if not head.next:
        return None
    tail = head
    while(tail.next):
        tail = tail.next
    prev = tail.back #getting the previous node from tail
    prev.next = None #deleted the tail node.
    return head
    

arr = [12,5,8,7,4,99]
head = convert2dtoDLL(arr)
print_dll(head)
print("The DLL after deleting tail node")
head = delete_end(head)
print_dll(head)