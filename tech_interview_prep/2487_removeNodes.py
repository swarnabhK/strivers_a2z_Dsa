# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.


class Solution:
    def removeNodes(self, head):
        st = []
        temp = head
        while(temp):
            while(st and temp.val>st[-1].val):
                st.pop()
            if st:
                st[-1].next = temp
            else:
                head = temp
            st.append(temp)
            temp = temp.next
        return head