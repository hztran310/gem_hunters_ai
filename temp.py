from pysat.solvers import Glucose3

def solve_cnf(cnf):
    solver = Glucose3()

    # Add all the clauses in the CNF to the solver
    for clause in cnf:
        solver.add_clause(clause)

    # Check if the CNF is satisfiable
    if solver.solve():
        model = solver.get_model()
        print("The CNF is satisfiable. Here is one possible model:")
        print(model)
    else:
        print("The CNF is not satisfiable.")

cnf = [[-1, 2], [-2, 3], [-1], [3]]

solve_cnf(cnf)
