# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        
        prv_node = head
        cur_node = head.next
        head.next = None
        while True:
            if not cur_node:
                return prv_node
            
            next_node = cur_node.next
            cur_node.next = prv_node
            prv_node = cur_node
            cur_node = next_node
            
        
        