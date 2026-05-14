class NodeTree:
    def __init__(self):
        self.nei={}
        self.Endword=False

class PrefixTree:

    def __init__(self):
        self.root=NodeTree()
        

    def insert(self, word: str) -> None:
        cur_root=self.root
        for c in word:
            if c not in cur_root.nei:
                cur_root.nei[c]=NodeTree()
            cur_root=cur_root.nei[c]
        cur_root.Endword=True




    def search(self, word: str) -> bool:
        cur_root=self.root
        for c in word:
            if c not in cur_root.nei:
                return False
            cur_root=cur_root.nei[c]
        return cur_root.Endword
        

    def startsWith(self, prefix: str) -> bool:
        cur_root=self.root
        for c in prefix:
            if c not in cur_root.nei:
                return False
            cur_root=cur_root.nei[c]
        return True
        
        