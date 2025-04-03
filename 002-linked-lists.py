'''
    TO DO: remove method

    Linked Lists
    - A sequential chain of nodes; one of the basic data structures.
    - Can be unidirectional o bidirectional.
    - Head node: (the single) node at the beginning of the list. Tail node: (the single) 
                 node at the end of the list.
    - The nodes don't need to be sequentially located in memory.
    - Actual methods defined depend on the use case.
    - Operations:
        - Add nodes: add a new node to the current head node to maintain connection with 
                     following nodes.
        - Remove nodes: remove all references to the node. Adjust link on the previous node 
                        so that it points to the following node, in order to avoid orphaned nodes.
                        In some languages, this is done automatically.
        - Find a node
        - Traverse the linked list (travel through)
    
    - Example: airports as nodes and their travel segments as links, where initial departure 
      airport is the head node, the final city is the tail node and each flight segment are the links.
'''

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
  
    def get_next_node(self):
        return self.next_node
  
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
  
    def get_head_node(self):
        return self.head_node
  
    # Insert new head node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node      # Replace the current head node with the new one

    # Traverse the linked list and return the nodes values as string
    def stringify_list(self):
        current_node = self.get_head_node()
        string_list = ""
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return string_list

    # Remove method
      

# Create linked list
my_linked_list = LinkedList(2)

# Add new nodes
my_linked_list.insert_beginning(55)
my_linked_list.insert_beginning(4)
my_linked_list.insert_beginning(21000000)

# Print the linked list
print(my_linked_list.stringify_list())