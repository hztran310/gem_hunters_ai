from itertools import combinations
from pysat.solvers import Glucose3
import time

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
    return new_grid
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

def DPLL(cnf, model={}):
    # If the CNF is empty, return True
    if not cnf:
        return model

    # If there is an empty clause, return False
    if [] in cnf:
        return False

    # Choose a literal
    literal = choose_literal(cnf)

    # Try assigning the literal to True
    new_model = model.copy()
    new_model[literal] = True
    new_cnf = assign(cnf, literal, True)
    result = DPLL(new_cnf, new_model)
    if result is not False:
        return result

    # Try assigning the literal to False
    new_model = model.copy()
    new_model[literal] = False
    new_cnf = assign(cnf, literal, False)
    result = DPLL(new_cnf, new_model)
    if result is not False:
        return result

    return False

def choose_literal(cnf):
    # Choose the first literal in the first clause
    return abs(cnf[0][0])

def assign(cnf, literal, value):
    # If value is True, remove all clauses containing literal
    # If value is False, remove literal from all clauses
    if value:
        return [[l for l in clause if l != -literal] for clause in cnf if literal not in clause]
    else:
        return [[l for l in clause if l != literal] for clause in cnf if -literal not in clause]

def check_grid(grid):
  height = len(grid)
  width = len(grid[0])
  for i in range(height):
    for j in range(width):
      if isinstance(grid[i][j], int):
        neighbors = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) 
                     if 0 <= x < height and 0 <= y < width and (x, y) != (i, j)]
        count = sum(1 for x, y in neighbors if grid[x][y] == 'T')
        if count != grid[i][j]:
          return False
  return True

import itertools

def brute_force(grid):
  height = len(grid)
  width = len(grid[0])
  unknown_cells = [(i, j) for i in range(height) for j in range(width) if grid[i][j] is None]
  for combination in itertools.product(['G', 'T'], repeat=len(unknown_cells)):
    new_grid = [row.copy() for row in grid]
    for (i, j), value in zip(unknown_cells, combination):
      new_grid[i][j] = value
    if check_grid(new_grid):
      return new_grid
  return None

def backtracking(grid, i=0, j=0):
  height = len(grid)
  width = len(grid[0])

  # Base case: if reached end of grid, return the grid
  if i == height:
    return grid if check_grid(grid) else None

  # Calculate next position to explore
  next_i, next_j = (i, j + 1) if j + 1 < width else (i + 1, 0)

  # If cell is not None, move to the next cell
  if grid[i][j] is not None:
    return backtracking(grid, next_i, next_j)

  # Try placing 'G' and 'T' and backtrack if necessary
  for value in ['G', 'T']:
    grid[i][j] = value
    result = backtracking(grid, next_i, next_j)
    if result is not None:
      return result
  grid[i][j] = None  # Backtrack
  return None

if __name__ == "__main__":
    grid = read_file('Test case 20x20.txt')
    cnf = generate_cnf(grid)
    # Solve using Pysat
    print("\nSolve with Pysat:\n")
    print("Input: ")
    print_grid(grid)
    start = time.time()
    output = solve(cnf, grid)
    end = time.time()
    if output is not None:
      print("Pysat solve time:", end - start)
      print("Output:")
      print_grid(output)
    
    # Solve using DPLL
    print("\nSolve with DPLL:\n")
    start = time.time()
    model = DPLL(cnf)
    end = time.time()
    if model is False:
        print("The CNF is unsatisfiable")
    else:
        print("DPLL time:", end - start)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is None:
                    pos = i*len(grid[0]) + j + 1
                    if pos in model and model[pos]:
                        grid[i][j] = 'T'
                    else:
                        grid[i][j] = 'G'
        print("Output:")
        print_grid(grid)

    # Solve using brute force
    print("\nSolve with Brute-force:\n")
    start = time.time()
    brute_force_result = brute_force(grid)
    end = time.time()
    print('Brute force time:', end - start)
    print("Brute force result:")
    print_grid(brute_force_result)
    
    # Solve using backtracking
    print("\nSolve with Backtracking:\n")
    start = time.time()
    backtracking_result = backtracking(grid)
    end = time.time()
    print('Backtracking time:', end - start)
    print("Backtracking result:")
    print_grid(backtracking_result)