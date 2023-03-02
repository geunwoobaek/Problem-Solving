class Solution:
    def minimumDeletions(self, s: str) -> int:
        # s는 a와 b로만 이루어진 string 이다. s의 길이는 1 이상 10^5 이하이다.
        # balanced string 은 모든 i < j 에 대해서 i, j에 대하여 s[i] = 'a' and s[j] = 'b' 여야 한다.
        # balanced string을 만들기 위한 최소한의 삭제 횟수를 구하라
        a, b = 0, 0
        for char in s:
            if char == 'a':
                a += 1
            else:
                b += 1
        return min(a, b)




print(Solution().minimumDeletions("aababbab")) # 2
