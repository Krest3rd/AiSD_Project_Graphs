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

    # def InsertAtBeginning(self, data):
    #     new_node = self.Node(data)
    #     new_node.next = self.head
    #     self.head = new_node

    # def InsertAtPosition(self, data, position):
    #     if position < 0:
    #         raise ValueError("Position must be a non-negative integer.")
        
    #     new_node = self.Node(data)
    #     if position == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #         return
        
    #     current_node = self.head
    #     for _ in range(position - 1):
    #         if current_node is None:
    #             raise IndexError("Position out of bounds.")
    #         current_node = current_node.next
        
    #     new_node.next = current_node.next
    #     current_node.next = new_node


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
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


        