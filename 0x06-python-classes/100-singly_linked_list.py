#!/usr/bin/python3
"""Modulde that implements singlylinked list"""
try:
    class Node:
        """class Node"""
        def __init__(self, data, next_node=None):
            """Constructor"""
            self.data = data
            self.next_node = next_node
        @property
        def data(self):
            """"get the node's data"""
            return self.__data
        
        @data.setter
        def data(self, value):
            """"set the node's data"""
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value
        
        @property
        def next_node(self):
            """"get the next node"""
            return self.__next_node
        
        @next_node.setter
        def next_node(self, value):
            """"set the next node's data"""
            if value is not None and not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
            self.__next_node = value

    class SinglyLinkedList:
        """"A singly linked list class"""
        def __init__(self):
            """Constructor"""
            self.__head = None
        def __str__(self):
            """"making the list printable"""
            result = []
            current = self.__head
            while current:
                result.append(str(current.data))
                current = current.next_node
            return "\n".join(result)
        
        def sorted_insert(self, value):
            """sorts the values in the list in descending order"""
            new_node = Node(value)
            if self.__head is None or self.__head.data >= new_node.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                current = self.__head
                while current.next_node is not None and current.next_node.data < new_node.data:
                    current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node
except TypeError as e:
    print(e)