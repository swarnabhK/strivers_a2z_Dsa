# Given an array, print the Next Greater Element (NGE) for every element.

# The Next Greater Element for an element x is the first greater element on the right side of x in the array.

# Elements for which no greater element exist, consider the next greater element as -1.

# Example 1:

#  Input: [4, 5, 1, 2, 25]
#  Output: [5, 25, 2, 25, -1]


# start from the end of the array, if empty add -1 as the result. 
# if number at top is less than the current number, pop the top and check the other elements, keep doing this unless you find a top> number. if not -1
# push the current element.

def nextGreaterElement(nums):
  res = [-1]*len(nums)
  st = []
  for i in range(len(nums)-1,-1,-1):
    #case where the top is greater than the current number 
    if st and st[-1]>nums[i]:
      res[i] = st[-1]
    elif st and st[-1]<=nums[i]:
      while(st and st[-1]<=nums[i]):
        st.pop()
      if st:
        res[i] = st[-1]
    st.append(nums[i])
  return res


print(nextGreaterElement([4, 5, 1, 2, 25]))

print(nextGreaterElement([6, 6, 6, 6, 6]))


        