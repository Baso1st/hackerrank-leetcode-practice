if __name__ == '__main__':
    print(0 - float('-inf'))



# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         task_set = set([i for i in range(len(tasks))])
#         done = set()
#         cool_down_map = defaultdict(int)
#         cool_down_count = 0
        
#         while task_set:
#             for i in task_set:
#                 if task[i] not in cool_down_map or cool_down_map[task[i]] == 0:
#                     done.add(i)
#                     cool_down_map[task[i]] = n
                    
                    
                
        
        