#https://leetcode.com/problems/combination-sum/
#39. Combination Sum

from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = defaultdict(set)
        cache[0] = [set()]
        
        for i in range(1, target+1):
            for can in [x for x in candidates if x <= i]:
                rem = i - can
                if rem in cache:
                    for val in cache[rem]:
                        new_val = list(val)
                        new_val.append(can)
                        cache[i].add(tuple(sorted(new_val)))        
                            
                            
        return cache[target] if target in cache else []

##################### A better Solution using backtracking. The solution is from leetcode solution tab and it has a very complex time complexity) ############## 

from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = set()
        self.candidates = candidates
        self.backtrack(target, [], 0)
        return self.result
        
    def backtrack(self, target, ances, start):
        if target < 0:
            return
        if target == 0:
            tup = tuple(sorted(ances))
            self.result.add(tup)
            return
        
        for i in range(start, len(self.candidates)):
            can = self.candidates[i]
            if can <= target:
                ances.append(can)
                self.backtrack(target - can, ances, i)
                ances.remove(can)