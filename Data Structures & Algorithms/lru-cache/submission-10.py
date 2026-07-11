class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.dummyL=Node(0,0)
        self.dummyR=Node(0,0)
        self.dummyL.next=self.dummyR
        self.dummyR.prev=self.dummyL
        

    def remove(self,node:Node):
        prv,nxt=node.prev,node.next
        prv.next=nxt
        nxt.prev=prv

    def insert(self,node:Node):
        prv,nxt=self.dummyR.prev,self.dummyR
        nxt.prev=node
        node.next=nxt
        prv.next=node
        node.prev=prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity==len(self.cache):
                remove_node=self.dummyL.next
                del  self.cache[remove_node.key]
                self.remove(remove_node)
               
            self.cache[key]=Node(key,value)
            self.insert(self.cache[key])

        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val=value

        
