# [13,46,24,52,20,9]
#1) check if 13 is in correct place, compare with left half: no left half, 13 is in correct place.
#2) check if 46 is in correct place, compare with left half, 46>13, so correct place
#3) check if 24 is in correct place, compare with left half, 24<46, so swap the values, new arr = [13,24,46,52,20,9], check 24>13,it is in correct place.
#4) check if 52 is in correct place, compare with left half, 52>46, it is in correct place.
#5) similarly check 20, we see that the correct place is index 1, so swap (20,52), (20,46), (20,24). New arr = [13,20,24,46,52,9]
#6) similarly check 9, we see that the correct place is index 0, so swap (9,52), (9,46), (9,24),(9,20),(9,13). New arr = [9,13,20,24,46,52], whcih is sorted.
#main idea is to pick an element and compare with each element on the left half side, if smaller keep swapping till you reach the correct position.

#Time complexity is O(N**2), even if the array is sorted we are always checking the left half.
def check_and_swap(idx,arr):
    for i in range(idx,0,-1): #check the left half for each index, i starts at idx and goes till 1(so that we don't get list index missing error for 0)
        if(arr[i]<arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i] #swap the values
            
def insertion_sort_1(arr):
    for i in range(1,len(arr)):
        check_and_swap(i,arr)


l = [13,46,24,52,20,9]
insertion_sort_1(l)
print(l)


#better time complexity
def insertion_sort2(arr):
    for i in range(len(arr)):
        j = i
        #if the array is sorted we won't enter this loop and best case TC is O(N)
        while(j>0 and arr[j]<arr[j-1]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1

l = [13,46,24,52,20,9]
insertion_sort2(l)
print(l)


l2 = [13,46,24,52,20,9,9,13,46]
insertion_sort2(l2)
print(l2)