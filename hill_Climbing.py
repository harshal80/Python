import random


def objective_function(x):
    return -(x**2)


def hill_climibing(max_iter=1000, step_size=0.1):
    current_solution = random.uniform(-10, 10)
    for _ in range(max_iter):
        next_soltion = current_solution + random.uniform(-step_size, step_size)
        if objective_function(next_soltion) > objective_function(current_solution):
            current_solution = next_soltion
    return current_solution


best_solution = hill_climibing()
print("Best Solution: ", best_solution)
print("objective value: ", objective_function(best_solution))
