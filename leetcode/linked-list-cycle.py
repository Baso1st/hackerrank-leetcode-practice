#https://leetcode.com/problems/linked-list-cycle/
#141. Linked List Cycle



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True


######## A set solution    
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         node_set = set()
#         current = head
#         while current:
#             if current in node_set:
#                 return True
#             node_set.add(current)
#             current = current.next
            
#         return False
    
    
    
######## A hasattr solution    
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         current = head
#         while current:
#             if hasattr(current, 'visited'):
#                 return True
#             current.visited = True
#             current = current.next
            
#         return False