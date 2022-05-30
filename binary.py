from sympy import O

def extract_bin(name) :
    with open(name,"rb") as file:
        data = file.read()
    
    new_char = ""

    for oct in data: 
        new_char += OctToBin(oct)

    return new_char
    
def OctToBin(o):
    return bin(o)[2:]

