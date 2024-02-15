# Given a stack, sort it using only stack operations (push and pop).

# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The values in the stack are to be sorted in descending order, with the largest elements on top.

# Input: [34, 3, 31, 98, 92, 23]
#    Output: [3, 23, 31, 34, 92, 98]


class Solution:
    def sortStack(self,stack):
        tempStack = []
        c=0
        for _ in range(len(stack)):
            if stack:
                el = stack.pop()
            if tempStack and el<tempStack[-1]:
                c = 0
            while tempStack and el<tempStack[-1]:
                stack.append(tempStack.pop())
                c+=1
            tempStack.append(el)
            while c>0:
                tempStack.append(stack.pop())
                c-=1
        return tempStack


sol = Solution();
stack = [34, 3, 31, 98, 92, 23]
print("Input: ", stack)
print("Sorted Output: ", sol.sortStack(stack))
