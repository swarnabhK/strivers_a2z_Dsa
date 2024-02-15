class Solution:
    def nextGreaterElement(self, nums1, nums2):
        st = []
        dic  = {}
        for i in range(len(nums2)-1,-1,-1):
            while(st and st[-1]<=nums2[i]):
                st.pop()
            if st:
                dic[nums2[i]] = st[-1]
            if not st:
                dic[nums2[i]] = -1
            st.append(nums2[i])
        return [dic[num] for num in nums1]
                
                
