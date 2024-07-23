# TRY THIS https://towardsdatascience.com/how-to-develop-optimization-models-in-python-1a03ef72f5b4
# see https://towardsdatascience.com/unit-1-optimization-theory-e416dcf30ba8
# Libraries that you can use to solver linear programming / optimization problems
# cvxopt, pulp, cvxpy, ecos, from scipy.optimize import linprog



# Linear programming and discrete optimization with Python using PuLP
# Assumption for LP is that each variable is >= 0
# puLP interfaces the solvers CPLEX, COIN, Gurobi, ...
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Whiskas Problem", LpMinimize)   # name=...  sense=LpMinimize or sense=LpMaximize

# The Decision Variables
x1 = LpVariable("ChickenPercent", 0, 100, LpInteger)   # name=..., lowBound=0, upBound=100, cat=LpInteger, e=None
x2 = LpVariable("BeefPercent", 0, 100)  # default is LpContinuous

# The Objective function is added to 'prob' first
prob += 0.013 * x1 + 0.008 * x2, "Total Cost of Ingredients per can"

# Here are the linear constraints
prob += x1 + x2 == 100, "PercentagesSum"
prob += 0.100 * x1 + 0.200 * x2 >= 8.0, "ProteinRequirement"
prob += 0.080 * x1 + 0.100 * x2 >= 6.0, "FatRequirement"
prob += 0.001 * x1 + 0.005 * x2 <= 2.0, "FibreRequirement"
prob += 0.002 * x1 + 0.005 * x2 <= 0.4, "SaltRequirement"

# The problem data is written to an .lp file (text)
prob.writeLP("WhiskasModel.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()


# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# or simply
print(f"{x1.name} = {value(x1)}")
print(f"{x2.name} = {value(x2)}")

# The optimised objective function value is printed to the screen
print(f"Total Cost of Ingredients per can =  {value(prob.objective)}")