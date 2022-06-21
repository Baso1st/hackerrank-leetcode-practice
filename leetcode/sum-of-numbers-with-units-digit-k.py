#2310. Sum of Numbers With Units Digit K
#https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/submissions/

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



                    if i in dp and (1 + dp[prev]) < dp[i]:
                        dp[i] = 1 + dp[prev]
                    else:
                        dp[i] = 1 + dp[prev]