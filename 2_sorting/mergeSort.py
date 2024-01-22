    # Divide-and-Conquer: The algorithm divides the unsorted array into two halves until each subarray has a single element, establishing a base case for sorted subarrays.

    # Recursive Sorting: The recursive calls sort the first and second halves independently, ensuring each subarray is sorted.

    # Merge Step: Merging involves comparing and combining elements from two sorted halves to create a sorted result, ensuring the final array is sorted.

    # Auxiliary Array: An auxiliary array is used to store the merged result during the merging step, minimizing space complexity.

    # Time Complexity: The time complexity of Merge Sort is O(n log n), where n is the number of elements in the array. The logarithmic factor arises from the recursive division, and the linear factor comes from the merging process. This makes Merge Sort efficient for large datasets and guarantees consistent performance.


def merge(arr, low, mid, high):
    # Create an auxiliary array to store the merged result
    res = []
    
    # Initialize pointers for two halves of the array
    low1, low2 = low, mid + 1
    
    # Compare elements from the two halves and merge them into the result array
    while low1 <= mid and low2 <= high:
        if arr[low1] <= arr[low2]:
            res.append(arr[low1])
            low1 += 1
        else:
            res.append(arr[low2])
            low2 += 1
    
    # If there are remaining elements in the first half, add them to the result
    while low1 <= mid:
        res.append(arr[low1])
        low1 += 1
    
    # If there are remaining elements in the second half, add them to the result
    while low2 <= high:
        res.append(arr[low2])
        low2 += 1
    
    
    # Copy the merged result back to the original array
    for i in range(low, high + 1):
        arr[i] = res[i - low]

def merge_sort(arr, low, high):
    # Base case: when the array length is 1 (already sorted)
    if low == high:
        return
    
    # Calculate the midpoint of the array
    mid = (low + high) // 2
    
    # Recursively sort the first half
    merge_sort(arr, low, mid)
    
    # Recursively sort the second half
    merge_sort(arr, mid + 1, high)
    
    # Merge the sorted halves
    merge(arr, low, mid, high)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
