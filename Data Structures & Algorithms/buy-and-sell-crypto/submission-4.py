from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        purc = float('inf')
        for x in prices:
            purc = min(purc,x)
            max_p = max(max_p,x-purc)

        return max_p
            

        