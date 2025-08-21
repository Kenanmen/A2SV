class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        r,c = len(grid),len(grid[0])
        def inbound(row,col):
            return 0 <= row < r and 0<=col < c and (row,col) not in visited
        def dfs(row,col):
            visited.add((row,col))
            for l,r in dir:
                newr,newc = l+row,r+col
                if inbound(newr,newc) and grid[newr][newc] =='1':
                    dfs(newr,newc)
        ans = 0
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited and grid[i][j] =='1':
                    ans +=1
                    dfs(i,j)
        return ans
