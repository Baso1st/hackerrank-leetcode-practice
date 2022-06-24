import functools

def sort_func(a, b):
    if a[0] == b[0]:
        return 0
    elif a[0] > b[0]:
        return 1
    else:
        return -1

if __name__ == '__main__':
    arr = [[1,3],[15,18],[2,6],[8,10]]
    
    arr.sort(key=functools.cmp_to_key(sort_func))
    sorted_arr = sorted(arr, key=functools.cmp_to_key(sort_func))
    print(arr)
    print(sorted_arr)