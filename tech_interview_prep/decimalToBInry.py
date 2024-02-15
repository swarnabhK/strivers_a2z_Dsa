# Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

# Input: 2
# Output: "10"
# Explanation: The binary equivalent of 2 is 10.


def decimalToBinary(num):
  st = []
  while(num>0):
    st.append(str(num%2))
    num = num//2
  return "".join(st[::-1])



print(decimalToBinary(2))    # Output: "10" (Binary representation of 2)
print(decimalToBinary(7))    # Output: "111" (Binary representation of 7)
print(decimalToBinary(18))   # Output: "10010" (Binary representation of 18)