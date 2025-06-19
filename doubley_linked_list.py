            
class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, None, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = n
        n.prev = temp

    

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is None:
            return
        n = Node(data, temp, temp.next)
        if temp.next is not None:
            temp.next.prev = n
        temp.next = n
    
    def delete_first(self):
        if self.is_empty():
            return
        self.start=self.start.next
        if self.start is not None:
            self.start.prev=None

    def delete_last(self):
        if self.is_empty():
            return
        if self.start.next is None:
             self.start=None
             return
     
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None

    
               
    def delete_item(self, data):
        if self.is_empty():
            return
        else:
            temp=self.start
            if temp.item==data:
                if temp.prev is None:
                    self.start=temp
                    if self.start is not None:
                        self.start.prev=None
                else:
                    temp.prev.next=temp.next
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                return
            temp=temp.next
 
          

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

                    
      
# Test the corrected implementation
mylist = DLL()
mylist.insert_at_start(10)  #
mylist.insert_at_last(12)   
s = mylist.search(12)       
mylist.insert_after(s, 20)  
        
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(12)
mylist.print_list() 
        






    



        