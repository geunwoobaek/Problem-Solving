class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        two_count = collections.Counter(colsum).get(2, 0)
        if two_count > lower or two_count > upper:
            return []
        ## upper부터 채우기
        ## upper_sum = 0 => upper만큼
        upper_list = []
        lower_list = []
        upper_sum = 0
        for c in colsum:
            if c == 0:
                upper_list.append(0)
                lower_list.append(0)
            elif c == 2:
                upper_list.append(1)
                lower_list.append(1)
            elif c == 1 and upper_sum + two_count < upper:
                upper_sum += 1
                upper_list.append(1)
                lower_list.append(0)
            else:
                upper_list.append(0)
                lower_list.append(1)
        return [upper_list, lower_list]
