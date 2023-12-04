#!/usr/bin/python3
class Node() : 
    def __init__(self , data , next_node = None) : 
        self.__data = data
        self.__next_node = next_node
        
    @property 
    def data(self) : 
        return self.__data 
    @data.setter 
    def data(self , value ) : 
        if not isinstance(value , int) : 
            raise TypeError("data must be an integer")
        else : 
            self.__data = value
            
            
    @property 
    def next_node(self) : 
        return self.__next_node 
    
    @next_node.setter 
    def next_node(self, node):
        if type(node).__name__ != 'Node' and node is not None:
            raise TypeError('next_node must be a Node object')
        else : 
            self.__next_node = node
            
            

class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """
        Initialize a SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the linked list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            crnt = self.head
            while crnt.next_node is not None and crnt.next_node.data < value:
                crnt = crnt.next_node
            new_node.next_node = crnt.next_node
            crnt.next_node = new_node

    def __str__(self):
        """
        Generate a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "h".join(nodes)
                
            
            
        
        
    
    
    
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
        
        