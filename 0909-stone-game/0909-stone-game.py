class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        mem = {}
        sums = sum(piles)
        def dp(turn,l,r):
            if l > r:
                
                return sums
            if (turn,l,r) not in mem:
                if turn == 1:
                    mem[(turn,l,r)] = min(dp(turn-1,l+1,r)- piles[l],dp(turn-1,l,r-1)-piles[r])
                else:
                    mem[(turn,l,r)] = max(dp(turn+1,l+1,r),dp(turn+1,l,r-1))
            return mem[(turn,l,r)]
        return sums - dp(0,0,len(piles)-1) >=0


        