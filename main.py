from platform import node
from sqlalchemy import null
from node import Node
from frequency import extract
from huffman import huffman_tree
from binary import extract_bin
from parcours import parcours

freq = extract("exemple_freq.txt")
tree = huffman_tree(freq)
compr = str(extract_bin("exemple_comp.bin"))
text = ""
while len(compr) != 0 :
    text += parcours(tree[0],compr)[0]
    compr = parcours(tree[0],compr)[1]

print("Le texte decompréssé est :")
print(text)