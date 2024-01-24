#There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
# Note: Start the array with positive elements.
# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5

#Approach 1: Create two arrays of negative and positive numbers.
#we notice that on even indexes the positive numbers will be stored, in negative indexes the negative numbers will be stored.
def rearrange_array_elements(nums):
    pos,neg = [],[]
    #add positive elements to the pos list, negative elements to the neg list.
    for i in range(len(nums)):
        if(nums[i]<0):
            neg.append(nums[i])
        else:
            pos.append(nums[i])
    res = [0]*len(nums) #list to hold the final list
    pos_index = 0  #variable to keep track of current element of the pos list
    neg_index = 0  #variable to keep track of current element of the neg list
    ind = 0  ##variable to keep track of current element of the res list
    while(pos_index<len(pos) and neg_index<len(neg)):   #we only want to loop till we have elements left in both neg and pos.
        if(ind%2==0):
            res[ind] = pos[pos_index]
            pos_index+=1
        else:
            res[ind] = neg[neg_index]
            neg_index+=1
        ind+=1
    #loop to fill the remaining elements of the neg list if there are negative elements remaining.
    while(neg_index<len(neg)):
        res[ind] = neg[neg_index]
        ind+=1
        neg_index+=1
    #loop to fill the remaining elements of the pos list if there are positive elements remaining.
    while(pos_index<len(pos)):
        res[ind] = pos[pos_index]
        ind+=1
        pos_index+=1
    return res

l = [1, 2, -4, -5, 3, 4,-6,7]
print(rearrange_array_elements(l)) 

#Approach2 : if the number of positves and no of negtaives are equal. In one pass we can set the neg and pos index, start with pos=0,neg=1
# at each iteration increase pos+=2 if a pos number is set, else neg+=2 if a neg number is set
# will only work if equal number of positive and negative elements are present.

def rearrange_array_elements2(nums):
    res = [0]*len(nums)
    pos_index,neg_index = 0,1
    for i in range(len(nums)):
        if(nums[i]>0):
            res[pos_index] = nums[i]
            pos_index+=2
        else:
            res[neg_index] = nums[i]
            neg_index+=2
    return res

l = [1,2,-4,-5]
print(rearrange_array_elements2(l))