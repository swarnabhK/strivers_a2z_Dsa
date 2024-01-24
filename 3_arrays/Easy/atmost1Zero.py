# Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
#since the string only contains 1 and 0, we can find the longest string that contains atmost one zero, that will be the required answer
# a valid window is one that contains only one zero.

def atmostOneZero(arr):
    left,count_zeroes,max_length = 0,0,0
    window = 0
    for right in range(len(arr)):
        if(arr[right]=='0'):
            count_zeroes+=1  #if we find a zero increase zero count for current window.
        while(count_zeroes>1):
            if(arr[left]=='0'):  #keep shrinking the window till we encounter that zero and remove it. 
                count_zeroes-=1 # once zero is removed the window becomes valid again.
            left+=1
        if(right-left+1>max_length):
            max_length = right-left+1   #length of longest valid window.
            window = arr[left:right+1]  #the longest window
    
    return window,max_length

longest_substring,max_length = atmostOneZero("1101100111")
print(f"The longest substring is: {longest_substring}")
print(f"Length of the longest substring is: {max_length}")