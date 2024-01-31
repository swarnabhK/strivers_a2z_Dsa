# Problem Statement: Given a doubly linked list of size ‘N’ consisting of positive integers, your task is to reverse it and return the head of the modified doubly linked list.

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

def reverse_DLL(head):
    if not head:
        return None
    tail = head
    while(tail.next):
        tail = tail.next
    q = tail
    #to reverse we just swap the next and back pointers and move backwards in the list
    while(tail):
        next = tail.next
        prev = tail.back
        tail.next = prev
        tail.back = next
        tail = prev
    return q


arr = [12,5,8,7,4,99]
head = convert2dtoDLL(arr)
print("The DLL after before reversing")
print_dll(head)
print("The DLL after after reversing")
head = reverse_DLL(head)
print_dll(head)