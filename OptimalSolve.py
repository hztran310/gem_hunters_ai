from Test import generate_cnf, print_grid
import time

grid_05 = [[3, None, 2, None],
          [None, None, 2, None],
          [None, 3, 1, None]]

grid_01 = [[None, 3, None, 3, 1],
          [2, None, None, 4, None],
          [None, None, 1, None, None],
          [None, 2, None, 2, None],
          [1, None, 1, 1, None]]

grid_02 = [[None, None, 2, None, 2, None, 1, 2, None],
          [None, 4, None, 3, None, None, 3, None, 4],
          [2, None, None, 4, None, 5, None, None, None],
          [None, None, 4, None, None, None, None, 6, None],
          [None, None, 2, None, None, 5, None, None, None],
          [3, None, None, None, None, 2, None, 4, 3],
          [1, None, None, None, 3, None, None, None, None],
          [None, 4, 6, None, None, None, 3, None, 2],
          [None, None, None, None, 3, 2, None, 1, None]]

grid_03 = [[None, None, 2, None, None, None, None, 1, None, None, None],
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

grid_04 = [[1, None, 1, 2, None, None, 2, None, 1, None, None, 3, None, None, 2],
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

grid = [
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
    return grid if is_valid_placement(grid) else None

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

def is_valid_placement(grid):
  height = len(grid)
  width = len(grid[0])
  for i in range(height):
    for j in range(width):
      if isinstance(grid[i][j], int):
        neighbors = [(x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                     if 0 <= x < height and 0 <= y < width and (x, y) != (i, j)]
        count = sum(1 for a, b in neighbors if grid[a][b] == 'T')
        if count != grid[i][j]:
          return False
  return True

if __name__ == "__main__":
    cnf = generate_cnf(grid)
    start = time.time()
    model = DPLL(cnf)
    end = time.time()
    print("Input: ")
    print_grid(grid)
    if model is False:
        print("The CNF is unsatisfiable")
    else:
        print("DPLL time:", end - start)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is None:
                    pos = i*len(grid[0]) + j + 1
                    if model[pos]:
                        grid[i][j] = 'T'
                    else:
                        grid[i][j] = 'G'
        print("Output:")
        print_grid(grid)

    # Solve using brute force
    start = time.time()
    brute_force_result = brute_force(grid)
    end = time.time()
    print('Brute force time:', end - start)
    print("Brute force result:")
    print_grid(brute_force_result)
    
    # Solve using backtracking
    start = time.time()
    backtracking_result = backtracking(grid)
    end = time.time()
    print('Backtracking time:', end - start)
    print("Backtracking result:")
    print_grid(backtracking_result)

