# Problem Statement: Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.


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

def search_element(head,target):
    while(head):
        if(head.value==target):
            return True
        head = head.next
    return False

head = insert_beginning(None,50)
head = insert_beginning(head,40)
head = insert_beginning(head,30)
head = insert_beginning(head,20)
head = insert_beginning(head,10)
head = insert_beginning(head,0)
print_ll(head)
print("Is the element present: ",search_element(head,30))
print("Is the element present: ",search_element(head,70))