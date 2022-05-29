from platform import node
from sqlalchemy import null
from node import Node
from frequency import extract
from huffman import huffman_tree
from binary import extract_bin

cpt = 0

def parcours(node,code):

    if node.left == None and node.right == None :
        code = code[cpt:]
        cpt = 0
        return (node.label,code)

    else :
        if code[cpt] == 0 :
            cpt+=1
            parcours(node.left,code[cpt])
        if code == 1 :
            cpt += 1
            parcours(node.right,code[cpt])
