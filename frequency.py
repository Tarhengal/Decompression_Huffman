def extract(name):
    file = open(name,'r')
    text = file.readlines()
    for i in range(len(text)) :
        text[i] = text[i].strip('\n')
    for i in range(1,len(text)):
        text[i] = (text[i][0],int(text[i][-1]))
    text.pop(0)
    reverse_text = reverseTuple(text)
    return reverse_text

def reverseTuple(lstOfTuple): 
    return [tup[::-1] for tup in lstOfTuple]