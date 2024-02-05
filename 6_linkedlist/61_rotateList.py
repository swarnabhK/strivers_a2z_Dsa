def list_length(self, head):
    n = 0
    while head:
        head = head.next
        n += 1
    return n
def rotateRight(self, head, k: int):
    if not head or k == 0:
        return head
    slow, fast = head, head
    length = self.list_length(head)
    k = k % length
    #if k == length, no rotation needs to be done, return the head.
    if k==0:
        return head
    for _ in range(k):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    fast.next = head
    return temp
