class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        tNd=self.trie
        for w in word:
            od = ord(w)-ord('a')
            if not tNd.children[od]:
                tNd.children[od]=TrieNode()
            tNd = tNd.children[od]
        tNd.isWord = True
        

    def search(self, word: str) -> bool:
        def searchTrie(word:str, tNd:TrieNode)->bool:
            for i in range(len(word)):
                if word[i]=='.':
                    for tcd in tNd.children:
                        if tcd and searchTrie(word[i+1:],tcd):
                            return True
                    return False
                od = ord(word[i])-ord('a')
                if not tNd.children[od]:
                    return False
                tNd = tNd.children[od]
            return tNd.isWord
        return searchTrie(word,self.trie)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)