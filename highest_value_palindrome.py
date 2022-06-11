#https://www.hackerrank.com/challenges/richie-rich/problem#:~:text=Palindromes%20are%20strings%20that%20read,of%20changes%20you%20can%20make.

def highestValuePalindrome(s, n, k):
    if is_palindrome(s):
        return maximize(s, k)
    elif k == 0:
        return '-1'
    else:
        pal_s, new_k = make_it_palindrome(s, k)
        if new_k < 0:
            return '-1'

        pal_s_9, new_k_9 = make_it_palindrome_v9(s, k)
        if new_k_9 < 0:
            return maximize(pal_s, new_k)

        maxed_1 = maximize(pal_s, new_k)
        maxed_2 = maximize(pal_s_9, new_k_9)

        return str(max(int(maxed_1), int(maxed_2)))


def make_it_palindrome(s, allowed):
    mid = len(s) // 2
    i = 0
    j = len(s) - 1
    s_arr = list(s)
    while i < mid and j >= mid:
        if s_arr[i] != s_arr[j]:
            s_arr[i] = s_arr[j] = max(s_arr[i], s_arr[j])
            allowed -= 1
        i += 1
        j -= 1
    return (''.join(s_arr), allowed)


def make_it_palindrome_v9(s, allowed):
    mid = len(s) // 2
    i = 0
    j = len(s) - 1
    s_arr = list(s)
    while i < mid and j >= mid:
        if s_arr[i] != s_arr[j]:
            if s_arr[i] != '9':
                allowed -= 1
            if s_arr[j] != '9':
                allowed -= 1                    
            s_arr[i] = s_arr[j] = '9'
        i += 1
        j -= 1
    return (''.join(s_arr), allowed)


def maximize(s, allowed):
    if allowed == 0:
        return s
    if len(s) % 2 == 0 and allowed % 2 != 0:
        return s

    mid = len(s) // 2
    i = 0
    j = len(s) - 1
    s_arr = list(s)
    while allowed > 1 and i < mid and j >= mid:
        if s_arr[i] != '9':
            s_arr[i] = s_arr[j] = '9'
            allowed -= 2
    
    if allowed == 1:
        s_arr[mid] = '9'
        allowed -= 1
    return ''.join(s_arr)


def is_palindrome(s):
    mid = len(s) // 2
    i = 0
    j = len(s) - 1
    while i < mid and j >= mid:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    print(highestValuePalindrome('1231', 4, 3), '9339')
    print(highestValuePalindrome('12321', 5, 1), '12921')
    print(highestValuePalindrome('3943', 4, 1), '3993')
    print(highestValuePalindrome('092282', 6, 3), '992299')
    print(highestValuePalindrome('0011', 4, 1), '-1')
    # print(make_it_palindrome('1231', 3))
    # print(make_it_palindrome_v9('1231', 3))
    # print(maximize('1331', 2))
