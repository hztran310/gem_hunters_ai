from itertools import combinations
from pysat.solvers import Glucose3
import time

grid_4 = [[3, None, 2, None],
          [None, None, 2, None],
          [None, 3, 1, None]]

grid_5 = [[None, 3, None, 3, 1],
          [2, None, None, 4, None],
          [None, None, 1, None, None],
          [None, 2, None, 2, None],
          [1, None, 1, 1, None]]

grid_9 = [[None, None, 2, None, 2, None, 1, 2, None],
          [None, 4, None, 3, None, None, 3, None, 4],
          [2, None, None, 4, None, 5, None, None, None],
          [None, None, 4, None, None, None, None, 6, None],
          [None, None, 2, None, None, 5, None, None, None],
          [3, None, None, None, None, 2, None, 4, 3],
          [1, None, None, None, 3, None, None, None, None],
          [None, 4, 6, None, None, None, 3, None, 2],
          [None, None, None, None, 3, 2, None, 1, None]]

grid_11 = [[None, None, 2, None, None, None, None, 1, None, None, None],
          [2, 2, None, None, 4, None, None, 3, 3, None, 3],
          [None, None, 5, 4, None, 3, None, None, None, 2, None],
          [2, None, None, None, None, None, 2, 2, None, 1, None],
          [1, None, 5, 5, None, None, 2, None, 1, None, 2],
          [2, 3, None, None, 2, None, None, None, 2, None, None],
          [None, None, 5, None, None, 3, 2, None, None, 4, None],
          [None, 4, None, None, None, None, None, 2, None, None, None],
          [None, 3, None, 5, 3, 2, None, None, None, None, 4],
          [3, None, None, None, None, 2, None, None, 4, None, None],
          [None, None, 3, None, 1, 2, None, 3, None, None, 3]]

grid_15 = [[1, None, 1, 2, None, None, 2, None, 1, None, None, 3, None, None, 2],
          [None, None, 2, None, None, 3, None, 4, 3, 2, None, None, None, 3 , None],
          [None, 3, None, None, 3, 3, None, None, None, 1, 2, None, 4, None, 1],
          [2, None, None, 5, None, 2, 2, None, 4, None, 2, None, None, 3, 2],
          [1, None, 4, None, None, None, 2, 2, 3, None, None, None, 3 , None, None],
          [None, 1, None, None, 6, None, None, 2, None, 3, None, 2, 3, 4, 3],
          [None, 2, 3, None, None, None, 5, None, 2, 3, 2, None, None, None, None],
          [3, None, None, 2, None, None, None, 3, 2, None, None, None, 4, None, None],
          [None, None, 4, 3, 3, 3, None, None, None, None, 2, 3, None, None, 2],
          [3, 4, None, None, None, 2, 2, None, 3, 3, 2, None, None, 3, None],
          [2, None, None, 4, None, None, None, 4, None, None, None, None, 2, 2, 1],
          [None, 4, 3, 3, None, 2, None, None, None, None, 3, 2, None, None, None],
          [None, 2, None, None, 3, None, None, None, 7, None, None, 2, 2, 3, None],
          [None, None, 3, 3, 3, None, 3, None, None, None, 3, 3, None, None, None],
          [1, None, None, 2, None, None, None, 2, None, 2, 2, None, None, 3, None]]

