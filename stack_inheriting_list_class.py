class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        return self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('stack empty')
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError
        
    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            return []
        
    def insert(self,index, data):
        raise AttributeError('no attribute to "insert" in stack')

s1=Stack()
s1.push(4)
s1.push(5)
s1.push(40)

print(s1.peek())

print(s1.pop())
print(s1.pop())