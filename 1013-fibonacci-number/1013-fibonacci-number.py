class Solution:
    def fib(self, n: int) -> int:
        def fibo(num):
            if num <= 1:
                return num
            res = fibo(num-1) + fibo(num-2)
            return res
        return fibo(n)
        