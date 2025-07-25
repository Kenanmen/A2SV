class Solution:
    def fib(self, num: int) -> int:
        
        if num <= 1:
            return num
        res = self.fib(num-1) + self.fib(num-2)
        return res
     
        