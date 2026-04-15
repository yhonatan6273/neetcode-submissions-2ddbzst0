# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        fast=head
        slow=head
        cur=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next

        s1=slow.next
        s2=slow.next.next
        slow.next=None
        s1.next=None
        while s2!=None:
            temp=s2.next
            s2.next=s1
            s1=s2
            s2=temp
            
       
        while cur and s1:
            temp2=s1.next
            temp3=cur.next
            cur.next=s1
            s1.next=temp3
            cur=temp3
            s1=temp2
        

            

        


        

        