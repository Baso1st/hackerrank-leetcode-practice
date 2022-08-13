#substring-with-concatenation-of-all-words
#30. Substring with Concatenation of All Words


from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []
        word_table = Counter(words)
        n = len(words)
        word_len = len(words[0])
        print(word_table)
        print('*'*10)
        for i in range(len(s) - (word_len * n)):
            substr = s[i: i + word_len * n]
            sub_words = [ substr[j:j+word_len] for j in range(0, len(substr), word_len) ]
            sub_table = Counter(sub_words)
            print(sub_table)
            good_idx = True
            for key, val in sub_table.items():
                if key not in word_table or word_table[key] != val:
                    good_idx = False
                    break
                    
            if good_idx:
                output.append(i)
        
        return output