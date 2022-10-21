# https://leetcode.com/problems/number-of-atoms/

# # Example 1:
# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.
# Input: formula = "H2O"
# Output: "H2O"
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# Example 2:

# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:

# Input: formula = "K4(ON(SO3)2)2" => 
# Output: "K4N2O14S4"
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

# K4(ON(SO3)2)2
# 괄호없애기
# 그다음 DICT로 나타내기 KEY별로 정렬하기
# 고고
# K4
# K4(ON(SO3)2 숫자 앞이 닫는괄호일경우 숫자에 곱해주기 
# 리스트로? ㅇㅋㅇㅋ
# 리스트안은 리스트로 ㅇㅋㅇㅋ 만약 괄호나오면 튜플로 ㅇㅋㅇㅋ?
# STACK
# K,4,(,O,1,N,1,(,S,1,O,3,),2 -> 괄호 2개지우고 나머지 숫자들 곱해주기 이때 TimeComplexity는? O(N)
# K,4,(,O,1,N,1,S,2,O,6,)
# [(num,alphabet), 이게 더좋음 ㅇㅇ



from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        new_formula = []
        list_formula = []
        for idx, i in enumerate(formula):
            if i.isalpha() and i.isupper():
                list_formula.append(i)
            elif i.isalpha() and i.islower():
                list_formula[-1] += i
            elif i.isdigit() and list_formula[-1].isdigit():
                list_formula[-1] += i
            else:
                list_formula.append(i)
            if list_formula[-1] == ")" and (
                idx == len(formula)-1 or not formula[idx+1].isdigit()
            ):
                list_formula.append("1")
        
        for cur in list_formula:
            if cur.isalpha():
                new_formula.append([1, cur])
            elif cur.isdigit() and new_formula[-1] == ')':
                # check 괄호안 처리
                # ')' 지우기
                new_formula.pop() 
                cursor = len(new_formula) - 1
                while new_formula[cursor] != '(':
                    new_formula[cursor][0]*= int(cur)
                    cursor -= 1
                # '(' 지우기
                new_formula.pop(cursor)
            elif cur.isdigit():
                new_formula[-1][0]*= int(cur)
            else:
                new_formula.append(cur)
        
        # new_formula to count dict
        count_dict = Counter()
        for num, alphabet in new_formula:
            count_dict[alphabet]+=num
        return ''.join([alphabet+str(num) if num>1 else alphabet for alphabet, num in sorted(count_dict.items(), key=lambda x: x[0])])

print(Solution().countOfAtoms("(H)"))
print(Solution().countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4")
print(Solution().countOfAtoms("Mg(OH)2") == "H2MgO2")
print(Solution().countOfAtoms("H2O") == "H2O")
    