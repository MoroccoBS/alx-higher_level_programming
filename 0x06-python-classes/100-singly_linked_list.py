#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class"""


class Node:
    """Represents a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __str__(self):
        """Return a string representation of the list"""
        node_strings = []
        ptr = self.__head

        while ptr is not None:
            node_strings.append(str(ptr.data))
            ptr = ptr.next_node

        return "\n".join(node_strings)

    def __init__(self):
        """Initialize a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node into a sorted singly linked list"""
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
