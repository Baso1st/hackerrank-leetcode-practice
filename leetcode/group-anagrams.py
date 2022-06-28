#https://leetcode.com/problems/group-anagrams/
#49. Group Anagrams


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        
        result = []
        for key, value in anagrams.items():
            result.append(value)
            
        return result
    
    
    def get_bit_map(self, str1):
        result = 0
        for c in str1:
            bits = (1 << ord(c) - ord('a'))
            result |= bits
        return (len(str1), result)