# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head,head.next
        while (f and f.next):
            f=f.next.next
            s=s.next
        secend_half=s.next
        tail=s.next=None
        while (secend_half):
            temp=secend_half.next
            secend_half.next=tail
            tail=secend_half
            secend_half=temp
        first_half=head
        prev=tail
        while(prev and first_half):
            temp1=first_half.next
            temp2=prev.next
            first_half.next=prev
            first_half=temp1
            prev.next=first_half
            prev=temp2



        


        