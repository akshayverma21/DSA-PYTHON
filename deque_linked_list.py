class Node:
    def __init__(self,item=None,prev=None, next=None):
        self.item=item
        self.prev=prev
        self.next=next

class DEQUE:
    def __init__(self):
        self.start=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.start is None
    
    
    def insert_front(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
            self.rear=n
            self.item_count+=1
        else:
            n.next=self.start
            self.start.prev=n
            self.start=n
            self.item_count+=1

    def insert_rear(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
            self.rear=n
            self.item_count+=1
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.prev=temp
            self.rear=n
            self.item_count+=1

    def delete_front(self):
        if self.is_empty():
            return 'deque is empty'
        
        temp=self.start
        value=temp.item

        self.start=self.start.next
       
        if self.start is None:
            self.rear=None
        else:
            self.start.prev=None
           
        self.item_count-=1
        return value
    
    def delete_rear(self):
        
        if self.is_empty():
            return 'deque is empty'

        elif self.start.next is None:
            temp=self.start
            value=temp.item
            self.start=None
            self.rear=None
            self.item_count-=1
            return value
        else:
            temp=self.rear
            value=temp.item
            self.rear=temp.prev
            temp.prev.next=None
            self.item_count-=1
            return value
            
        

    def get_front(self):
        if self.is_empty():
            return 'deque is empty'
        return self.start.item
    
    def get_rear(self):
        if self.is_empty():
            return 'deque is empty'
        return self.rear.item
    

    def size(self):
        if self.is_empty():
            return 'deque is empty'

        return self.item_count


# Test the DEQUE
d = DEQUE()
print(d.is_empty())  # True
d.insert_front(10)
d.insert_rear(20)
d.insert_front(5)
print(d.size())  # 3
print(d.get_front())  # 5
print(d.get_rear())  # 20
print(d.delete_front())  # 5
print(d.delete_rear())  # 20
print(d.size())  # 1
print(d.get_front())  # 10
print(d.delete_front())  # 10
print(d.is_empty())  # True
print(d.delete_front())  # 'deque is empty'

        