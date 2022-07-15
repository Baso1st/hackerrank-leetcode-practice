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
        



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        stack = []
        branches = []
        self.backtrack(s, 0, wordDict, stack, branches)
        
        return branches
    
    def backtrack(self, s, i, wordDict, stack, branches):
        if i >= len(s):
            branches.append(' '.join(stack))
            return
        for w in wordDict:
            if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                stack.append(w)
                self.backtrack(s, i+len(w), wordDict, stack, branches)
                stack.pop()
        
        return False