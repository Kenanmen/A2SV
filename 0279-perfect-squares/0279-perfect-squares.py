class Solution:
    def numSquares(self, n: int) -> int:
        squares = [1]
        i = 2
        while i * i <= n:
            squares.append(i*i)
            i +=1
        dp = [i for i in range(n+1)]
        for sq in squares:
            for i in range(sq,n+1):
                dp[i] = min(dp[i-sq]+ 1, dp[i])
        return dp[n]
                

        
        