# check sx, sy -> tx, ty
# bruteforce하게 보면, sx -> tx도달, 
# dp[sx][sy] = dp[sx+sy][sx], dp[sx][sx+sy] bruteforce방식

import sys
from functools import cache
sys.setrecursionlimit(10**6)
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        @cache
        def dfs(tx, ty):
            if sx == tx and sy == ty:
                return True
            if sx > tx or sy > ty:
                return False
            if tx == ty:
                return False
            
            if tx >= ty and ty > sy:
                num = tx // ty
                num -= num*ty == tx
                return dfs(tx - num*ty, ty)
            
            if ty < tx and ty == sy:
                k = (tx -sx) // ty
                return tx - k*ty == sx
            
            if tx < ty and tx > sx:
                num = ty // tx
                num -= num*tx == ty
                return dfs(tx, ty-num*tx)

            if tx < ty and tx == sx:
                k = (ty -sy) // tx
                return ty - k*tx == sy



        return dfs(tx, ty)