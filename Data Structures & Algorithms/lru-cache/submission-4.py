class Node:
    def __init__(self,key,val):
        self.val,self.key=val,key
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self,capacity):
        self.cap=capacity
        self.cache={}
        self.right,self.left=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        nxt=node.next
        pre=node.prev
        nxt.prev=pre
        pre.next=nxt
    

    
    def insert(self,node):
        pre,nxt=self.right.prev,self.right
        pre.next=nxt.prev=node
        node.next,node.prev=nxt,pre
        
    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

    def put(self,key,val):
        new_node=Node(key,val)
        if key not in self.cache:
            
            if not (len(self.cache)==self.cap):
                self.cache[key]=new_node
                self.insert(new_node)
              
            else:
                need_to_remove=self.left.next
                self.remove(need_to_remove)
                del self.cache[need_to_remove.key]
                self.cache[key]=new_node
                self.insert(new_node)  
           
        else:
            self.remove(self.cache[key])
            self.cache[key]=new_node
            self.insert(self.cache[key])
          