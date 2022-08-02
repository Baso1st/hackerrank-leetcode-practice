#https://leetcode.com/problems/word-ladder/
#127. Word Ladder
# The problem is finding the shortest path in a graph(BFS), but leetcode solution tab had the below solutions that search from both end of the graph. It is beautiful!!!

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        begin_set = {beginWord}
        end_set = {endWord}
        level = 1
        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            new_begin_set = set()
            for word in begin_set:
                for adj in self.get_adjs(word):
                    if adj in end_set:
                        return level + 1
                    if adj in word_set:
                        new_begin_set.add(adj)
                        word_set.remove(adj)
            level += 1
            begin_set = new_begin_set
        
        return 0
            
    def get_adjs(self, word):
        adjs = []
        word = list(word)
        for i, c in enumerate(word):
            for new_c in range(ord('a'), ord('z')+1):
                new_c = chr(new_c)
                word[i] = new_c
                adjs.append(''.join(word))
            word[i] = c
        return adjs