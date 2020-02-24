# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
# elapsed time : N/A (from solution text)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        coordForIslandNum = {}
        islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) in coordForIslandNum: continue
                if grid[i][j] == "1":
                    island = self.dfs(grid, (i, j))
                    for c in island:
                        coordForIslandNum[c] = islands
                    islands += 1
                    
        return islands        

    def dfs(self, grid, coord):
        result = [coord]
        grid[coord[0]][coord[1]] = 0
        adjs = self.adjacentIdx(grid, coord[0], coord[1])
        if len(adjs) > 0:
            for adj in adjs:
                result += self.dfs(grid, adj)
        return result
        
    def adjacentIdx(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        adjacentIdx = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        
        return list(filter(
            lambda c: self.isInbound(grid, c[0], c[1]) and grid[c[0]][c[1]] == "1", adjacentIdx))
    
    def isInbound(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])     
        
        return i>=0 and i<m and j>=0 and j<n
        
        

        
