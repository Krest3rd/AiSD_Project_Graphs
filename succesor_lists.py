from lists import Linked_List
from help import check_successor_lists, calculate_circle_positions

def succesor_lists_print(succesor_lists: list[Linked_List]) -> None:
    check_successor_lists(succesor_lists)

    for i in succesor_lists:
        i.display()


def edge_exists_list(succesor_lists: list[Linked_List], start: int, end: int) -> bool:
    check_successor_lists(succesor_lists)

    if start < 1 or start > len(succesor_lists) or end < 1 or end > len(succesor_lists):
        raise ValueError("Node values must be between 1 and the number of nodes.")

    return succesor_lists[start - 1].Find(end)


def list_BreathFirstSearch(succesor_lists: list[Linked_List], start: int) -> list[int]:
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


def list_DepthFirstSearch(succesor_lists: list[Linked_List], start: int) -> list[int]:
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
                result.append(stack[-1])
                break
            current = current.next
        else:
            stack.pop()

    
    return result


def list_Kahn_topological_sort(succesor_lists: list[Linked_List]) -> list[int]:
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

def list_export(succesor_lists: list[Linked_List]) -> None:
    positions = calculate_circle_positions(len(succesor_lists))
    result = "\\begin{scope}[every node/.style={circle,thick,draw}]\n"
    for i in range(len(succesor_lists)):
        result += f"\t\\node at ({positions[i][0]},{positions[i][1]}) {{{i+1}}};\n"
    result += "\\end{scope}\n\n"
    result += "\\begin{scope}[every edge/.style={thick}]\n"
    for i,j in enumerate(succesor_lists):
        current = j.head.next
        while current is not None:
            result += f"\t\\path [->] ({i+1}) edge ({current.data});\n"
            current = current.next
    result += "\\end{scope}\n"
    print(result)


def list_Tarjan_topological_sort(succesor_lists: list[Linked_List]) -> list[int]:
    check_successor_lists(succesor_lists)

    # 0 - unvisited, 1 - visited, 2 - finished
    visited = [0] * len(succesor_lists)
    result = []
    stack = []

    while not all(visited):
        for i in range(len(visited)):
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                break

        while stack:
            current = succesor_lists[stack[-1]].head.next
            while current is not None:
                if visited[current.data - 1] == 1:
                    raise ValueError("Graph has cycles, topological sort not possible.")
                if visited[current.data - 1] == 0:
                    stack.append(current.data - 1)
                    visited[current.data - 1] = 1
                    break
                current = current.next
            else:
                current = stack.pop()
                visited[current] = 2
                result.insert(0,current + 1)

    return result


if __name__ == "__main__":
    succesor_lists = [Linked_List() for _ in range(5)]
    for i in range(5):
        succesor_lists[i].InsertAtEnd(i + 1)
    
    succesor_lists[0].InsertAtEnd(2)
    succesor_lists[2].InsertAtEnd(1)
    succesor_lists[2].InsertAtEnd(4)
    succesor_lists[4].InsertAtEnd(1)
    succesor_lists[4].InsertAtEnd(4)

    succesor_lists_print(succesor_lists)
    print(list_BreathFirstSearch(succesor_lists, 1))
    print(list_DepthFirstSearch(succesor_lists, 1))
    print(list_Kahn_topological_sort(succesor_lists))
    print(list_Tarjan_topological_sort(succesor_lists))
    list_export(succesor_lists)