class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return print(self.items.pop(0))
        return 'queue is empty'
    
    def getFront(self):
        if not self.is_empty():
            return print(self.items[0])
        return 'queue is empty'
        
    
    def getRear(self):
        if not self.is_empty():
            return print(self.items[-1])
        return 'queue is empty'
    
    def size(self):
        return print(len(self.items))
    
s1=Queue()
s1.enqueue(1)
s1.enqueue(2)
s1.enqueue(3)
s1.enqueue(4)
s1.size()
s1.dequeue()
s1.dequeue()

s1.getFront()
s1.getRear()
s1.size()
