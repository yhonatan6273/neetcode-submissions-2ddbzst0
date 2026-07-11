# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        cur=dummy
        
        
      
        while l1 or l2 :
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            cur_sum=v1+v2+carry
            carry=cur_sum//10
            cur_val=cur_sum%10
            cur.next=ListNode(cur_val)
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry>0:
            cur.next=ListNode(carry)
            cur=cur.next

        
        return dummy.next
            



