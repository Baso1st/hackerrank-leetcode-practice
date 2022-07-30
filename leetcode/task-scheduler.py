#https://leetcode.com/problems/task-scheduler/
#621. Task Scheduler


import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        
        time = 0
        q = deque()
        while q or heap:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
                
        return time
                        

################################## A bit more effecient math solution from leetcode solutions tab ######################################

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)
