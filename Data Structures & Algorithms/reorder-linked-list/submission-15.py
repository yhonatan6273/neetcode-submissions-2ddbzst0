# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        s,f=head,head
        while f and f.next:
            s=s.next
            f=f.next.next
        cur_s=s
        secendS=s.next
        cur_s.next=None
        prev=None
        cur=secendS
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        startL,startR=head,prev
        while startR:
            temp1=startR.next
            temp2=startL.next
            startL.next=startR
            startR.next=temp2
            startR=temp1
            startL=temp2
            

        