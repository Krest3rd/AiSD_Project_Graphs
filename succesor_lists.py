from lists import Linked_List
from checks import check_successor_lists

def succesor_lists_print(succesor_lists: list[Linked_List]) -> None:
    check_successor_lists(succesor_lists)

    for i in succesor_lists:
        i.display()


def edge_exists_list(succesor_lists: list[Linked_List], start: int, end: int) -> bool:
    check_successor_lists(succesor_lists)

    if start < 1 or start > len(succesor_lists) or end < 1 or end > len(succesor_lists):
        raise ValueError("Node values must be between 1 and the number of nodes.")

    return succesor_lists[start - 1].Find(end)


def table_BreathFirstSearch(succesor_lists: list[Linked_List], start: int) -> list[int]:
    check_successor_lists(succesor_lists)

    if start < 1 or start > len(succesor_lists):
        raise ValueError("Start value must be between 1 and the number of nodes")
    
    result = [start]
    visited = [False] * len(succesor_lists)
    visited[start - 1] = True
    i = 0

    while i < len(result):
        current = succesor_lists[result[i] - 1].head.next
        while current is not None:
            if not visited[current.data - 1]:
                result.append(current.data)
                visited[current.data - 1] = True
            current = current.next
        i += 1
    
    return result


def table_DepthFirstSearch(succesor_lists: list[Linked_List], start: int) -> list[int]:
    check_successor_lists(succesor_lists)

    if start < 1 or start > len(succesor_lists):
        raise ValueError("Start value must be between 1 and the number of nodes")
    
    stack = [start]
    visited = [False] * len(succesor_lists)
    visited[start - 1] = True
    result = [start]

    while stack:
        current = succesor_lists[stack[-1] - 1].head.next
        while current is not None:
            if not visited[current.data - 1]:
                stack.append(current.data)
                visited[current.data - 1] = True
                break
            current = current.next
        else:
            stack.pop()
            result.append(stack[-1])
    
    return result


def table_Kahn_topological_sort(succesor_lists: list[Linked_List]) -> list[int]:
    check_successor_lists(succesor_lists)

    in_degree = [0] * len(succesor_lists)
    for i in succesor_lists:
        current = i.head.next
        while current is not None:
            in_degree[current.data - 1] += 1
            current = current.next

    queue = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i + 1)

    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        current = succesor_lists[node - 1].head.next
        while current is not None:
            in_degree[current.data - 1] -= 1
            if in_degree[current.data - 1] == 0:
                queue.append(current.data)
            current = current.next
    
    if len(result) != len(succesor_lists):
        raise ValueError("Graph has cycles, topological sort not possible.")
    
    return result


if __name__ == "__main__":
    succesor_lists = []
    for i in range(5):
        linked_list = Linked_List()
        linked_list.InsertAtEnd(i+1)
        for j in range(i+1, 5):
            linked_list.InsertAtEnd(j+1)
        succesor_lists.append(linked_list)
    succesor_lists_print(succesor_lists)
    print(table_BreathFirstSearch(succesor_lists, 1))
    print(table_DepthFirstSearch(succesor_lists, 1))