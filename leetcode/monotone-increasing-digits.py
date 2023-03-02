# n 한자리 그대로 리턴
# n이 두자리일 경우 십의자리 그대로 사용하고 monontone 일경우 그대로 사용함
# 모노톤이 아닐경우 가장높은 자리수를 1 감소시키고 그 뒤의 모든 자리수를 9로 바꿈
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        n = list(str(n))
        i = 1
        while i < len(n) and n[i - 1] <= n[i]:
            i += 1
        if i < len(n):
            while i > 0 and n[i - 1] > n[i]:
                n[i - 1] = str(int(n[i - 1]) - 1)
                i -= 1
            n[i + 1:] = '9' * (len(n) - i - 1)
        return int(''.join(n))

