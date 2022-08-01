#https://leetcode.com/problems/minimum-window-substring/
#76. Minimum Window Substring
#### Leetcode has a solution better than the one below, You need to take a look at it.

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        elif len(t) == len(s):
            return s if self.get_freq(s) == self.get_freq(t) else ""
        
        t_freq = self.get_freq(t)
        s_freq = self.get_freq(s)
        if not self.is_part_of(s_freq, t_freq):
            return ""

        min_sub = s
        left = 0
        right = 0
        while right <= len(s):
            freq = self.get_freq(s[left:right])
            while not self.is_part_of(freq, t_freq) and right <= len(s):
                right += 1
                if right <= len(s):
                    freq[s[right-1]] += 1
            while self.is_part_of(freq, t_freq) and left < right:
                left += 1
                freq[s[left-1]] -= 1
        
            min_sub = s[left-1:right] if len(s[left-1:right]) < len(min_sub) else min_sub
            
        return min_sub

            
    def is_part_of(self, whole, part):
        for key, val in part.items():
            if whole[key] < val:
                return False
        return True
    
    def get_freq(self, word):
        return Counter(word)