from linked_list import Linked_List
from checks import check_matrix # type: ignore

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
    
    



