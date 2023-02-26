from collections import defaultdict, deque

class SearchEngine:
    def __init__(self):
        self.index = defaultdict(set)
        self.data = defaultdict(int)

    def insert(self, sentence, time):
        for c in sentence:
            self.index[c].add(sentence)
        self.data[sentence] += time

    def search(self, c):
        if c == '#':
            return []
        if c not in self.index:
            return []
        result = list(self.index[c])
        result.sort(key=lambda x: (self.data[x], x), reverse=True)
        return result[:3]






class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.engine = SearchEngine()
        for sentence, time in zip(sentences, times):
            self.engine.insert(sentence, time)

    def input(self, c: str) -> List[str]:
        return self.engine.search(c)
