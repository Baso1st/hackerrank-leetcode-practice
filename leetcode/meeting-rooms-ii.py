#https://leetcode.com/problems/meeting-rooms-ii/
#253. Meeting Rooms II

from ast import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        
        intervals.sort()
        
        visited = [False for i in range(n)]
        rooms = 0
        
        for i in range(n):
            if visited[i]:
                continue
            rooms+= 1
            self.recurse(i, intervals, visited)
            
        return rooms
            
    def recurse(self, i, intervals, visited):
        if visited[i]:
            return
        visited[i] = True
        for j in range(i+1, len(intervals)):
            if not visited[j] and intervals[j][0] >= intervals[i][1]:
                self.recurse(j, intervals, visited)
                break
                
        
            
            