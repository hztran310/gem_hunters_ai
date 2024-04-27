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
                  clause = [neighbor[0]*width + neighbor[1] + 1 for neighbor in subset]
                  cnf.append(clause)
              
              # Generate clauses for more than the number of traps
              for subset in combinations(neighbors, grid[i][j] + 1):
                  clause = [-1*(neighbor[0]*width + neighbor[1] + 1) for neighbor in subset]
                  cnf.append(clause)

  return cnf


def solve(cnf, grid):
    height = len(grid)
    width = len(grid[0])
    solver = Glucose3()
    for clause in cnf:
        solver.add_clause(clause)

    if solver.solve():
        model = solver.get_model()
        solution = [['T' if i*width + j + 1 in model else 'G' for j in range(width)] for i in range(height)]
        print("Input:")
        print_grid(grid)
        print("Output:")
        print_grid(solution)
    else:
        print("No solution found")

    return None

grid = [[3, None, 2, None],
        [None, None, 2, None],
        [None, 3, 1, None]]

cnf = generate_cnf(grid)
print(cnf)
solve(cnf, grid)