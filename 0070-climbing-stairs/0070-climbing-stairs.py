class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 3:
            return n
        else:
            first = 1
            second = 2
            for i in range(3,n+1):
                third = first + second
                first = second
                second = third
            return second
        
        