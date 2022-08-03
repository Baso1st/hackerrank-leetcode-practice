#https://leetcode.com/problems/maximum-profit-in-job-scheduling/
#1235. Maximum Profit in Job Scheduling


from collections import defaultdict
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        
        jobs.sort()
        
        dp = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            job = jobs[i]
            next_job_idx = self.get_next_job(jobs, job[1])
            curr_profit = job[2]
            if next_job_idx != n:
                curr_profit = curr_profit + dp[next_job_idx]
            
            dp[i] = curr_profit
            if i < n-1:
                dp[i] = max(curr_profit, dp[i+1])
        return dp[0]
    
    
    def get_next_job(self, jobs, end):
        left = 0
        right = len(jobs) - 1
        next_job_idx = len(jobs)
        
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][0] >= end:
                next_job_idx = mid
                right = mid -1
            else:
                left = mid + 1
                
        return next_job_idx
                                             