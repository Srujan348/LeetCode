class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        import bisect


        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the index of the first element >= (x - d)
            idx = bisect.bisect_left(arr2, x - d)
            
            # If the element at this index is <= (x + d), it falls in the forbidden range
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
                
            distance_value += 1
            
        return distance_value