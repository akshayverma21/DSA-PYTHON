class priority_queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data,priority):
        index=0
        while index < len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))

       
    def pop(self):
        if self.is_empty():
            raise Exception('priority queue empty')
        return self.items.pop(0)
    

    def size(self):
        return len(self.items)


    def print_list(self):
        return print(self.items)
    
d1=priority_queue()
d1.push('akshay',1)
d1.push(4,6)
d1.push(2,5)
d1.push(1,4)
d1.push(1,3)
d1.push(1,2)
print(d1.pop())
# print(d1.size())
# d1.print_list()









        
        