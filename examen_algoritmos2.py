#crear un asolucion para maxz=2x1+3x2+4x3+5x4 mostrando los pasos que siguio para llegar al final en python?

from pulp import LpMaximize, LpVariable, LpProblem, value

# Define the linear programming problem
prob = LpProblem("Maximize Z", LpMaximize)

# Define the decision variables
x1 = LpVariable("x1", lowBound=-infinity, upBound=infinity)
x2 = LpVariable("x2", lowBound=-infinity, upBound=infinity)
x3 = LpVariable("x3", lowBound=-infinity, upBound=infinity)
x4 = LpVariable("x4", lowBound=-infinity, upBound=infinity)

# Define the objective function
prob += 2*x1 + 3*x2 + 4*x3 + 5*x4, "maxz"

# Define the constraints (if any)
# (In this case, there are no constraints, so we can skip this step)

# Solve the linear programming problem
prob.solve()

# Print the optimal solution
print("Optimal solution:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x3 =", value(x3))
print("x4 =", value(x4))
print("Maximum value of maxz =", value(prob.objective))