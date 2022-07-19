#https://leetcode.com/problems/longest-palindrome/
#409. Longest Palindrome

from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_table = defaultdict(int)
        palin_length = 0
        odd_count = 0
        for c in s:
            freq_table[c] += 1
            odd_count += 1
            if freq_table[c] == 2:
                palin_length += 2
                freq_table[c] = 0
                odd_count -= 2
    
        return palin_length + 1 if odd_count else palin_length
        
        
            
            