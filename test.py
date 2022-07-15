if __name__ == '__main__':
    x = [1, 2]
    y = [[2, 1], [2, 3], [3, 4]]
    #print(x in y)
    print(max(2, 2))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        for i, val in enumerate(nums):
            look_for = target - val
            if val in table:
                table[val].append(i)
            else:
                table[val] = [i]
        
        for key, val in table.items():
            if key + key == target:
                if len(val) > 1:
                    return val[0:2]
                else: 
                    continue

            look_for = target - key
            
            if look_for in table:
                indicies = [val[0], table[look_for][0]]
                return indicies
            
        raise Exception("Couldn't find an answer....")

        
        