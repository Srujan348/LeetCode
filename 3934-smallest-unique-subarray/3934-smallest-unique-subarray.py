from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base1, mod1 = 100003, 1000000007
        base2, mod2 = 100019, 1000000009

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i in range(n):
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + nums[i]) % mod1
            pref2[i + 1] = (pref2[i] * base2 + nums[i]) % mod2

        def has_unique(length: int) -> bool:
            p1, p2 = pow1[length], pow2[length]
            counts = Counter()
            for i in range(n - length + 1):
                h1 = (pref1[i + length] - pref1[i] * p1) % mod1
                h2 = (pref2[i + length] - pref2[i] * p2) % mod2
                key = (h1 << 32) | h2
                counts[key] += 1
            return any(v == 1 for v in counts.values())

        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if has_unique(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans