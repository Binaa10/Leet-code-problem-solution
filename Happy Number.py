class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = sum(int(x) ** 2 for x in str(n))
        return n == 1
