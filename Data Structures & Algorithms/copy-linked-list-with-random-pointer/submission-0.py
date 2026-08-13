"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table={None: None}
        cur=head
        while cur:
            table[cur]=Node(cur.val)
            cur=cur.next
        temp=head
        while temp:
            nxt=temp.next
            rand=temp.random
            table[temp].next=table[nxt]
            table[temp].random=table[temp.random]
            temp=temp.next
        return table[head]

        








