from collections import defaultdict, deque
from typing import List
from sortedcontainers import SortedList


# time, 문자열에 맞게 정렬 되게끔 자료구조 만들면 된다.
# 다만 문자열의 time을 추가하기 위해서는 어떻게 해야하나?
# 문자열 -> time
class SearchEngine:
    def __init__(self):
        self.index = defaultdict(SortedList)
        self.data = defaultdict(int)
        self.prefix_input = ""
        self._ascill_sentence = {}

    def sort_func(self, x):
        # x[0] = 숫자, x[1] = 문자열
        # 숫자가 크고, 문자열의 아스키코드가 큰 순서대로 정렬
        return (-x[0], x[1])

    def insert(self, sentence, time):
        curr = ''
        new_record = []
        aggregate_time = self.data.get(sentence, 0)
        new_record = (aggregate_time + time, sentence)
        for c in sentence:
            curr += c
            if sentence in self.data:
                self.index[curr].remove((aggregate_time, sentence))
            if curr not in self.index:
                self.index[curr] = SortedList([new_record], key=self.sort_func)
            else:
                self.index[curr].add(new_record)
        self.data[sentence] = new_record[0]

    def search(self, c):
        if c == '#':
            self.insert(self.prefix_input, 1)
            self.prefix_input = ''
            return []
        self.prefix_input += c
        result = []
        if self.prefix_input not in self.index:
            result = []
        result = list(i[1] for i in self.index[self.prefix_input])
        return result[:3]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.engine = SearchEngine()
        sentenses_times = list(zip(sentences, times))
        sentenses_times.sort(key=lambda x: (-x[1], x[0]))
        for sentence, time in sentenses_times:
            self.engine.insert(sentence, time)

    def input(self, c: str) -> List[str]:

        res = self.engine.search(c)
        # print(f'input: {c}, res: {res}')
        return res

# class TrieNode(object):
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False
#         self.data = None
#         self.rank = 0
        
# class AutocompleteSystem(object):
#     def __init__(self, sentences, times):
#         self.root = TrieNode()
#         self.keyword = ""
#         for i, sentence in enumerate(sentences):
#             self.addRecord(sentence, times[i])

#     def addRecord(self, sentence, hot):
#         p = self.root
#         for c in sentence:
#             if c not in p.children:
#                 p.children[c] = TrieNode()
#             p = p.children[c]
#         p.isEnd = True
#         p.data = sentence
#         p.rank -= hot
    
#     def dfs(self, root):
#         ret = []
#         if root:
#             if root.isEnd:
#                 ret.append((root.rank, root.data))
#             for child in root.children:
#                 ret.extend(self.dfs(root.children[child]))
#         return ret
        
#     def search(self, sentence):
#         p = self.root
#         for c in sentence:
#             if c not in p.children:
#                 return []
#             p = p.children[c]
#         return self.dfs(p)
    
#     def input(self, c):
#         results = []
#         if c != "#":
#             self.keyword += c
#             results = self.search(self.keyword)
#         else:
#             self.addRecord(self.keyword, 1)
#             self.keyword = ""
#         return [item[1] for item in sorted(results)[:3]]