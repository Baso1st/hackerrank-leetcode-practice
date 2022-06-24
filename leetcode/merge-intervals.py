#https://leetcode.com/problems/merge-intervals/
#56. Merge Intervals

from ast import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        i = 0 
        j = 1
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                new_interval = [min(intervals[i][0], intervals[j][0]), max(intervals[i][1], intervals[j][1])]
                intervals[i] = None
                intervals[j] = new_interval
                
            i += 1
            j += 1
        
        intervals = list([x for x in intervals if x])
        
        return intervals
      
