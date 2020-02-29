from collections import defaultdict

class Solution:

  def DFS(self, grid, i, j, idx):
    # print("DFS", i, j, idx)
    key = f"{i},{j}"
    self.visited[key] = idx
    for d in [(1,0), (-1,0), (0,1), (0,-1)]:
      di = d[0]
      dj = d[1]
      i2 = i + di
      j2 = j + dj
      if i2 < 0 or i2 >= self.height:
        continue
      if j2 < 0 or j2 >= self.width:
        continue
      key = f"{i2},{j2}"
      if self.visited[key] == 0 and grid[i2][j2] == "1":
        self.DFS(grid, i2, j2, idx)

  def numIslands(self, grid: List[List[str]]) -> int:
    # MAX = 1000
    self.visited = defaultdict(int)
    self.height = len(grid)
    if len(grid) == 0:
      self.width = 0
    else:
      self.width = len(grid[0])
    idx = 0
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        key = f"{i},{j}"
        # print("check", i, j, grid[i][j])
        if self.visited[key] == 0 and grid[i][j] == "1":
          # print(self.visited)
          idx += 1
          self.DFS(grid, i, j, idx)

    # print(idx)
    return idx
