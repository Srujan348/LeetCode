class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Case A: Buy separately
        a = need1 * cost1 + need2 * cost2
        
        # Case B: Buy only combined items until the maximum need is met
        b = max(need1, need2) * costBoth
        
        # Case C: Buy combined items to cover the overlap, then fill the rest separately
        mn = min(need1, need2)
        c = mn * costBoth + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(a, b, c)