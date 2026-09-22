# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        s=f=head
        prev=None
        if head is None or head.next is None:
            return None
        while(f and f.next):
            prev=s
            s=s.next
            f=f.next.next
        prev.next=s.next
        return head
        
        
