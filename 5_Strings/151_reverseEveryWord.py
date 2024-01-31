# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


#reverse the whole string, trim the start and end spaces, reverse every word in the new string, remove extra spaces between words.
class Solution:
    def reverseString(self,s,l,r):
        while(l<r):
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
    def trim_spaces(self,s):
        l,r = 0,len(s)-1
        while(s[l]==" "):
            l+=1
        while(s[r]==" "):
            r-=1
        return s[l:r+1]
    def reverse_words(self,s):
        l,r = 0,0
        while(r<len(s)):
            while(r<len(s) and s[r]!=" "):
                r+=1
            self.reverseString(s,l,r-1)
            r+=1
            l = r
    def remove_extra_space(self,s):
        result = []
        prev_char = None
        for char in s:
            if char==" " and prev_char==" ":
                prev_char = char
            else:
                result.append(char)
                prev_char = char
        return "".join(result)
    def reverseWords(self, s):
        st = list(s)
        self.reverseString(st,0,len(st)-1)
        ans = self.trim_spaces(st)
        self.reverse_words(ans)
        result = self.remove_extra_space(ans)
        return result
    

solution_obj = Solution()

# Test Case 1
input_str1 = "   the sky is blue   "
result1 = solution_obj.reverseWords(input_str1)
print(result1)
# Expected Output: "blue is sky the"

# Test Case 2
input_str2 = "  hello world!  "
result2 = solution_obj.reverseWords(input_str2)
print(result2)
# Expected Output: "world! hello"

# Test Case 3
input_str3 = "a b c"
result3 = solution_obj.reverseWords(input_str3)
print(result3)
# Expected Output: "c b a"
