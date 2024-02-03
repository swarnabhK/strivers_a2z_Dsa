def detectCycle(head):
    pos,slow,fast = 0,head,head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        #we first need to check if there is a loop in the linked list
        if slow==fast:
            #if loop is found, move the slow to head, move both slow and fast forward, the point where they meet is the start of the loop in the LL.
            slow = head
            while(slow!=fast):
                slow = slow.next
                fast = fast.next
            return slow
    return None