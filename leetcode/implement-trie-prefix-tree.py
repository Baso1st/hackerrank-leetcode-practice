#https://leetcode.com/problems/implement-trie-prefix-tree/
#208. Implement Trie (Prefix Tree)

class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = Node()
                current = current.children[c]
                
        current.is_word = True
        

    def search(self, word: str) -> bool:
        node = self._search_aid(word)
        if not node:
            return False
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self._search_aid(prefix)
        if not node:
            return False
        return True   
        
    def _search_aid(self, prefix: str) -> Node:
        if not prefix or not self.root.children:
            return None
        current = self.root
        for c in prefix:
            if c not in current.children:
                return None
            current = current.children[c]
            
        return current
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)