#https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage:
    # Just a bruteforce solution to get us started. 
    def __init__(self, size: int):
        self.size = size
        self.stream = []
        
    def next(self, val: int) -> float:
        self.stream.append(val)
        if len(self.stream) <= self.size:
            return sum(self.stream) / len(self.stream)
        else:
            self.stream.pop(0)
            return sum(self.stream) / self.size
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)