import unittest
import Island as IslandClass

class TestNumIslands(unittest.TestCase):
  island = IslandClass.Island()

  # Test an empty grid
  def test_empty_grid(self):
    grid = []
    self.assertEqual(self.island.numIslands(grid), 0)
  
  # Test grid with single island
  def test_single_island(self):
    grid = [[1]]
    self.assertEqual(self.island.numIslands(grid), 1)

  # Test grid with multiple islands
  def test_multiple_islands(self):
    grid = [
      [1, 0, 1],
      [0, 1, 0],
      [1, 0, 1]
    ]
    self.assertEqual(self.island.numIslands(grid), 1)
  
  # Test grid with no islands
  def test_no_islands(self):
    grid = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
    self.assertEqual(self.island.numIslands(grid), 0)

  # Test grid with all cells set to 1
  def test_all_ones(self):
    grid = [
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]
    ]
    self.assertEqual(self.island.numIslands(grid), 1)

  # Test grid with a single row
  def test_single_row(self):
    grid = [
      [1, 1, 1]
    ]
    self.assertEqual(self.island.numIslands(grid), 1)

  # Test grid with a single column
  def test_single_column(self):
    grid = [
      [1],
      [1],
      [1]
    ]
    self.assertEqual(self.island.numIslands(grid), 1)
  
  # Test grid with islands connected diagonally
  def test_diagonal_islands(self):
    grid = [
      [1, 0, 0, 0, 1],
      [0, 1, 0, 1, 0],
      [0, 0, 1, 0, 1],
      [1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0]
    ]
    self.assertEqual(self.island.numIslands(grid), 2)
  
  # Test a mixed grid
  def test_mixed_grid(self):
    grid = [
      [1, 1, 0, 0, 1],
      [0, 1, 1, 0, 0],
      [0, 0, 0, 1, 1],
      [1, 0, 1, 0, 1],
      [1, 0, 1, 1, 1]
    ]
    self.assertEqual(self.island.numIslands(grid), 3)

  # Test grid with islands that are adjacent horizontally, vertically and diagonally
  def test_adjacent_islands(self):
    grid = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0],
      [1, 1, 1, 0, 0, 0, 1, 0, 0],
      [1, 1, 0, 0, 0, 1, 1, 1, 0],
      [0, 0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 1, 0, 0]
    ]
    self.assertEqual(self.island.numIslands(grid), 4)

  # Test single island surrounded by water
  def test_island_surrounded_by_water(self):
    grid = [
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,1,1,1,0],
      [0,0,0,0,0]
    ]
    self.assertEqual(self.island.numIslands(grid), 1)

if __name__ == "__main__":
  unittest.main()