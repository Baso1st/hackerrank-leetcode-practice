#https://leetcode.com/problems/integer-to-roman/
#12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
         (50, 'L'),(40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        roman_num = []
        while num > 0:
            for roman in romans:
                if num >= roman[0]:
                    quo, num = divmod(num, roman[0])
                    roman_num.append(quo * roman[1])
        return ''.join(roman_num)