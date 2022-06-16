#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        table = {}
        
        # each letter on it's own is a palindrom
        
        max_len = 1
        for i in range(n):
            table[i,i] = True
            
        # check for 2 letters palindroms
        start = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i, i+1] = True
                start = i
                max_len = 2
        
        # check for the rest of substr
        k = 3
        while k <= n:
            for i in range(n-k+1):
                j = i + k -1
                if j >= n:
                    break
                if (i+1, j-1) in table and s[i] == s[j]:
                    table[i, j] = True
                    if max_len < k:
                        max_len = k
                        start = i
            k += 1
        
        return s[start: start + max_len]