class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Continue simulating until the string is small enough
        while len(s) > k:
            next_s = []
            
            # Step through the string in chunks of size k
            for i in range(0, len(s), k):
                chunk = s[i : i + k]
                # Sum the integer values of the characters in the chunk
                chunk_sum = sum(int(digit) for digit in chunk)
                next_s.append(str(chunk_sum))
                
            # Replace s with the newly formed string
            s = "".join(next_s)
            
        return s