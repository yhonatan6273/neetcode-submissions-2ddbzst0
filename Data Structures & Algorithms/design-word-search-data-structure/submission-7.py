class TreeNode:
    def __init__(self):
        self.childrens={}
        self.found=False
class WordDictionary:

    def __init__(self):
        self.root=TreeNode()

        

    def addWord(self, word: str) -> None:
        cur=self.root
        for w in word:
            if w in cur.childrens:
                cur=cur.childrens[w]
            else:
                cur.childrens[w]=TreeNode()
                cur=cur.childrens[w]
        cur.found=True
        

        

    def search(self, word: str) -> bool:
        cur=self.root
        def dfs(i,word,cur):
            if i==len(word):
                if cur.found==True:
                    return True
                return False
            w=word[i]
            if w==".":
                for child in cur.childrens.values():
                    if dfs(i+1,word,child):
                        return True
                return False
            elif w not in cur.childrens:

                return False
            return dfs(i+1,word,cur.childrens[w])
        return dfs(0,word,cur)

