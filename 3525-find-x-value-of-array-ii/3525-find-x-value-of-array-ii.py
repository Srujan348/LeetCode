from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_counts = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)
        
    def merge(self, left_prod, left_counts, right_prod, right_counts):
        k = self.k
        new_prod = (left_prod * right_prod) % k
        new_counts = list(left_counts)
        
        for i in range(k):
            if right_counts[i] > 0:
                new_rem = (left_prod * i) % k
                new_counts[new_rem] += right_counts[i]
                
        return new_prod, new_counts
        
    def build(self, nums, node, start, end):
        if start == end:
            val = nums[start] % self.k
            self.tree_prod[node] = val
            self.tree_counts[node][val] = 1
            return
            
        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        
        self.tree_prod[node], self.tree_counts[node] = self.merge(
            self.tree_prod[2 * node + 1], self.tree_counts[2 * node + 1],
            self.tree_prod[2 * node + 2], self.tree_counts[2 * node + 2]
        )
        
    def update(self, node, start, end, idx, val):
        if start == end:
            val_mod = val % self.k
            self.tree_prod[node] = val_mod
            self.tree_counts[node] = [0] * self.k
            self.tree_counts[node][val_mod] = 1
            return
            
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node + 1, start, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, end, idx, val)
            
        self.tree_prod[node], self.tree_counts[node] = self.merge(
            self.tree_prod[2 * node + 1], self.tree_counts[2 * node + 1],
            self.tree_prod[2 * node + 2], self.tree_counts[2 * node + 2]
        )
        
    def query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return self.tree_prod[node], self.tree_counts[node]
            
        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node + 1, start, mid, l, r)
        elif l > mid:
            return self.query(2 * node + 2, mid + 1, end, l, r)
        else:
            left_prod, left_counts = self.query(2 * node + 1, start, mid, l, r)
            right_prod, right_counts = self.query(2 * node + 2, mid + 1, end, l, r)
            return self.merge(left_prod, left_counts, right_prod, right_counts)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        if not nums or not queries:
            return []
            
        n = len(nums)
        seg_tree = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, xi in queries:
            # 1. Persistently update the value at idx
            seg_tree.update(0, 0, n - 1, idx, val)
            
            # 2. Query the valid subarray from start to the end of the array
            _, counts = seg_tree.query(0, 0, n - 1, start, n - 1)
            
            # 3. Append the count of prefixes that result in target modulo xi
            ans.append(counts[xi])
            
        return ans