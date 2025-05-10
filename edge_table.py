from checks import check_edge_table # type: ignore

# Prints the edge table in a readable format.
def edge_table_print(edge_table: list[tuple[int,int]]) -> None:
    # Check if the edge table is valid
    check_edge_table(edge_table)

    # Print the edge table
    print("Start\tEnd")
    print("-----\t-----")
    for edge in edge_table:
        print(f"{edge[0]}\t{edge[1]}")


def edge_exists_table(edge_table: list[tuple[int,int]], start: int, end: int) -> bool:
    # Check if the edge table is valid
    check_edge_table(edge_table)

    return (start, end) in edge_table


def table_BreathFirstSearch(edge_table: list[tuple[int,int]], start:int) -> list[int]:
    # Check if the edge table is valid
    check_edge_table(edge_table)

    #  Initialize the result list and visited list
    result = [start]
    visited = [False] * (max(max(edge_table)) + 1)
    visited[start] = True
    current = 0

    # Fill the result list using BFS 
    while current < len(result):
        for i in edge_table:
            if i[0] == result[current] and not visited[i[1]]:
                result.append(i[1])
                visited[i[1]] = True
        current += 1
    return result


def table_DepthFirstSearch(edge_table: list[tuple[int,int]], start:int) -> list[int]:
    # Check if the edge table is valid
    check_edge_table(edge_table)

    stack = [start]
    visited = [False] * (max(max(edge_table)))
    visited[start - 1] = True
    result = [start]

    while stack:
        for i in edge_table:
            if i[0] == stack[-1] and not visited[i[1]-1]:
                stack.append(i[1])
                visited[i[1]-1] = True
                result.append(i[1])
                break
        
        else:
            stack.pop()

    return result



if __name__ == "__main__":
    # Example usage
    # Create an edge table
    edge_table = [(1,2),(3,1),(3,4),(5,1),(5,4)]
    edge_table_print(edge_table)
    print(table_BreathFirstSearch(edge_table, 5))
    print(table_DepthFirstSearch(edge_table, 5))