grid_20 = [
          [None, None, 3, None, 2, 2, None, None, 2, None, 2, None, None, None, 2, 1, None, None, None, 1],
          [2, None, None, 3, None, None, None, 3, None, None, 2, 2, 4, None, None, 2, None, 3, None, 2],
          [2, 3, None, None, 4, 4, 5, None, None, 3, None, None, None, 4, None, 3, 1, None, 3, None],
          [None, None, 4, None, None, None, 5, None, 3, None, None, None, 3, None, None, None, None, 3, None, None],
          [None, 3, None, None, 5, None, None, None, None, 3, 4, 3, None, None, 3, None, 4, None, None, 3],
          [1, 3, 3, None, None, None, 4, 4, None, None, None, None, 1, 2, None, None, None, 4, None, 1],
          [None, 2, None, 2, None, 3, None, None, None, 4, None, 4, 3, None, None, 3, None, None, 2, 1],
          [None, None, 2, 3, 3, None, 3, None, 3, 3, None, None, None, None, 5, None, None, 2, None, None],
          [None, 2, 2, None, None, None, None, 2, None, None, 3, 3, None, 3, None, None, 4, None, 3, 1],
          [1, None, None, 5, None, 4, 3, None, None, 2, None, None, 2, 2, None, 2, None, None, None, 2],
          [2, 3, None, None, None, 4, None, None, None, None, 3, None, None, None, 1, 1, 3, None, None, None],
          [None, None, 5, None, None, None, None, 4, 3, None, None, 3, None, None, None, None, 3, 3, None, None],
          [1, None, None, None, 3, 3, None, 2, None, None, None, None, 2, 2, None, None, None, None, 2, 1],
          [1, 3, None, 5, 4, None, 2, 2, None, 4, 4, None, None, 3, None, 2, None, None, None, 3],
          [2, None, None, None, None, None, None, 2, 2, None, None, None, 5, None, 3, 2, 3, None, None, None],
          [None, None, 4, None, None, None, 2, None, None, None, 4, 3, None, None, None, None, None, 4, 4, None],
          [2, 3, None, None, 4, 4, None, None, 3, None, None, None, 2, None, None, None, None, None, 3, 2],
          [None, 3, None, 3, None, None, None, 2, None, None, 4, 2, 2, 2, None, None, None, 4, None, None],
          [None, None, 3, None, None, None, 5, None, 3, 2, None, None, 2, None, 3, 3, 3, None, 5, None],
          [None, 1, 2, None, 2, None, None, 3, None, None, None, 1, 2, 1, None, None, None, None, 3, None]
          ]

def print_grid(grid):
  for row in grid:
      print(', '.join(str(cell) if cell is not None else '_' for cell in row))

def generate_cnf(grid):
  height = len(grid)
  width = len(grid[0])
  cnf = []

  for i in range(height):from itertools import combinations
from pysat.solvers import Glucose3

def print_grid(grid):
  for row in grid:
      print(', '.join(str(cell) if cell is not None else '_' for cell in row))

def generate_cnf(grid):
  height = len(grid)
  width = len(grid[0])
  cnf = []

  for i in range(height):
    for j in range(width):
      if isinstance(grid[i][j], int):
        pos = i*width + j + 1
        neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) 
               if 0 <= x < height and 0 <= y < width and (x, y) != (i, j)]
        unknown_neighbors = [(x, y) for x, y in neighbors if grid[x][y] is None]
        n = len(unknown_neighbors)
        k = grid[i][j] - len([1 for x, y in neighbors if grid[x][y] == 'T'])

        # U(k, n): for any k+1 squares out of n, at least one is not a mine
        for subset in combinations(unknown_neighbors, k+1):
          clause = [-((x*width + y + 1)) for x, y in subset]
          cnf.append(clause)

        # L(k, n): for any n-k+1 squares out of n, at least one is a mine
        for subset in combinations(unknown_neighbors, n-k+1):
          clause = [(x*width + y + 1) for x, y in subset]
          cnf.append(clause)

  return cnf


def solve(cnf, grid):
  height = len(grid)
  width = len(grid[0])
  solver = Glucose3()
  for clause in cnf:
    solver.add_clause(clause)

  if solver.solve():
    print("The CNF is satisfiable. Here are all possible models:")
    model = solver.get_model()
    new_grid = [row.copy() for row in grid]  # Create a copy of the grid for each model
    for i in range(height):
      for j in range(width):
        if new_grid[i][j] is None:
          pos = i*width + j + 1
          if -pos in model:
            new_grid[i][j] = 'G'
          elif pos in model:
            new_grid[i][j] = 'T'
    print("Output:")
    print_grid(new_grid)
  else:
    print("The CNF is not satisfiable.")


if __name__ == "__main__":
  # This code will only run if you do `python Test.py`, not when you import Test in another file
  grid = grid_4
  print("Input:")
  print_grid(grid)
  cnf = generate_cnf(grid)
  print("CNF:", cnf)
  solve(cnf, grid)
    

