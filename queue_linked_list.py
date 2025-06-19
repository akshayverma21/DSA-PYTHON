class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,start=None,rear=None):
        self.start=start
        self.rear=rear
        self.item_count=0

    def is_empty(self):
        return self.start==None
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
            self.rear=n
            self.item_count+=1
        else:
            self.rear.next=n
            self.rear=n
            self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            return None
        
        temp=self.start
        value=temp.item

        self.start=self.start.next
        if self.start is None:
            self.rear=None

        self.item_count-=1
        return value
       
       
            

    def get_front(self):
        return self.start.item
    
    def get_rear(self):
        return self.rear.item
    

    def size(self):
        return print(self.item_count)
    
s1=Queue()
s1.enqueue(1)
s1.enqueue(2)
s1.enqueue(3)
s1.enqueue(4)
s1.enqueue(5)

print(s1.get_front())
print(s1.dequeue())
s1.size()
print(s1.get_rear())

print(s1.dequeue())
# s1.size()
# print(s1.get_rear())
# s1.size()




