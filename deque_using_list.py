class DEQUE:
    def __init__(self):
        self.items=[]


    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self,data):
        if self.is_empty():
            self.items.append(data)
        else:
            self.items.insert(0,data)

    def insert_rear(self,data):
        if self.is_empty():
            self.items.append(data)

        else:
            self.items.append(data)

    def delete_front(self):
        if self.is_empty():
            return 'DEQUE IS EMPTY'
        else:
            item=self.items[0]
            self.items.pop(0)
            return item
        
    def delete_rear(self):
        if self.is_empty():
            return None
        else:
            item=self.items[-1]
            self.items.pop(-1)
            return item
        
    def size(self):
        return len(self.items)
    
    def get_front(self):
        if self.is_empty():
            return 'empty'
        else:
            return self.items[0]
        
    def get_rear(self):
        if self.is_empty():
            return 'empty'
        else: 
            return self.items[-1]
        
    
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
        

