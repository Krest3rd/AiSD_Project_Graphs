from random import randint

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


# for row in generate_adj_matrix(5,100):
#     print(row)

def matrix_to_edge_table(matrix: list[list]) -> list[tuple[int,int]]:
    # Check if matrix is list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("Only 2D list of list of int is accepted")
    print('OK')

    # Check if each value is 1, 0, or -1
    for row in matrix:
        if not all(i in {1,0,-1} and type(i) is int for i in row):
            raise ValueError("Allowed values are integers 1,0 and -1")
    
    # Checks if the matrix is an NxN matrix
    n = len(matrix)
    if not all(len(row)==n for row in matrix):
        raise ValueError("Input matrix has to be an NxN matrix")

    # Fill the table
    table = []
    for row in range(n):
        for col in range(row,n):
            if matrix[row][col] == 1:
                table.append((row,col))
            elif matrix[row][col] == -1:
                table.append((col,row))
    return table


def generate_edge_table(n: int, saturation: int) -> list[tuple[int,int]]:
    matrix = generate_adj_matrix(n, saturation)
    table = matrix_to_edge_table(matrix)
    return table

# for i in generate_edge_table(5,100):
#     print(i)

# def generate_list(n: int, saturation: int) -> dict:
#     matrix = generate_matrix(n, saturation)

