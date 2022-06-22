#2310. Sum of Numbers With Units Digit K ===> AKA Coin Chnage AKA knapsack problem
#https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/submissions/
#Two solutions are provided for this problem. There is a better one as well using dynamic programming bottom up approach

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0 :
            return 0
        if k == 0 and num % 10 != 0:
            return -1 
        
        all_ints = []
        
        i = k
        while i <= num:
            all_ints.append(i)
            i += 10
        
        all_ints = list(reversed(all_ints))

        result = []
        
        temp_num = num
        result_sum = 0
        count = 0
        for val in all_ints:
            if temp_num == 0 or result_sum >= num:
                break
            if temp_num < val:
                continue
            while temp_num > 0 and self.has_divisor(temp_num - val, all_ints):
                count += 1
                temp_num -= val
                result_sum += val
        
        if result_sum == num:
            return count
        
        return -1
    

    def has_divisor(self, rem, arr):
        if rem < 0:
            return False
        for val in arr:
            if rem % val == 0:
                return True
            
        return False
    
#######################Below is top down approach using dynamic programming#####################
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if k == 0 and num % 10 != 0:
            return -1         
        all_ints = []
        
        i = k
        while i <= num:
            if i :
                all_ints.append(i)
            i += 10

        memo = {}
        memo[0] = 0
        self.least_count(num, all_ints, memo)
        if num in memo:
            return memo[num] if memo[num] < float('inf') else -1
        else:
            return -1          

    def least_count(self, num, arr, memo):

        if num == 0:
            return 0

        if num in memo:
            return memo[num]            

        min_val = float('inf')
        for val in arr:
            if val > num:
                continue
            result = 1 + self.least_count(num - val, arr, memo)
            min_val = min(min_val, result)
        

        memo[num] = min_val
        return memo[num]



# 58
# 9
# 37
# 2
# 0
# 7
# 5
# 1
# 10
# 5
# 4
# 0
# 10
# 0
# 18
# 3
# 30
# 4
# 20
# 1
