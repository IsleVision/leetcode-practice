class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.isWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            idx = ord(l)-ord('a')
            if not cur.children[idx]:
                cur.children[idx]=TrieNode()
            cur = cur.children[idx]
        cur.isWord=True

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            child=cur.children[ord(l)-ord('a')]
            if not child:
                return False
            cur = child
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
            child=cur.children[ord(l)-ord('a')]
            if not child:
                return False
            cur = child
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)