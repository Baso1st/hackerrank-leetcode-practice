# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_table = {}
        for c in chars:
            if c in chars_table:
                chars_table[c] += 1
            else:
                chars_table[c] = 1
        
        
        total = 0
        for word in words:
            word_table = {}
            bad = False
            for c in word:
                if c not in chars_table:
                    bad = True
                    break
                if c in word_table:
                    word_table[c] += 1
                else:
                    word_table[c] = 1
                    
            if not bad:
                for key in word_table:
                    if word_table[key] > chars_table[key]:
                        bad = True
                        break
            if not bad:
                total += len(word)
            
        return total