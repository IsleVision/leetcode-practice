class Trie:

    def __init__(self):
        self.arr=[]
        

    def insert(self, word: str) -> None:
        self.arr +=[word]
        

    def search(self, word: str) -> bool:
        return word in self.arr
        

    def startsWith(self, prefix: str) -> bool:
        for w in self.arr:
            if w.find(prefix)==0:
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)