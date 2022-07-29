#https://leetcode.com/problems/find-all-anagrams-in-a-string/
#438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_arr = self.get_char_set(p)
        ans = []
        
        prev_arr = self.get_char_set(s[:len(p)])
        if prev_arr == p_arr:
            ans.append(0)
        for i in range(1, len(s) - len(p) + 1):
            prev_arr[ord(s[i-1]) - ord('a')] -= 1
            prev_arr[ord(s[i+len(p)-1]) - ord('a')] += 1
            if prev_arr == p_arr:
                ans.append(i)

        return ans
        
    
    def get_char_set(self, word):
        arr = [0] * 26
        for c in word:
            arr[ord(c) - ord('a')] += 1
        
        return arr


########################### A similar complexity, but a slightly different approach from the leetcode solutions tab #######################


from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[s[i]] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output