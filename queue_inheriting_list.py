class Queue(list):
    def is_empty(self):
        return len(self)==0
    
    def enqueue(self,data):
        self.append(data)
       
       
    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        return ("stack empty")
    
    def getFront(self):
        if not self.is_empty():
            return print(self[0])
        return ("stack empty")
    
    def getRear(self):
        if not self.is_empty():
            return print(self[-1])
        return ("stack empty")
    
    def size(self):
        return print(len(self))
        
    

    

s1=Queue()
s1.enqueue(1)
s1.enqueue(2)
s1.enqueue(3)
s1.enqueue(4)

print(s1)

# print(s1.dequeue())
# print(s1.dequeue())
# print(s1.dequeue())
# print(s1.dequeue())
# print(s1.dequeue())
s1.getFront()
s1.getRear()
s1.size()




    
    


    
