class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        row,col = len(grid), len(grid[0])
        def inbound(r,c):
            return 0 <= r< row and 0 <= c < col
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans +=4
                    for l,r in dir:
                        newr,newc = l + i,r + j
                        if inbound(newr,newc):
                            if grid[newr][newc] == 1:
                                ans -=1
        return ans