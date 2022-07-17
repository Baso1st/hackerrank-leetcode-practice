#https://leetcode.com/problems/merge-two-sorted-lists/
#21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        merger = ListNode(0) #Dummy Node

        result = merger
        
        while l1 and l2:
            if l1.val <= l2.val:
                merger.next = l1
                l1 = l1.next
            else:
                merger.next = l2
                l2 = l2.next
                
            merger = merger.next
        
        merger.next = l1 or l2
            
        return result.next
            
            
        
        