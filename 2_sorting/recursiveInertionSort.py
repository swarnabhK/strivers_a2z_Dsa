#[1,3,2,7,6,9,0]
#for each outer loop iteration we are checking the left part of the array

#approach 1: Parameterised recursion. Here we are calling the recursive case after doing some processing(for loop)

def insertion_sort_1(arr,start,n):
    if(start>n):
        return
    for i in range(start,0,-1):
        if(arr[i]<arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
    insertion_sort_1(arr,start+1,n)

l1=[1,3,2,7,6,9,0,2]
insertion_sort_1(l1,0,len(l1)-1)
print(l1)

#approach 2: here we first keep the recursive calls on the stack and start popping them out once we reach the base condition
#IS(5)..for loop,IS(4)...for loop(),IS(3)..for loop,IS(2).. for loop,IS(1).. for loop,IS(0) base condition, return to IS(1) and execute the for loop.
#in this approach we are not using the extra variable n, to keep track of when the base condition exits.
def insertion_sort_2(arr,start):
    if(start==0):
        return
    insertion_sort_2(arr,start-1)
    for i in range(start,0,-1):
      if(arr[i]<arr[i-1]):
          arr[i],arr[i-1]= arr[i-1],arr[i]



l2=[1,3,2,7,6,9,0,2]
insertion_sort_2(l2,len(l2)-1)
print(l2)



#Best case complexity is O(N) because we won't enter the while loop if the array is already sorted.
def insertion_sort_3(arr,start,n):
    if(start>n):
        return
    j = start
    while(j>0 and arr[j]<arr[j-1]):
        arr[j],arr[j-1] = arr[j-1],arr[j]
        j-=1
    insertion_sort_3(arr,start+1,n)

l3=[1,3,2,7,6,9,0,2]
insertion_sort_2(l3,len(l3)-1)
print(l3)
