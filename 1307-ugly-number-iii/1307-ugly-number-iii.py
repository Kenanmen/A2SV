class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l,r = 1,min(a,b,c)*n
        def check(mid):
            num = mid// a + mid // b + mid // c - mid // math.lcm(a,b) - mid // math.lcm(b,c)- mid // math.lcm(a, c) + mid //(math.lcm(a,b,c))
            return num < n
        while l <= r:
            mid =(l+r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l
        
         
       


        