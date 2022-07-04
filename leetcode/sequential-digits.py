#https://leetcode.com/problems/sequential-digits/
#1291. Sequential Digits


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        
        next_seq = self.get_next(low, high)
        while next_seq <= high:
            result.append(next_seq)
            next_seq = self.get_next(next_seq+1, high)
        
        return result
        
    def get_next(self, low, high):
        digits = '123456789'
        chunk_size = len(str(low))
        chunk = 0
        while chunk_size < 10:
            for i in range(10-chunk_size):
                chunk = int(digits[i:i+chunk_size])
                if low <= chunk <= high:
                    return chunk
            chunk_size += 1      
            
        return high+1
