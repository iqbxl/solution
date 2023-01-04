def numIslands(grid: list[list[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])

  def dfs(i, j):
    if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
      return
    
    grid[i][j] = 0
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i + 1, j + 1)
    dfs(i + 1, j - 1)
    dfs(i - 1, j + 1)
    dfs(i - 1, j - 1)

  count = 0
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        count += 1
        dfs(i, j)
  return count

if __name__ == "__main__":
  with open('islands.txt', 'r') as file:
    grid = [[int(c) for c in line.strip()] for line in file]
  print(numIslands(grid))