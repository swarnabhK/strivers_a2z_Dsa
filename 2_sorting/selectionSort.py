#selection sort.
# Select the minimum at each iteration and swap with the first index of that iteration. idx = 0 for 1st iteration, idx = 1 for 2nd iteration.

def find_minimum(arr,idx):
  mini_index = 0
  minimum = arr[idx]
  for i in range(idx,len(arr)):
    if(arr[i]<=minimum):
      mini_index = i
      minimum = arr[i]
  return mini_index

def selection_sort(arr):
  #we run the outer loop for n-1 times, because we need to find the minimum n-1 times.
  for i in range(0,len(arr)-1):
    mini = find_minimum(arr,i)
    arr[i],arr[mini] = arr[mini],arr[i]

l = [13,46,24,52,20,9] 
selection_sort(l)
print(l)

l2 = [13,46,24,52,20,9,9,13,46]
selection_sort(l2)
print(l2) 