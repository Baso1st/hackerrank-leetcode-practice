#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#17. Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_table = self.get_digit_table()
        
        ans = [[l] for l in digit_table[digits[0]]]
        
        for c in digits[1:]:
            new_ans = []
            for l in digit_table[c]:
                for arr in ans:
                    new_arr = list(arr)
                    new_arr.append(l)
                    new_ans.append(new_arr)
            ans = new_ans
        
        for i in range(len(ans)):
            ans[i] = ''.join(ans[i])
            
        return ans
        

    def get_digit_table(self) -> dict:
        digit_table = defaultdict(list)
        letter = 97
        for i in range(2, 10):
            i = str(i)
            for _ in range(3):
                digit_table[i].append(chr(letter))
                letter += 1
            if i == '7':
                digit_table[i].append(chr(letter))
                letter += 1
        digit_table['9'].append('z')




from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.digits = digits
        self.digit_table ={"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        self.ans = []
        self.backtrack()
        
        return self.ans
        
        
    def backtrack(self, i = 0, word = []):
        if len(word) == len(self.digits):
            self.ans.append(''.join(word))
            return
        
        for l in self.digit_table[self.digits[i]]:
            word.append(l)
            self.backtrack(i+1, word)
            word.pop()

