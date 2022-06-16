import time


def bubble_sort(arr):
    """
    Time Complexity:O(N*2)
    Space Complexity: O(1)
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    
################################################ Insertion Sort ############################################

def insertion_sort(arr):
    """
    Time Complexity:O(N*2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j -1 ] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1

################################################ Selection Sort ############################################

def selection_sort(arr):
    """
    Time Complexity:O(N*2)
    Space Complexity: O(1)
    """
    current = 0
    while current < len(arr):
        min_idx = current
        for i in range(current, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[current], arr[min_idx] = arr[min_idx], arr[current]
        current += 1


################################################ Merge Sort ################################################

def merge_sort(arr, low, high, helper):
    """
    Time Complexity:O(N LOG(N))
    Space Complexity: O(N)
    """
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid, helper)
        merge_sort(arr, mid + 1, high, helper)
        merge(arr, low, mid, high, helper)


def merge(arr, low, mid, high, helper):
    for i in range(low, high+1):
        helper[i] = arr[i]

    left_idx = low
    right_idx = mid + 1
    current = low

    while left_idx <= mid and right_idx <= high:
        if helper[left_idx] <= helper[right_idx]:
            arr[current] = helper[left_idx]
            left_idx += 1
        else:
            arr[current] = helper[right_idx]
            right_idx += 1        
        current += 1
    
    remaining = mid - left_idx
    for i in range(remaining + 1):
        arr[current+i] =  helper[left_idx + i]


################################################ Quick Sort ################################################

def quick_sort(arr, low, high):
    """
    Time Complexity:O(N*2)
    Space Complexity: O(1)
    """
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p, high)


def partition(arr, low, high):
    piviot = (low + high) // 2
    while low < high:
        while arr[low] < arr[piviot]:
            low += 1

        while arr[high] > arr[piviot]:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    
    return low


if __name__ == '__main__':
    arr = [*range(100000, 0, -1)]
    # arr = [2, 7, 3, 9, 5, 1]
    start = time.time()
    arr_copy = list(arr)
    # quick_sort(arr_copy, 0, len(arr) -1)
    # merge_sort(arr_copy, 0, len(arr) -1, len(arr)*[None])
    # selection_sort(arr_copy)
    # bubble_sort(arr_copy)
    # insertion_sort(arr_copy)
    print(time.time() - start)
    # print(arr_copy)