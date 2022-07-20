# https://www.hackerrank.com/challenges/lilys-homework/problem

def lilysHomework(arr):
    sorted_arr = sorted(arr)
    count_1 = count_swaps(list(arr), sorted_arr)
    count_2 = count_swaps(list(reversed(arr)), sorted_arr)

    return min(count_1, count_2)
    

def count_swaps(arr, sorted_arr):
    count = 0
    hash = {}
    for idx, val in enumerate(arr):
        hash[val] = idx

    for idx in range(len(sorted_arr)):
        if arr[idx] != sorted_arr[idx]:
            count += 1
            other_idx = hash[sorted_arr[idx]]
            hash[sorted_arr[idx]] = idx
            hash[arr[idx]] = other_idx
            arr[idx], arr[other_idx] = sorted_arr[idx], arr[idx]

    return count



if __name__ == '__main__':
    print(lilysHomework([7, 15, 12, 3]))
    print(lilysHomework([2, 5, 3, 1]))
    print(lilysHomework([3, 4, 2, 5, 1]))
    
