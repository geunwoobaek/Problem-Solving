
# 만약에 abc, ac가 들어오면
# trie.root[a].count = 2
# trie.root[a].root[b].count = 1
# trie.root[a].root[b].root[c].count = 1
# trie.root[a].root[c].count = 1
from typing import List


class Trie:
    def __init__(self, isStart = False):
        self.root = {}
        self.count = 0
        self.isStart = isStart

    def insert(self, word, idx = 0):
        node = self.root
        self.count += 1
        if idx == len(word):
            return
        if word[idx] not in node:
            node[word[idx]] = Trie()
        node[word[idx]].insert(word, idx+1)

    def getCount(self, word, idx = 0):
        if self.isStart:
            return self.root[word[idx]].getCount(word, idx+1)
        if idx == len(word):
            return self.count
        return self.count + self.root[word[idx]].getCount(word, idx+1)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie(True)
        for word in words:
            trie.insert(word)
        return [trie.getCount(word) for word in words]



print(Solution().sumPrefixScores(["abc","ab","bc", "b"]))
