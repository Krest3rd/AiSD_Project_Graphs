from linked_list import Linked_List
from checks import check_matrix # type: ignore

# Prints the adjacency matrix in a readable format.
def print_matrix(matrix: list[list[int]]) -> None:
    check_matrix(matrix)
    
    # Print upper guide
    print("  |", end=' ')
    for i in range(len(matrix)):
        print(f"{i+1:2}", end=' ')
    print()

    # print upper separator
    print("__+", end='')
    for i in range(len(matrix)):
        print("___", end='')
    print()

    #  Print rows
    for row in range(len(matrix)):
        print(f"{row+1:2}|", end=' ')
        for col in range(len(matrix)):
            print(f"{matrix[row][col]:2}", end=' ')
        print()


# Checks if edge (start, end) exists in the adjacency matrix
# Returns True if it exists, False otherwise
def edge_exists(matrix: list[list[int]], start: int, end: int) -> bool:
    check_matrix(matrix)

    if start < 1 or start > len(matrix) or end < 1 or end > len(matrix):
        raise ValueError("Start and end nodes must be between 1 and the size of the matrix.")
    
    if matrix[start-1][end-1] == 1:
        return True
    else:
        return False


# This function implements a breadth-first search (BFS) algorithm on an adjacency matrix.
# It starts from a given node and explores all its neighbors before moving to the next level.
# The function returns a list of nodes visited in the order they were encountered.
def matrix_BreathFirstSearch(matrix: list[list[int]], start:int) -> list[int]:
    check_matrix(matrix)

    result = [start]
    visited = [False] * len(matrix)
    visited[start-1] = True
    current = 0


    while current < len(result):
        row = result[current]-1
        for i,j in enumerate(matrix[row]):
            if j == 1 and not visited[i]:
                result.append(i+1)
                visited[i] = True
        current += 1
    return result


# This function implements a depth-first search (DFS) algorithm on an adjacency matrix.
# It starts from a given node and explores as far as possible along each branch before backtracking.
# The function returns a list of nodes visited in the order they were encountered.
def matrix_DepthFirstSearch(matrix: list[list[int]], start:int) -> list[int]:
    check_matrix(matrix)

    stack = [start]
    visited = [False] * len(matrix)
    visited[start-1] = True
    result = [start]

    while stack:
        for i,j in enumerate(matrix[stack[-1]-1]):
            if j == 1 and not visited[i]:
                stack.append(i+1)
                visited[i] = True
                result.append(i+1)
                break
        else:
            stack.pop()

    return result
        

# This function implements Kahn's algorithm for topological sorting of a directed acyclic graph (DAG).
# It returns a list of nodes in topologically sorted order.
# The function first checks if the input matrix is valid and then calculates the in-degrees of each node.
# It uses a queue to process nodes with no incoming edges and updates the in-degrees of their successors.
# If the graph has cycles, it raises a ValueError.
def matrix_Kahn_topological_sort(matrix: list[list[int]]) -> list[int]:    
    check_matrix(matrix)

    n = len(matrix)
    # Calculate how many incoming edges each node has
    degrees = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                degrees[j] += 1

    # Create a queue of nodes with no incoming edges
    print(degrees)
    queue = []
    for i in range(len(degrees)):
        if degrees[i] == 0:
            queue.append(i+1)
    
    result = []
    while queue:
        # Get the first node in the queue
        node = queue.pop(0)
        result.append(node)

        # Decrease the incoming edge count for all its successors
        for i in range(len(matrix)):
            if matrix[node-1][i] == 1:
                degrees[i] -= 1
                if degrees[i] == 0:
                    queue.append(i+1)
    
    if len(result) != len(matrix):
        raise ValueError("Graph has cycles, topological sort not possible.")
    
    return result


# This function implements Tarjan's algorithm for topological sorting of a directed acyclic graph (DAG).
# It uses a depth-first search approach to find the topological order.
# The function returns a list of nodes in topologically sorted order.
# It raises a ValueError if the graph has cycles.
# The function uses a stack to keep track of the current path and a visited list to mark nodes as visited.
# It also maintains a result list to store the topological order.
# The function continues until all nodes are visited, and it handles cycles by checking the visited status of nodes.
def matrix_Trajan_topological_sort(matrix: list[list[int]]) -> list[int]:
    check_matrix(matrix)

    # 0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * len(matrix)
    result = []
    stack = []

    # Keep going until all nodes are visited
    while not all(i == 2 for i in visited):
        # Find the first unvisited node
        # and mark it as visiting
        for i,j in enumerate(visited):
            if j == 0:
                stack.append(i)
                visited[i] = 1
                break
        
        # Push 
        while stack:
            for i,j in enumerate(matrix[stack[-1]]):
                if j == 1:
                    if visited[i] == 1:
                        raise ValueError("Graph has cycles, topological sort not possible.")
                    if visited[i] == 0:
                        stack.append(i)
                        visited[i] = 1
                        break
            else:
                current = stack.pop()
                visited[current] = 2
                result.insert(0,current+1)
    return result


# Example usage:
if __name__ == "__main__" or True:

    matrix = [[0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 1, 0],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 1, 0]]

    print("Adjacency Matrix:")
    print_matrix(matrix)
    print("Edge exists (1, 2):", edge_exists(matrix, 1, 2))
    print("Edge exists (1, 3):", edge_exists(matrix, 1, 3))
    print("Edge exists (2, 1):", edge_exists(matrix, 2, 1))
    print("Breath First Search from node 5:")
    print(matrix_BreathFirstSearch(matrix, 5))
    print("Depth First Search from node 5:")
    print(matrix_DepthFirstSearch(matrix, 5))
    print("Topological Sort using Kahn's algorithm:")
    print(matrix_Kahn_topological_sort(matrix))
    print("Topological Sort using Tarjan's algorithm:")
    print(matrix_Trajan_topological_sort(matrix))
    



