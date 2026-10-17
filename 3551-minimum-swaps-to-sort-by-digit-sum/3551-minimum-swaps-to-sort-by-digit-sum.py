class Solution:
    def minSwaps(self, nums: List[int]) -> int:
    
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        # Step 1 & 2: Create the target sorted array
        # We sort by (digit_sum, value)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Step 3: Map values to their target indices
        # Since constraints say distinct positive integers, this is safe
        target_idx = {val: i for i, val in enumerate(target)}

        # Step 4: Cycle detection
        n = len(nums)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_idx[nums[i]] == i:
                continue

            # Found a new cycle
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = target_idx[nums[j]]
                cycle_len += 1

            if cycle_len > 0:
                swaps += (cycle_len - 1)

        return swaps