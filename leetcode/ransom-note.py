#https://leetcode.com/problems/ransom-note/
#383. Ransom Note


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        maga_freq = [0] * 26

        for c in magazine:
            maga_freq[ord(c) - ord('a')] += 1
                
        for c in ransomNote:
            idx = ord(c) - ord('a')
            maga_freq[idx] -= 1
            if maga_freq[idx] < 0:
                return False

        return True
