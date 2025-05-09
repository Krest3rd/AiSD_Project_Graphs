from random import randint
from linked_list import Linked_List

# This function generates a random adjacency matrix of size n x n with a given saturation percentage.
# The saturation percentage determines how many of the possible edges in the upper triangle of the matrix are filled with 1s.
# The matrix is symmetric, with 1 indicating a directed edge from node i to node j, and -1 indicating a directed edge from node j to node i.
# The upper triangle of the matrix is the only part that is filled with ones to avoid cycles.
def generate_adj_matrix(n: int, saturation: int) -> list[list[int]]:
    # Check if saturation is in correct range
    if saturation > 100 or saturation < 0:
        raise ValueError('Saturation has to be between 0 and 100')
    
    # Calculate how many fields in the upper triangle of matrix (excluding the main diag)
    count = 0
    for i in range(1,n):
        count += i

    # Calculate how many fields have to be filled (always rounds down)
    count = int(count * saturation/100)
    
    # Create empty matrix
    print('Creating matrix')
    matrix = [[0 for i in range(n)] for i in range(n)]

    # Randomly fill in the triangle (can potentially go on for infinity probably should change it)
    while count:
        i = randint(0,n-2)
        j = randint(i+1,n-1)
        if matrix[i][j] == 0:
            # print(j,i)
            matrix[i][j] = 1
            matrix[j][i] = -1
            count -=1
    print('Matrix Created')
    return matrix


def check_matrix(matrix: list[list]) -> bool:
    # Check if matrix is list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("Only 2D list of list of int is accepted")

    # Check if each value is 1, 0, or -1
    for row in matrix:
        if not all(i in {1,0,-1} and type(i) is int for i in row):
            raise ValueError("Allowed values are integers 1,0 and -1")
    
    # Checks if the matrix is an NxN matrix
    n = len(matrix)
    if not all(len(row)==n for row in matrix):
        raise ValueError("Input matrix has to be an NxN matrix")
    
    # Check if the matrix is symmetric
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -matrix[j][i]:
                raise ValueError("Matrix is not symmetric")
    
    return True



# This function converts a adjecency matrix into an edge table.
# The edge table is a list of tuples, where each tuple (i,j) represents a directed edge from node i to node j.
def matrix_to_edge_table(matrix: list[list]) -> list[tuple[int,int]]:
    # Check if the matrix is valid
    check_matrix(matrix)

    n = len(matrix)

    # Fill the table
    table = []
    for row in range(n):
        for col in range(row,n):
            if matrix[row][col] == 1:
                table.append((row,col))
            elif matrix[row][col] == -1:
                table.append((col,row))
    return table

# This function generates an edge table from a random adjacency matrix of size n x n with a given saturation percentage.
# def generate_edge_table(n: int, saturation: int) -> list[tuple[int,int]]:
#     matrix = generate_adj_matrix(n, saturation)
#     table = matrix_to_edge_table(matrix)
#     return table


# This function converts an adjacency matrix into a list of succesor lists.
# Each linked list represents the successors of a node, with the first element being the node itself.
# For readability value of the node is increased by 1.
# If a node has no successors, a 0 is added to the list.
def matrix_to_succesor_list(matrix: list[list]) -> list[Linked_List]:
    check_matrix(matrix)

    n = len(matrix)
    list = []
    for i in range(n):
        flag = False
        linked_list = Linked_List()
        linked_list.InsertAtEnd(i+1)
        for j in range(n):
            if matrix[i][j] == 1:
                linked_list.InsertAtEnd(j+1)
                flag = True
        if not flag:
            linked_list.InsertAtEnd(0)
        list.append(linked_list)
    return list

# def generate_succesor_lists(n: int, saturation: int) -> list[Linked_List]:
#     matrix = generate_adj_matrix(n, saturation)
#     return matrix_to_linked_list(matrix)

# Example usage
if __name__ == "__main__":
    n = 5
    saturation = 50
    matrix = generate_adj_matrix(n, saturation)
    for row in matrix:
        print(row)
    table = matrix_to_edge_table(matrix)
    for i in table:
        print(i)
    succesor_lists = matrix_to_succesor_list(matrix)
    for i in succesor_lists:
        i.display()

