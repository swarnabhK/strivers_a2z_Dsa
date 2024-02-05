def removeNthFromEnd(head, n):
    slow,fast = head,head
    #maintain a distance of n from the slow pointer
    for _ in range(n):
        fast = fast.next
    # case when n is equal to size of the list, we remove the first node
    if not fast:
        return head.next
    while(fast.next):
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head