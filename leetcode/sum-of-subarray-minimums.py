#https://leetcode.com/problems/sum-of-subarray-minimums/
#907. Sum of Subarray Minimums


########### My solution O(N**2)#############
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mins = []
        tally = 0
        n = len(arr)
        for i in range(n):
            min_val = arr[i]
            tally += min_val
            for j in range(i+1, n):
                min_val = min(min_val, arr[j])
                tally += min_val
            
        return tally % ( (10**9) + 7)


############ A better solution O(N) ############
# The following solution is explained in the following article and video
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/2118729/Very-detailed-stack-explanation-O(n)-or-Images-and-comments
# https://www.youtube.com/watch?v=9-TXIVEXX2w&t=12s&ab_channel=Fraz
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        n = len(arr)
        mod = 1e9 + 7
        stack = [-1]
        total = 0
        for right_idx in range(n):
            val = arr[right_idx]
            while stack and val < arr[stack[-1]]:
                idx = stack.pop()
                left = idx - stack[-1]
                right = right_idx - idx
                total += left*arr[idx]*right
                total %= mod
            stack.append(right_idx)
        
        return int(total % mod)