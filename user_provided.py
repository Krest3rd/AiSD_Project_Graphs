from linked_list import Linked_List

def input_to_successor_list(size: int) -> list[Linked_List]:
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    list = []

    for i in range(1,size+1):
        print(f"\t{i}> ", end='', flush=True)
        successors = [int(i) for i in input().strip().split()]
        successors.sort()

        if len(successors) == 0:
            successors.append(0)

        linked_list = Linked_List()
        linked_list.InsertAtEnd(i)
        for j in successors:
            linked_list.InsertAtEnd(j)
        list.append(linked_list)
    return list

# for i in input_to_successor_list(5):
#     i.display()