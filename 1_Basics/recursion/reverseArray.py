#reverse an array using recursion

#[1,2,3,4], swap(ends)

def reverse(arr,start,end):
    if(start>=end):
        return
    arr[start],arr[end] = arr[end],arr[start]
    reverse(arr,start+1,end-1)

arr = [1,2,3,4]
print("Before reverse")
print(arr)
reverse(arr,0,len(arr)-1)
print("After reverse")
print(arr)
