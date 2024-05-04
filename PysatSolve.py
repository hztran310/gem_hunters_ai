from itertools import combinations
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

def read_file(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = []
                for val in line.strip().split(','):
                    if val.strip().lower() == 'none':
                        row.append(None)
                    else:
                        try:
                            row.append(int(val))
                        except ValueError:
                            row.append(val.strip())
                grid.append(row)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist. Please check the file path and try again.")
        return None
    return grid

if __name__ == "__main__":
  # This code will only run if you do `python PysatSolve.py`, not when you import PysatSolve in another file
  grid = read_file('Test case 20x20.txt')
  print("Input:")
  print_grid(grid)
  cnf = generate_cnf(grid)
  print("CNF:", cnf)
  solve(cnf, grid)
    

