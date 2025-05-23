from lists import Linked_List, EdgeTable
from help import check_successor_lists

# Function to take input for successor lists
# and convert them into linked lists
def input_to_successor_list(size: int) -> list[Linked_List]:
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    list = []

    for i in range(1,size+1):
        while True:
            print(f"\t{i}> ", end='', flush=True)
            try:
                successors = [int(i) for i in input().strip().split()]
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue

            # Remove duplicates
            successors = [i for i in set(successors)]
            successors.sort()

            if not all(i<size+1 and i>0 for i in successors):
                print("Successor values must be between 1 and the number of nodes.")
            else:
                break
            

        # if len(successors) == 0:
        #     successors.append(0)

        linked_list = Linked_List()
        linked_list.InsertAtEnd(i)
        for j in successors:
            linked_list.InsertAtEnd(j)
        list.append(linked_list)
    return list
    

# Function to convert successor lists into an adjacency matrix
# The adjacency matrix is a 2D list where adj_matrix[i][j] = 1 if there is an edge from i to j
# and adj_matrix[i][j] = -1 if there is an edge from j to i
# and adj_matrix[i][j] = 0 if there is no edge between i and j
def succesor_lists_to_adj_matrix(succesor_lists: list[Linked_List]) -> list[list[int]]:
    # Check if the successor lists are valid
    check_successor_lists(succesor_lists)

    size = len(succesor_lists)
    adj_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in succesor_lists:
        current = i.head.next
        while current is not None:
            if current.data != 0:
                adj_matrix[i.head.data - 1][current.data - 1] = 1
                # adj_matrix[current.data - 1][i.head.data - 1] = -1
            current = current.next
    return adj_matrix


def successor_list_to_edge_table(succesor_lists: list[Linked_List]) -> EdgeTable:
    # Check if the successor lists are valid
    check_successor_lists(succesor_lists)
    
    # Fill the table
    table = EdgeTable()
    table.nodes = len(succesor_lists)
    for i in succesor_lists:
        current = i.head.next
        while current is not None:
            if current.data != 0:
                table.add_edge(i.head.data, current.data)
            current = current.next
    return table


# Example usage:
if __name__ == "__main__":
    size = int(input("Enter the number of nodes: "))
    print("Enter the successors for each node (space-separated):")
    succesor_lists = input_to_successor_list(size)
    
    adj_matrix = succesor_lists_to_adj_matrix(succesor_lists)
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(row)

    edge_table = successor_list_to_edge_table(succesor_lists)
    print("Edge Table:")
    for edge in edge_table.edges:
        print(edge)

