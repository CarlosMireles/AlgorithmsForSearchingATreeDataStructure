# Search methods
import time
import search

ab = search.GPSProblem('A', 'B', search.romania)

# Time measurement breadth_first_graph_search
initial_time = time.perf_counter()
broad = search.breadth_first_graph_search(ab)
broad_time = round((time.perf_counter() - initial_time), 13) * 10**3

# Time measurement depth_first_graph_search
initial_time = time.perf_counter()
deep = search.depth_first_graph_search(ab)
deep_time = round((time.perf_counter() - initial_time), 13) * 10**3

# Time measurement branch_and_bound_search
initial_time = time.perf_counter()
branch_and_bound = search.branch_and_bound_search(ab)
branch_and_bound_time = round((time.perf_counter() - initial_time), 13) * 10**3

# Time measurement branch_and_bound_with_heuristic_search
initial_time = time.perf_counter()
branch_and_bound_with_heuristic = search.branch_and_bound_with_heuristic_search(ab)
branch_and_bound_with_heuristic_time = round((time.perf_counter() - initial_time), 13) * 10**3

# ------------------------------------------------------ #

print("Bread-first Search", " -- Execution time: ", str(broad_time) + " ms")
print("Generated Nodes: " + str(broad[1]) + " - Visited Nodes: " + str(broad[2]))
print("Total Cost = " + str(broad[3]))
print(broad[0].path())

print("")

print("Depth-first Search", " -- Execution time: ", str(deep_time) + " ms")
print("Generated Nodes: " + str(deep[1]) + " - Visited Nodes: " + str(deep[2]))
print("Total Cost = " + str(deep[3]))
print(deep[0].path())

print("")

print("Branch and Bound Search", " -- Execution time: ", str(branch_and_bound_time) + " ms")
print("Generated Nodes: " + str(branch_and_bound[1]) + " - Visited Nodes: " + str(branch_and_bound[2]))
print("Total Cost = " + str(branch_and_bound[3]))
print(branch_and_bound[0].path())

print("")

print("Branch and Bound with Heuristic Search", " -- Execution time: ",
      str(branch_and_bound_with_heuristic_time) + " ms")
print("Generated Nodes: " + str(branch_and_bound_with_heuristic[1]) + " - Visited Nodes: "
      + str(branch_and_bound_with_heuristic[2]))
print("Total Cost = " + str(branch_and_bound_with_heuristic[3]))
print(branch_and_bound_with_heuristic[0].path())
