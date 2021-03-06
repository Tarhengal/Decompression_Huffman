from platform import node
from node import Node
from frequency import extract

def huffman_tree(freq):
    
    nodes = [Node(char[0],char[1]) for char in freq]
    
    while len(nodes) > 1 :
        nodes.sort(key=lambda x: (x.freq,x.label))
        l_child = nodes[0]
        r_child = nodes[1]
        new_node = Node(l_child.freq+r_child.freq,l_child.label+r_child.label,l_child,r_child)
        nodes.remove(l_child)
        nodes.remove(r_child)
        nodes.append(new_node)

    return nodes