#https://leetcode.com/problems/find-median-from-data-stream/
#295. Find Median from Data Stream
# The solutions below is from LeetCode solutions tab. Obviously there are a lot of other solutions out ther simpler solutions out there, but his one is gold

import heapq

class MedianFinder:
    def __init__(self):
        self.lg_min_heap = [] # holds the larger half
        self.sm_max_heap = [] # holds the smaller half
        heapq.heapify(self.lg_min_heap)
        heapq.heapify(self.sm_max_heap)
        
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.sm_max_heap, (-1)*num)
        top = (-1)*heapq.heappop(self.sm_max_heap)
        heapq.heappush(self.lg_min_heap, top)
        
        if len(self.sm_max_heap) < len(self.lg_min_heap):
            top = heapq.heappop(self.lg_min_heap)
            heapq.heappush(self.sm_max_heap, (-1)*top)
        

    def findMedian(self) -> float:
        if len(self.sm_max_heap) > len(self.lg_min_heap):
            return self.sm_max_heap[0] * (-1)
        else:
            return ( (self.sm_max_heap[0] * (-1)) + self.lg_min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()