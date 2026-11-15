class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Represents the initial prefix sum of 0
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                # Odd current sum pairs with all previous even sums
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # Even current sum pairs with all previous odd sums
                result = (result + odd_count) % MOD
                even_count += 1
                
        return result