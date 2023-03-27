# We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


# 1 <= words.length <= 100
# words[i].length == 6
# words[i] consist of lowercase English letters.
# All the strings of wordlist are unique.
# secret exists in words.
# 10 <= allowedGuesses <= 30


# approach
# if allowedGuesses >= words.length and then do sequential search 
# else
# 가능한 후보군 좁혀나가기 
# 매칭갯수가 3개일 경우 3개인 후보군이 다음 후보군이된다.
# 매칭갯수가 6개가 될경우 답리턴
# Timecomplexity = O(N) 
class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidates = words[:]
        while candidates:
            # check matching number with candidate
            mid = len(candidates) // 2
            word = candidates[mid]
            match_count = master.guess(word)
            if match_count == 6:
                return
            # get next candidates from finding same matching count
            candidates = list(filter(lambda c: sum([c[i] == word[i] for i in range(6)]) == match_count and word != c, candidates))
                    



        
        