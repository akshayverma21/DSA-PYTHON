from linkied_list_singly import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0

    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if self.is_empty():
             
            raise IndexError('stack empty')
        popped_item=self.start.item
        self.delete_first()
        self.item_count-=1
        return popped_item
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('stack empty')
        
    def size(self):
        return self.item_count
    


s1=Stack()
s1.push(4)
s1.push(5)
s1.push(40)
s1.push(50)
s1.push(60)
s1.push(4)
s1.push(5)
s1.push(40)
s1.push(50)
s1.push(60)

s1.push(4)
s1.push(5)
s1.push(40)
s1.push(50)
s1.push(60)
s1.push(4)
s1.push(5)
s1.push(40)
s1.push(50)
s1.push(60)

print(s1.peek())
print(s1.size())
print(s1.pop())
# print(a)
# print(s1.size())