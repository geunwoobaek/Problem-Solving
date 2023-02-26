# only using 5words 0,1,6,8,9
# 0 -> 0, 1 -> 1, 6 -> 9, 8 -> 8, 9 -> 6
# 여러 자리수
# abc => reverse(cba)
# 0,1,6,8,9 => 10,16,18,19
# n< 10^9
# 168 2*5^2 +
# 5^9까지만 사용가능
class Solution:
    def confusingNumberII(self, n: int) -> int:
        digits = ["0", "1", "6", "8", "9"]
        reverseMap = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        def getNum(current_pointer):
            word = []
            while current_pointer >= 5:
                current_pointer, digit = divmod(current_pointer, 5)
                word.append(digits[digit])
            word.append(digits[current_pointer])
            return int(''.join(word)[::-1])

        def checkReverseIsSame(num):
            currNumStr = str(num)
            reverseStr = ''.join([reverseMap[c] for c in currNumStr[::-1]])
            return currNumStr == reverseStr

        res = 0
        curr_pointer = 0
        while True:
            curr_pointer += 1
            curr_num = getNum(curr_pointer)

            if curr_num > n:
                break

            if checkReverseIsSame(curr_num):
                continue
            res += 1
        return res
