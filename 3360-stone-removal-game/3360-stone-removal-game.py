class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        turns = 0
        while n >= stones:
            n -= stones
            stones -= 1
            turns += 1
        return turns % 2 == 1