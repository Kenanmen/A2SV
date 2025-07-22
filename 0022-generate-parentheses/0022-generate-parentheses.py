class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def rec(path,open,close):
            if close==n and open == n:
                res.append("".join(path))
                return
            if open< n:
                
                path.append('(')
                rec(path, open+1, close)
                path.pop()

            if close < open:
                path.append(')')
                rec(path, open, close+1)
                path.pop()

            
               
        rec([],0,0)
        return res



        