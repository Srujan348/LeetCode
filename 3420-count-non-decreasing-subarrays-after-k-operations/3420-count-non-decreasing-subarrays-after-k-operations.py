class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        st = []  # Stack of tuples: (start_idx, end_idx, max_val)
        ans = 0
        j = n - 1
        cost = 0
        
        for i in range(n - 1, -1, -1):
            val = nums[i]
            end_idx = i
            
            # Pop blocks smaller than or equal to current value
            while st and st[-1][2] <= val:
                b_idx, b_end, b_val = st.pop()
                overlap_start = b_idx
                overlap_end = min(j, b_end)
                
                # Add the penalty cost difference for the active window
                if overlap_start <= overlap_end:
                    cost += (val - b_val) * (overlap_end - overlap_start + 1)
                end_idx = b_end
                
            # Push the newly merged block
            st.append((i, end_idx, val))
            
            # Shrink window from the right if cost exceeds budget k
            while cost > k:
                left, right = 0, len(st) - 1
                m_j = 0
                
                # Binary search to find the block containing j
                while left <= right:
                    mid = (left + right) // 2
                    b_idx, b_end, b_val = st[mid]
                    
                    if b_idx <= j <= b_end:
                        m_j = b_val
                        break
                    elif j < b_idx:
                        left = mid + 1
                    else:
                        right = mid - 1
                        
                # Subtract the exact cost contribution of element j
                cost -= (m_j - nums[j])
                j -= 1
                
            ans += (j - i + 1)
            
        return ans