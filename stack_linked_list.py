class Node:
    def __init__(self, item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self, start=None):
        self.start=start
        self.item_count=0
    
    def is_empty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError('stack empty')

    def peek(self):
        if self.is_empty():
            raise self.is_empty()
        else:
            return self.start.item
        
    def size(self):
        return self.item_count
        
    
        

        

s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.pop()
# print(s1.is_empty())
# print(s1.is_empty())
print(s1.peek())
print(s1.item_count)
