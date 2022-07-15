#https://leetcode.com/problems/word-break/
#139. Word Break
#Honestly had to watch this video https://www.youtube.com/watch?v=Sx9NNgInc3A&ab_channel=NeetCode 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
                
        return dp[0]
        
        