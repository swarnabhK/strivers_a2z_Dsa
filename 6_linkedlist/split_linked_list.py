#revisit this question
def splitListToParts(head, k):
    n = 0
    temp = head
    # find the length of the list
    while temp:
        temp = temp.next
        n += 1

    # make the divisions
    l_list = n // k
    extra = n % k
    res = []
    i = 0

    while i < k:
        part_size = l_list + 1 if extra > 0 else l_list
        extra -= 1

        # Create a new part
        part_head = head
        part_prev = None
        for _ in range(part_size):
            if head:
                part_prev = head
                head = head.next

        if part_prev:
            part_prev.next = None  # Disconnect the part from the rest of the list

        res.append(part_head)
        i += 1

    return res
