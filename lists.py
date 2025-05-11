# Simple implementation of a singly linked list in Python
class Linked_List:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    # Find a node with the given data
    def Find(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    # Display the linked list
    def display(self):
        if  len(self) == 1:
            print(self.head.data,"->None",sep="")
            return
        if not self.head:
            return
        current_node = self.head
        while current_node.next:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(current_node.data)

    def __len__(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count


class EdgeTable:
    def __init__(self):
        self.nodes = 0
        self.edges = []

    def add_edge(self, start: int, end: int):
        if start < 1 or start > self.nodes or end < 1 or end > self.nodes:
            raise ValueError("Node values must be between 1 and the number of nodes.")
        self.edges.append((start, end))

    def __len__(self):
        return len(self.table)