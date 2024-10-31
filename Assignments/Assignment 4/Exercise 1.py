class Stack:
    def __init__(self):
        self.elements=[]
    def push(self,val): #O(1)
        self.elements.append(val)
    def pop(self): #O(1)
        if len(self.elements)==0:
            return None
        return self.elements.pop()


def is_palindrome(val) -> bool:
    if len(val) == 0:
        return True
    s = Stack()
    for i in val:
        s.push(i)
    reversed_word = ""
    top_letter = s.pop()
    while top_letter != None:
        reversed_word +=  top_letter
        top_letter = s.pop()
    return val.lower() == reversed_word.lower()



fakeuserinput = "Neveroddoreven"
result = is_palindrome(fakeuserinput)
print(result)
    
        