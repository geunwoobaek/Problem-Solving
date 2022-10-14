# https://leetcode.com/problems/edit-distance/
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# convert word1 to word2.
# word1's idx word2's idx  if word2's idx == end_idx answer 
# Insert a character
# Delete a character
# Replace a character

# fisrt approach using bruteforce
# A: ABC B: BCA
# A: ABC B: KABCF
# 1-1)현재 A의 index i에 대해 B[i]와 같다면 i+=1을 한다.
# 1-2)현재 A의 index i에 대해 A[i]를 삭제하거나, B[i]로 대체하거나, B[i]를 i에 추가하거나 선택가능 
#    cnt+=1 을한다.
# 모든 (1-1 - 1-2)에 대한 모든 분기에 대해 cnt가 가장 적은것을 반환한다.
from collections import deque
import heapq


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cnt = 0
        visit_check = set()
        que = []
        que.append([0,0,word1]) # cnt, idx, word
        visit_check.add((0,word1))
        while que:
            cnt, idx, word = heapq.heappop(que)
            if word == word2:
                return cnt
            while idx < len(word) and idx < len(word2) and word[idx] == word2[idx]:
                idx+=1
            
            candidates = []
            
            # 삭제
            if idx < len(word):
                next_word = word[:idx]+word[idx+1:]
                candidates.append([cnt+1, idx, next_word])
            
            # 대체
            if idx < len(word) and idx < len(word2):
                next_word = word[:idx]+word2[idx]+word[idx+1:]
                candidates.append([cnt+1, idx+1, next_word])
          
            # 추가
            if idx <= len(word) and idx < len(word2):
                next_word = word[:idx]+word2[idx]+word[idx:]
                candidates.append([cnt+1, idx+1, next_word])
            
            for candidate in candidates:
                if (candidate[1], candidate[2]) not in visit_check:
                    visit_check.add((candidate[1], candidate[2]))
                    heapq.heappush(que, candidate)
        return cnt

print(Solution().minDistance("", "a") == 1)
print(Solution().minDistance("horse", "ros") == 3)
print(Solution().minDistance("intention", "execution") == 5)