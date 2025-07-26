class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        l,r = 0, n//2
        while l < r:
            cur = s[l:r]
            if s.count(cur) * (r-l) == n:
                return True
            else:
                r -=1
        return False
        

        