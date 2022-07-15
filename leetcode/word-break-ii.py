#https://leetcode.com/problems/word-break-ii/
#140. Word Break II
# Solved this one after #139. Word Break, they are the same idea, except this one is a bit more complex. 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for x in range(len(s)+1)]
        dp[-1].append('')
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and w == s[i:i+len(w)]:
                    for val in dp[i+len(w)]:
                        if val:
                            dp[i].append(w + ' ' + val)
                        else:
                            dp[i].append(w)

        return dp[0]
        