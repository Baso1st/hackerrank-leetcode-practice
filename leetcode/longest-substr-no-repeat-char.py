#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#3. Longest Substring Without Repeating Characters


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        char_table = defaultdict(int)
        start = 0
        for i, c in enumerate(s):
            if c in char_table and char_table[c] >= start:
                longest = max(longest, i - start)
                start = char_table[c]+1
                char_table[c] = i
            else:
                char_table[c] = i
         
        return max(longest, n - start)

############## Using sliding window, better space complexity ##############

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        start = 0
        chars = [0] * 128
        for i in range(n):
            r = s[i]
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[start]
                chars[ord(l)] -= 1
                start += 1
            longest = max(longest, i - start + 1)
            

        return longest
             