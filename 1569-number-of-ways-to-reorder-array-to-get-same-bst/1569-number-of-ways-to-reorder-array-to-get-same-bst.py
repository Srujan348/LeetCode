import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            # Divide into left and right subtrees based on BST property
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Calculate combinations to interleave left and right arrays
            combinations = math.comb(len(left) + len(right), len(left))
            
            # Conquer recursively
            left_ways = ways(left)
            right_ways = ways(right)
            
            return (combinations * left_ways * right_ways) % MOD
            
        # Subtract 1 to exclude the original array configuration
        return (ways(nums) - 1) % MOD