# https://www.hackerrank.com/challenges/between-two-sets/problem


from math import gcd

def getTotalX(a, b):
    gcd_b = arr_gcd(b)
    lcm_a = arr_lcm(a)

    result = []
    lcm_multiple = lcm_a

    while lcm_multiple <= gcd_b:
        if gcd_b % lcm_multiple == 0:
            result.append(lcm_multiple)
        lcm_multiple += lcm_a
    
    return len(result)


def arr_lcm(arr):
    if len(arr) == 1:
        return arr[0]
    lcm_arr = lcm(arr[0], arr[1])
    if len(arr) > 2:
        for val in arr[2:]:
            lcm_arr = lcm(lcm_arr, val)
    return lcm_arr


def arr_gcd(arr):
    if len(arr) == 1:
        return arr[0]
    result = gcd(arr[0], arr[1])
    for val in arr[2:]:
        if result == 1:
            break
        result = gcd(result, val)
    return result


def lcm(x, y):
    return (x * y) // gcd(x, y)


if __name__ == '__main__':
    print(getTotalX([2, 4], [16, 32, 96]))
    print(getTotalX([3, 4], [24, 48]))
    print(getTotalX([2], [20, 30, 12]))
    print(getTotalX([3, 9, 6], [36, 72]))