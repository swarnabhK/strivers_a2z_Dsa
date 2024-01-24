# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
def max_ones(nums):
    maxOnes = 0
    count = 0
    for num in nums:
        if(num==1):
            count+=1
            if(count>maxOnes):
                maxOnes = count
        else:
            count = 0
    return maxOnes

prices = [1, 1, 0, 1, 1, 1,0,0,1,1,0]
print(max_ones(prices))