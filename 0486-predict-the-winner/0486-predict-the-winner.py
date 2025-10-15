class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        mem = {}
        def dp(turn,l,r):
            if l > r:
                return (0,0)
           

            if (turn,l,r) not in mem:
                if turn == 0:
                    a,b = dp(turn+1,l+1,r)
                    c,d = dp(turn+1,l,r-1)
                    if (a+nums[l])-b > c+nums[r]-d:
                        mem[(turn,l,r)] = (a+nums[l],b)
                    else:
                        mem[(turn,l,r)] = (c+nums[r],d)
                else:
                    a,b = dp(turn-1,l+1,r)
                    c,d = dp(turn-1,l,r-1)
                    if b+nums[l]-a > d+nums[r]-c:
                        mem[(turn,l,r)] = (a,b+nums[l])
                    else:
                        mem[(turn,l,r)] = (c,d+nums[r])
            return mem[(turn,l,r)]
        a,b = dp(0,0,len(nums)-1)
        return a >= b



                
            
            

           