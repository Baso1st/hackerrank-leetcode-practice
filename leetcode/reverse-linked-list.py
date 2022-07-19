#https://leetcode.com/problems/reverse-linked-list/
#206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret
    

################# An Iterative approach. It is better and faster ###################. 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        
        return prev
        