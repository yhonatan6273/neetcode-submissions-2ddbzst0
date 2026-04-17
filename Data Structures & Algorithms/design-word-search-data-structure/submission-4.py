class TreeNode:
    def __init__(self):
        self.childrens={}
        self.endword=False
class WordDictionary:

    def __init__(self):
        self.root=TreeNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.childrens:
               cur.childrens[c]=TreeNode()
            cur=cur.childrens[c]
        cur.endword=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        def dfs(i,word,cur):
            if i==len(word):
                if cur.endword:
                    return True
                return False

            c=word[i]
            if c==".":
                for child in cur.childrens.values():
                    if dfs(i+1,word,child):
                        return True
                return False
            elif c not in cur.childrens:
                return False
            return dfs(i+1,word,cur.childrens[c])
        return dfs(0,word,cur)








            

        
