class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1] *(n+1)
        def rec(i):
            if i <=3:
                mem[i] = i
                return mem[i]
            if mem[i] == -1:
                mem[i] = rec(i-1) + rec(i-2)
            return mem[i]
        return rec(n)
        