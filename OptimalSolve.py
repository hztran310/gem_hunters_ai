from Test import generate_cnf

grid = [[2, None, None, 1, None],
        [None, 5, 4, 2, None],
        [3, None, None, 2, 1],
        [3, None, 6, None, 1],
        [2, None, None, 2, 1]]

def solve(cnf, grid):
    print("Solving the CNF...")

if __name__ == "__main__":
    cnf = generate_cnf(grid)
    solve(cnf, grid)

