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
        # Get the neighbors of the cell
        neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) 
             if 0 <= x < height and 0 <= y < width and (x, y) != (i, j) and grid[x][y] is None]
        
        # Generate clauses for exactly the number of traps
        for subset in combinations(neighbors, grid[i][j]):
          clause = [(neighbor[0]*width + neighbor[1] + 1) for neighbor in subset]
          cnf.append(clause)

  # Remove duplicate clauses
  cnf = [list(x) for x in set(tuple(x) for x in cnf)]

  return cnf


def solve(cnf, grid):
    height = len(grid)
    width = len(grid[0])
    solver = Glucose3()
    for clause in cnf:
        solver.add_clause(clause)

    if solver.solve():
      model = solver.get_model()
      for i in range(height):
        for j in range(width):
          if grid[i][j] is None:
            check = False
            for k in range(1, height*width+1):
              if k in model and k == i*width + j + 1:
                  grid[i][j] = 'G'
                  check = True
                  break
                
            if not check:
              grid[i][j] = 'T'
                        
      print("Output:")
      print_grid(grid)
    else:
      print("No solution found")

    return None

grid = [[3, None, 2, None],
        [None, None, 2, None],
        [None, 3, 1, None]]

cnf = generate_cnf(grid)
print(cnf)
solve(cnf, grid)