#https://www.hackerrank.com/challenges/richie-rich/problem#:~:text=Palindromes%20are%20strings%20that%20read,of%20changes%20you%20can%20make.

import time

def highestValuePalindrome(s, n, k):
    s = list(s)
    if k == 0 and is_palindrome(s):
        return ''.join(s)
    elif k == 0:
        return '-1'
    elif is_palindrome(s):
        return ''.join(maximize(s, k, n*[False]))
    else:
        changed = n * [False]
        pal_s, new_k = make_it_palindrome(s, k, changed)
        if new_k < 0:
            return '-1'
        maxed_1 = maximize(pal_s, new_k, changed)
        return ''.join(maxed_1)


def make_it_palindrome(s, k, changed):
    mid = len(s) // 2
    i = 0
    j = len(s) - 1
    s_arr = list(s)
    while i < mid and j >= mid and k >= 0:
        if s_arr[i] != s_arr[j]:
            s_arr[i] = s_arr[j] = max(s_arr[i], s_arr[j])
            changed[i] = changed[j] = True
            k -= 1

        i += 1
        j -= 1
    return (s_arr, k)


def maximize(s_arr, k, changed):
    if k == 0:
        return s_arr
    mid = len(s_arr) // 2
    i = 0
    j = len(s_arr) - 1
    while k > 0 and i <= mid and j >= mid:
        if s_arr[i] != '9':
            if i == j:
                s_arr[i] = '9'
                k -= 1
            elif changed[i]:
                k -= 1
                s_arr[i] = s_arr[j] = '9'
            elif k >= 2:
                k -= 2
                s_arr[i] = s_arr[j] = '9'

        i += 1
        j -= 1
    return s_arr


def is_palindrome(s):
    mid = len(s) // 2
    right_start = mid if len(s) % 2 == 0 else mid +1
    if s[:mid] == (s[right_start:])[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(highestValuePalindrome('1231', 4, 3) == '9339')
    print(highestValuePalindrome('12321', 5, 1) == '12921')
    print(highestValuePalindrome('3943', 4, 1) == '3993')
    print(highestValuePalindrome('092282', 6, 3) == '992299')
    print(highestValuePalindrome('0011', 4, 1) == '-1')
    print(highestValuePalindrome('3943', 4, 4) == '9999')
    print(highestValuePalindrome('777', 3, 0) == '777')