# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        std_node = head
        cur_node = head.next if head else None
        
        while cur_node:
            if std_node.val == cur_node.val:
                std_node.next = cur_node.next
            else:
                std_node = cur_node
            cur_node = cur_node.next
        return head
            
                