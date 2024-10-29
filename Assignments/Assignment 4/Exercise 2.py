class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, val):  # O(1)
        self.elements.append(val)
    
    def pop(self):  # O(1)
        if len(self.elements) == 0:
            return None
        return self.elements.pop()

def is_balanced(expression):
    s = Stack()
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in parentheses_map.values():
            s.push(char)  
        elif char in parentheses_map.keys():
            if len(s.elements) == 0 or s.elements[-1] != parentheses_map[char]:  
                return False
            s.pop()  
    
    return len(s.elements) == 0

# Test cases
print(is_balanced("(1+2)-3*[41+6]"))         
print(is_balanced("(1+2)-3*[41+6}"))         
print(is_balanced("(1+2)-3*[41+6"))          
print(is_balanced("(1+2)-3*]41+6["))         
print(is_balanced("(1+[2-3]*4{41+6})"))     
    