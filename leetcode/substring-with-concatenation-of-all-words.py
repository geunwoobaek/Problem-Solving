# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# constraints:
# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

# Approach 1 Brute Force
# check all possible substrings of length len(words) * len(words[0])
# and check if it is a concatenation of all words
# time compleixty = len(words)*len(words[0])*len(s) => 5000*30*10000 => 1500000000(10^9)

# how make it efficient?
# 각 인덱스 시작점에 대해 시작하는 단어 length만큼 저장한다.
# cache[i] = s[i:i+len(words[0])]
# 이것을 만드는 비용은 len(s) * len(words[0]) => 10000*30 => 300000(10^5)
# 이렇게 하면, 각 인덱스 시작점에 대해 O(1)로 확인할 수 있다.
# len(s) * len(words) + len(s) * len(words[0]) => 10000*5000 + 10000*30 => 15000000(10^7)


# how make it more efficient?
# 5
from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cache = {}
        for i in range(len(s)-len(words[0])+1):
            cache[i] = s[i:i+len(words[0])]
        result = []
        counter_words = Counter(words)
        for i in range(len(s)-len(words)*len(words[0])+1):
            # implement isConcatenation
            # check if s[i:i+len(words)*len(words[0])] is a concatenation of words
            count_dict = Counter([cache[j] for j in range(i, i+len(words)*len(words[0]), len(words[0]))])
            if count_dict == counter_words:
                result.append(i)
        return result

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9])
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == [])