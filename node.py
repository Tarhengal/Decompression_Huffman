class Node:

    def __init__(self, freq, label, left = None, right = None ):
        self.freq = freq
        self.label =  label
        self.left = left
        self.right = right
    
    def get_label(self):
        return self.label
    
    def get_freq(self):
        return self.freq
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def __str__(self):
        return f'{self.freq} {self.label} [{self.left},{self.right}]'
    
    def __repr__(self):
        return f'{self.freq} {self.label} [{self.left},{self.right}]'