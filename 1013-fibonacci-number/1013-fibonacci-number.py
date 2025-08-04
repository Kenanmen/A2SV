class Solution:
    def fib(self, num: int) -> int:
        mem = defaultdict(int)
        def fibo(n):
            if n == 0 or n == 1:
                return n
            if  not mem[n]:
                mem[n] = fibo(n-1) + fibo(n-2)
            return mem[n]
        return fibo(num)

        
        
     
        