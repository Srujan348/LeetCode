class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
    
        n = len(nums)
        
        # Square all elements and sort them ascending
        squares = sorted(x * x for x in nums)
        
        # Subtract the smallest half, add the largest half
        # (n // 2) perfectly captures the floor of n/2
        return sum(squares[n // 2:]) - sum(squares[:n // 2])