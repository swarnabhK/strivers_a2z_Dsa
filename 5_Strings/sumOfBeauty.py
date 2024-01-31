#     Initialize the ans variable to keep track of the total beauty sum.
#     Iterate through each character in the input string s using an outer loop (index i).
#     For each character at index i, initialize a frequency array freq to count the occurrences of each letter in the substring starting from index i.
#     Use an inner loop (index j) to extend the substring and update the frequency array accordingly.
#     For each substring, calculate the beauty sum by taking the difference between the maximum and minimum frequency in the freq array.
#     Accumulate the calculated beauty sum for each substring into the overall ans.
#     Return the final ans as the total beauty sum for the entire string.
#     In essence, the solution captures the beauty of substrings by considering the variation in the frequency of letters within each substring, and it sums up these beauty values across all possible substrings in the given string.

def beautySum(s):
    ans = 0
    for i in range(len(s)):
        freq = [0]*26
        for j in range(i,len(s)):
            ind = ord(s[j])-ord('a')
            freq[ind]+=1
            ans+=max(freq)-min(x for x in freq if x)
    return ans


print(beautySum('aabcb'))
print(beautySum('aabcbaa'))

