def deleteMiddle(head):
    prev,slow,fast = None,head,head
    while(fast and fast.next):
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev is None:
        return None
    prev.next = slow.next
    return head