#https://leetcode.com/problems/merge-k-sorted-lists/
#23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        head = curr = ListNode()
        heap = []
        heapq.heapify(heap)
        for i, li in enumerate(lists):
            if li:
                heapq.heappush(heap, (li.val, i, li))
                
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return head.next