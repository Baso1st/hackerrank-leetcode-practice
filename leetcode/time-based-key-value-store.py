#https://leetcode.com/problems/time-based-key-value-store/
#981. Time Based Key-Value Store


########################### O(N) solution ##########################
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.table[key]
        for i in range(len(values)-1, -1, -1):
            val = values[i]
            if val[1] <= timestamp:
                return val[0]
            
        return ''


########################### O(LOG(N)) solution ##########################


from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.table[key]
        
        left = 0
        right = len(values)
        
        while left < right:
            mid = (left + right) // 2
            
            if timestamp < values[mid][1]:
                right = mid
            else:
                left = mid + 1
        
        return "" if left == 0 else values[left - 1][0]