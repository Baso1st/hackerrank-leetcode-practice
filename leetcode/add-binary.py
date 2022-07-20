#https://leetcode.com/problems/add-binary/
#67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), b)
        smaller, bigger = a.zfill(n), b.zfill(n)

        carry = '0'
        result = [''] * n
        for i in range(n-1, -1, -1):
            if carry == '0':
                if smaller[i] == '0' and bigger[i] == '0':
                    result[i] = '0'
                elif smaller[i] == '1' and bigger[i] == '1':
                    result[i] = '0'
                    carry = '1'
                else:
                    result[i] = '1'
            else:
                if smaller[i] == '0' and bigger[i] == '0':
                    result[i] = '1'
                    carry = '0'
                elif smaller[i] == '1' and bigger[i] == '1':
                    result[i] = '1'
                else:
                    result[i] = '0'                
        
        
        result = ''.join(result)
        
        if carry == '1':
            result = carry + result
        
        return result
        
        