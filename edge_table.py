# from checks import check_edge_table
from lists import EdgeTable

# Prints the edge table in a readable format.
def edge_table_print(edge_table: EdgeTable) -> None:
    # Check if the edge table is valid
    # check_edge_table(edge_table)

    # Print the edge table
    print(f"Number of nodes: {edge_table.nodes}")
    print("Start\tEnd")
    print("-----\t-----")
    for edge in edge_table.edges:
        print(f"{edge[0]}\t{edge[1]}")


# Checks if the edge exists in the edge table.
# Returns True if the edge exists, False otherwise.
def edge_exists_table(edge_table: EdgeTable, start: int, end: int) -> bool:
    # Check if the edge table is valid
    # check_edge_table(edge_table)

    return (start, end) in edge_table.edges


# Returns list of nodes reachable from the start node using BFS.
def table_BreathFirstSearch(edge_table: EdgeTable, start:int) -> list[int]:
    # Check if the edge table is valid
    # check_edge_table(edge_table)

    #  Initialize the result list and visited list
    result = [start]
    visited = [False] * edge_table.nodes
    visited[start-1] = True
    current = 0

    # Fill the result list using BFS 
    while current < len(result):
        for i in edge_table.edges:
            if i[0] == result[current] and not visited[i[1]-1]:
                result.append(i[1])
                visited[i[1]-1] = True
        current += 1
    return result

# Returns list of nodes reachable from the start node using DFS.
def table_DepthFirstSearch(edge_table: EdgeTable, start:int) -> list[int]:
    # Check if the edge table is valid
    # check_edge_table(edge_table)

    stack = [start]
    visited = [False] * edge_table.nodes
    visited[start - 1] = True
    result = [start]

    while stack:
        for i in edge_table.edges:
            if i[0] == stack[-1] and not visited[i[1]-1]:
                stack.append(i[1])
                visited[i[1]-1] = True
                result.append(i[1])
                break
        
        else:
            stack.pop()

    return result

# Sorts the nodes in topological order using Kahn's algorithm.
# Returns a list of nodes in topological order.
def table_Kahn_topological_sort(edge_table: EdgeTable) -> list[int]:
    # Check if the edge table is valid
    # check_edge_table(edge_table)

    # Initialize the in-degree of each node
    in_degree = [0] * edge_table.nodes
    for edge in edge_table.edges:
        in_degree[edge[1] - 1] += 1

    queue = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i + 1)

    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for edge in edge_table.edges:
            if edge[0] == node:
                in_degree[edge[1] - 1] -= 1
                if in_degree[edge[1] - 1] == 0:
                    queue.append(edge[1])

    if len(result) != edge_table.nodes:
        raise ValueError("Graph has cycles, topological sort not possible.")

    return result
        
# Sorts the nodes in topological order using Tarjan's algorithm.
# Returns a list of nodes in topological order.
def table_Trajan_topological_sort(edge_table: EdgeTable) -> list[int]:
    # 0 - not visited, 1 - visited, 2 - finished
    visited = [0] * edge_table.nodes
    result = []
    stack = []

    while not all(i == 2 for i in visited):
        
        for i,j in enumerate(visited):
            if j == 0:
                stack.append(i)
                visited[i] = 1
                break

        while stack:
            for i in edge_table.edges:
                if i[0] == stack[-1]+1: 
                    if visited[i[1]-1] == 1:
                        raise ValueError("Graph has cycles, topological sort not possible.")
                    if visited[i[1]-1] == 0:
                        stack.append(i[1]-1)
                        visited[i[1]-1] = 1
            else:
                current = stack.pop()
                visited[current] = 2
                result.insert(0,current+1)
    
    return result


if __name__ == "__main__":
    # Example usage
    # Create an edge table
    edge_table = EdgeTable()
    edge_table.nodes = 5
    for edge in [(1,2),(3,1),(3,4),(5,1),(5,4)]:
        edge_table.add_edge(edge[0], edge[1])
    edge_table_print(edge_table)
    print(table_BreathFirstSearch(edge_table, 5))
    print(table_DepthFirstSearch(edge_table, 5))
    print(table_Kahn_topological_sort(edge_table))
    print(table_Trajan_topological_sort(edge_table))