from Test import generate_cnf, print_grid

grid = [[2, None, None, 1, None],
        [None, 5, 4, 2, None],
        [3, None, None, 2, 1],
        [3, None, 6, None, 1],
        [2, None, None, 2, 1]]

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


if __name__ == "__main__":
    cnf = generate_cnf(grid)
    model = DPLL(cnf)
    print("Input: ")
    print_grid(grid)
    if model is False:
        print("The CNF is unsatisfiable")
    else:
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

