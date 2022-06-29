#https://leetcode.com/problems/k-closest-points-to-origin/
#973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result_table = {}
        for point in points:
            distance = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
            if distance in result_table:
                result_table[distance].append(point)
            else:
                result_table[distance] = [point]
        
        
        output = []
        for key in sorted(result_table.keys()):
            output += result_table[key]
            if len(output) >= k:
                break

        return output[:k]