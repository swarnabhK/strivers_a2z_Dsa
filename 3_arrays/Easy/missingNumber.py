# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.
#example, N = 5, array[] = {1,2,4,5}-> find missing number which is 3

#approach 1: adjacent elements will have a difference of 1, apart from the two adjacent elements with a missing number in between them
# in that case the difference will be 2.

def missing_number(nums, N):
    # Check if the missing number is at the beginning
    if nums[0] != 1:
        return 1
    
    # Check if the missing number is at the end
    if nums[-1] != N:
        return N
    
    # Check for the missing number in the middle
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            return nums[i-1] + 1

# Example usage:
l = [1, 3, 4, 5]
print(missing_number(l, 5))


#approach 2: using xor. xor between two same elements is 0. Xor between a 0 and an element is the element itself.
#(1^1)=0, (1^0) =1
#1 ->first do a xor with all elements from 1 to N.
#2-> do a xor of all the elements in the array
#xor 1 and 2. (elements not missing will form pairs) (1^2^3^4^5)^(1^2^3^5) = (1^1)^(2^2)^(3^3)^(5^5)^(4) = 0^0^0^0^4 = 0^4=4(missing element)
  
def missing_number_xor(nums,N):
    xor1 = 1
    for i in range(2,N+1):
        xor1 = xor1^i
    xor2 = nums[0]
    for i in range(1,len(nums)):
        xor2 = xor2^nums[i]
    missing = xor1^xor2
    return missing

  
l = [1, 2, 3, 5]
print(missing_number_xor(l, 5))


#approach 3: Use a set to put the numbers . Run a loop from 1 to N to check which number is not present in the set


def missing_number3(nums,N):
    s = set(nums)
    for i in range(1,N+1):
        if(i not in s):
            return i

l = [1, 2, 3, 5]
print(missing_number3(l, 5))