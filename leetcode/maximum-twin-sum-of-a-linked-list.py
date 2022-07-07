#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
#2130. Maximum Twin Sum of a Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_val = 0
        
        tail = head.next
        tail.prev = head
        while tail.next:
            tail.next.prev = tail
            tail = tail.next
            
        left = head
        right = tail
        
        while left != right:
            val = left.val + right.val
            if val > max_val:
                max_val = val
            left = left.next
            if left == right:
                break
            right = right.prev
        
        return max_val
            
######################## A better solution that doesn't modify the node ########################

    class Solution:
        def pairSum(self, head: Optional[ListNode]) -> int:
            max_val = 0
            arr = []

            slow = head
            fast = head
            while fast and fast.next:
                arr.append(slow.val)
                slow = slow.next
                fast = fast.next.next

            for i in range(len(arr)-1, -1, -1):
                max_val = max(arr[i] + slow.val, max_val)
                slow = slow.next

            return max_val