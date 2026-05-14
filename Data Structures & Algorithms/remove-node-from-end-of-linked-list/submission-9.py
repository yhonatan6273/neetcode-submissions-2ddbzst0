# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end=head
        counter=0
        while end:
            counter+=1
            end=end.next
        cur=0
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        
        while cur!=counter-n:
            cur+=1
            prev=prev.next
        cur_rem=prev.next
        prev.next=cur_rem.next
        cur_rem.next=None
        return dummy.next
