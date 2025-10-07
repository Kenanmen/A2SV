class Solution:
    def isUgly(self, n: int) -> bool:
        
        a = 2
        while n>=1 and a <=5:
            while n%a==0:
                n = n//a
                
            a +=1
        if n != 1:
            return False
        return True
       


        