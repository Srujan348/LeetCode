class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_count = 0
        equal_count = 0
        
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                equal_count += 1
                
        # Generate the indices starting at less_count, for equal_count elements
        return list(range(less_count, less_count + equal_count))