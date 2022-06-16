#https://leetcode.com/problems/diet-plan-performance/

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        point = 0
        total = sum(calories[:k])
        if total > upper:
            point += 1
        elif total < lower:
            point -= 1
        
        for i in range(1, n - k + 1):
            j = i + k -1
            total -= calories[i-1]
            total += calories[j]
            if total > upper:
                point += 1
            elif total < lower:
                point -= 1

        return point