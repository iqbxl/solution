import argparse

class Island:
  """
  Island class for counting number of islands
  """
  def parseArgs(self) -> str:
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add an input file argument
    parser.add_argument("input", help="input file")

    # Parse the command line arguments
    args = parser.parse_args()

    # Return the input file name
    return args.input

  def numIslands(self, grid: list[list[int]]) -> int:
    if not grid:
      return 0
      
    rows = len(grid)
    cols = len(grid[0])

    # Recursively calls itself and marks all adjacent cells as visited
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

    # Visit each cell in the grid once (Time complexity: O(m * n))
    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          count += 1
          dfs(i, j)
    return count

if __name__ == "__main__":

  # Create new island object
  island = Island()
  input_file = island.parseArgs()

  try:
    with open(input_file, 'r') as file:
      grid = [[int(c) for c in line.strip()] for line in file]
    print(island.numIslands(grid))
  except FileNotFoundError:
    print("Error: input file does not exist")
    exit(1)