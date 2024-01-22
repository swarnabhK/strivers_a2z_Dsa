#array: we need to find the pivot index
#find pivot index, do quick sort on left side and do quick sort on right side.left side <pivot. right side>pivot.
# we are randomly choosing a pivot in order to reduce worst case time complexity if the array is already sorted.
import random

def find_random_pivot_index(arr, low, high):
    # Choose a random index between low and high (inclusive)
    pivot_index = random.randint(low, high)
    
    # Swap the randomly chosen pivot with the element at the low index
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    return find_pivot_index(arr, low, high)

def find_pivot_index(arr, low, high):
    i, j = low, high
    pivot = arr[low]
    
    # Partition the array into elements less than or equal to the pivot and greater than the pivot
    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i < j:
            # Swap the two elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element to its correct position
    arr[low], arr[j] = arr[j], arr[low]
    
    return j

def quick_sort(arr, low, high):
    if low < high:
        # Find a random pivot index and perform partitioning
        pivot = find_random_pivot_index(arr, low, high)
        
        # Recursively apply QuickSort on the left and right subarrays
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)


