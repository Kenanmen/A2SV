class Solution:
    def climbStairs(self, n: int) -> int:
        mem = defaultdict(int)
        def func(i):
            if i <= 3:
                return i
            if not mem[i]:
                mem[i] = func(i-1) + func(i-2)
            return mem[i]
        return func(n)
            
       