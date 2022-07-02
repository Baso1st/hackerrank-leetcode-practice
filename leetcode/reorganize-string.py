#https://leetcode.com/problems/reorganize-string/
#767. Reorganize String
# Two working solutions below. 


from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq_table = defaultdict(int)
        for c in s:
            freq_table[c] += 1
            if freq_table[c] > (n+1) // 2: # if a char is more than half the array, we can't separate it. 
                return ""
        
        result = ['']
        
        
        while len(result) <= len(s):
            max_char = result[-1]
            max_val = 0
            for key, val in freq_table.items():
                if key == result[-1]:
                    continue
                if val > max_val:
                    max_val = val
                    max_char = key
                    
            if  max_char == result[-1]:
                return ""
            result.append(max_char)
            freq_table[max_char] -= 1
            
        return ''.join(result)

#############################################################################

from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq_table = defaultdict(int)
        
        for c in s:
            freq_table[c] += 1
            if freq_table[c] > (n+1) // 2: # if a char is more than half the array, we can't separate it. 
                return ""
        
        
        sorted_by_freq = sorted(freq_table.items(), key = lambda x : x[1], reverse = True)
        
        
        longest_str = sorted_by_freq[0][1]
        piles = [[] for x in range(longest_str)]
        
        freq_ordered_s = []
        
        for key, val in sorted_by_freq:
            for i in range(val):
                freq_ordered_s.append(key)
        while freq_ordered_s:
            for i in range(len(piles)):
                if freq_ordered_s:
                    piles[i].append(freq_ordered_s.pop(0))
        
        result = []
        for pile in piles:
            if result and result[-1] == pile[0]:
                return ""
            result += pile
                
        return ''.join(result)
