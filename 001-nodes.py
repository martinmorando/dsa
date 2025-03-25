'''
    Nodes
    + Most nodes contain: 
        - data: integers, strings, arrays, etc.
        - links (AKA "pointers"): reference/s to other node/s.
    
    If the node contains only null pointers ("None" in Python), 
    this means we are at the end of the node path.

    Pending questions: Is there no link or is the link null? 
'''

class Node:

    # Initialize a node with a value and an optional link to another node
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    # Returns the value of the node
    def get_value(self):
        return self.value

    # Returns the link to the next node
    def get_link_node(self):
        return self.link_node

    # Sets the link to the next node
    def set_link_node(self, link_node):
        self.link_node = link_node


# Create nodes
a = Node("A")
b = Node("B")
c = Node("C")

# Link nodes: a -> b -> c
a.set_link_node(b)
b.set_link_node(c)
# c has no link because there are no more nodes

# Get data from linked nodes
b_data = a.get_link_node().get_value()
c_data = b.get_link_node().get_value()

# Print data
print(b_data)
print(c_data)