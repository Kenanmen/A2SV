class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        ans = 0
        ones = 0
        i = 0
        while i < len(s):
            if s[i]== '0':
                
                while i < len(s) and s[i] == '0':
                    
                    i +=1
                ans += ones
                
            else:
                ones +=1
                i+=1
        return ans
