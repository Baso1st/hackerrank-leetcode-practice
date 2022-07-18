#https://leetcode.com/problems/valid-anagram/
#242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = [0] * 26
        t_freq = [0] * 26
        
        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            s_freq[s_idx] += 1
            t_idx = ord(t[i]) - ord('a')
            t_freq[t_idx] += 1
            
        return s_freq == t_freq
        
        