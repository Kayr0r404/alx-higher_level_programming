#!/usr/bin/python3


class Node:

    def __init__(self, data, new_node=None):
        """
        class constructor
        args:
        data: The value or data stored in the node.
        new_node: A reference (pointer) to the next node in the linked list.
        """
        self.data = data
        self.next = new_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self._data = data

    @property
    def new_node(self):
        return self._node

    @new_node.setter
    def new_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self._node = value


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def sorted_insert(self, data):
        """
        Add a Node to the list while maintaining ascending order.
        """
        new_node = Node(data)  # Create a new node with the provided data

        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = new_node
        elif self.head.data >= data:
            # If the new node's data is smaller than
            # or equal to the head's data,
            # insert it at the beginning
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse the list to find the
            # correct position to insert the new node
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            # Insert the new node after the current node
            new_node.next = current.next
            current.next = new_node

    def printList(self):
        """
        Print the data in the list.
        """
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
