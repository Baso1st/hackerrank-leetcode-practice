# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        table = {}
        rank = 1
        for val in sorted_arr:
            if val not in table:
                table[val] = rank
                rank += 1
            
        result = []
        for val in arr:
            result.append(table[val])
            
        return result