from lists import Linked_List

def check_matrix(matrix: list[list]) -> bool:
    # Check if matrix is list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("Only 2D list of list of int is accepted")

    # Check if each value is 1 and 0
    for row in matrix:
        if not all(i in {1,0} and type(i) is int for i in row):
            raise ValueError("Allowed values are integers 1 and 0")
    
    # Checks if the matrix is an NxN matrix
    n = len(matrix)
    if not all(len(row)==n for row in matrix):
        raise ValueError("Input matrix has to be an NxN matrix")
    
    # # Check if the matrix is symmetric
    # for i in range(n):
    #     for j in range(n):
    #         if matrix[i][j] != -matrix[j][i] and i!=j:
    #             raise ValueError("Matrix is not symmetric")
            
    # Check if the diagonal is 0 (no self loops)
    for i in range(n):
        if matrix[i][i] != 0:
            raise ValueError("Matrix has self loops")
    
    return True


def check_successor_lists(succesor_lists: list[Linked_List]) -> bool:
    # Check if successor lists contains linked lists
    if not all(isinstance(i, Linked_List) for i in succesor_lists):
        raise ValueError("Only list of linked lists is accepted.")

    # Check if values of nodes are integers
    for i in succesor_lists:
        current = i.head.next
        while current is not None:
            if type(current.data) is not int:
                raise ValueError("Successor list contains non-integer node.")
            current = current.next

    # Check if the successor lists are valid
    for i in succesor_lists:
        current = i.head.next
        while current is not None:
            if current.data < 0 or current.data > len(succesor_lists):
                raise ValueError("Successor list contains invalid node.")
            current = current.next
