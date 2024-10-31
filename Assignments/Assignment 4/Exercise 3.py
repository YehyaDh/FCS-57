class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, val):  # O(1)
        self.elements.append(val)
    
    def pop(self):  # O(1)
        if len(self.elements) == 0:
            return None
        return self.elements.pop()
    
def decoding(val):
    s = Stack()
    for i in val:
        if i == " " or i.isalpha():
            s.push(i)
        elif i == "*" :
            res=s.pop()
            print(res,end='')
    decoded_word ="".join(reversed(s.elements))
    return decoded_word


inputj = "SIVLE ****** DAED TNSI ***"
result = decoding(inputj)
print(result)