def isPalindrome(head) -> bool:
    # find the middle and then reverse the sublist. Compare the reversed sublist with every element of the first half
    slow,fast = head,head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    prev = None
    while(slow):
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    first_list,second_list = head,prev
    #doing second_list because eventually it will become null
    while(second_list):
        if(second_list.val!=first_list.val):
            return False
        second_list = second_list.next
        first_list = first_list.next
    return True

        
