from linkied_list_singly import *

class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0


    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item

        pass
    def pop(self):
        if not self.is_empty():
           self.mylist.delete_first()
           self.item_count-=1
        else:
            raise IndexError("empty")
        
    
s=Stack()
s.push(30)
s.push(20)
s.push(10)
print("s1.peek",s.peek())


    
