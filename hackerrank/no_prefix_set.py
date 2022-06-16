#https://www.hackerrank.com/challenges/no-prefix-set/problem

class TrieNode:
    def __init__(self):
        self.children: dict = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self) -> None:
        self._root = TrieNode()
        self._count = 0
         

    def add(self, word):
        self._add_recursive(self._root, word, 0)


    def _add_recursive(self, node: TrieNode, word: str, index: int):
        if index >= len(word):
            node.isEndOfWord = True
            return
        
        char = word[index]
        if char in node.children:
            nextNode = node.children[char]
        else:
            nextNode = TrieNode()
            node.children[char] = nextNode
            self._count += 1

        self._add_recursive(nextNode, word, index + 1)


    def contains(self, word) -> bool:
        if len(word) == 0:
            return False
        return self._search_recursive(self._root, word, 0)


    def _search_recursive(self, node: TrieNode, word, index):
        if index == len(word):
            return node.isEndOfWord

        char = word[index]
        if char not in node.children:
            return False

        nextNode = node.children[char]
        return self._search_recursive(nextNode, word, index + 1)


    def contains_words_with_prefix(self, prefix):
        return self._contains_with_prefix_recursive(self._root, prefix, 0)


    def _contains_with_prefix_recursive(self, node:TrieNode, prefix, index):
        if index == len(prefix):
            return True

        char = prefix[index]
        if char in node.children:
            nextNode = node.children[char]
            return self._contains_with_prefix_recursive(nextNode, prefix, index + 1)
        
        return False


    def contains_word_thats_prefix_of(self, word):
        return self._contains_word_thats_prefix_of(self._root, word, 0)


    def _contains_word_thats_prefix_of(self, node: TrieNode, word, index):
        if index == len(word):
            return False
        
        char = word[index]
        if char in node.children:
            next_node = node.children[char]
            if next_node.isEndOfWord:
                return True
            return self._contains_word_thats_prefix_of(next_node, word, index+1)
        
        return False

        
def noPrefix(words):
    trie = Trie()
    for word in words:
        if trie.contains_words_with_prefix(word) or trie.contains_word_thats_prefix_of(word):
            print('BAD SET')
            print(word)
            return
        trie.add(word)
    print('GOOD SET')

