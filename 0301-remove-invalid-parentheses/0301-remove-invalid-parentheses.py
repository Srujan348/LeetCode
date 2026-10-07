class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        # Start with the original string in our current level
        level = {s}
        
        while True:
            # Filter the current level for only valid strings
            valid = list(filter(is_valid, level))
            
            # If we found any valid strings, this is the minimum removal level
            if valid:
                return valid
            
            # Otherwise, generate the next level by removing one parenthesis
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in "()":
                        next_level.add(string[:i] + string[i+1:])
            
            level = next_level