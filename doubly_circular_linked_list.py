class Node:
    def __init__(self, item=None, prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class DCLL:
    def __init__(self, start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            n.prev.next=n
            self.start.prev=n
    
    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp !=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,temp, data):
        if temp is not None:
            n=Node(data)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n

    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp=temp.next
            while temp is not self.start:
                print(temp.item, end=' ')
                temp=temp.next

    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
            

    def delete_last(self):
         if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev

    def delete_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next

                

        



         


    
        

        

            
        
    
        
        
    
    
                       
                    

                   
            

                
            

    
              

        



    
    



cll=DCLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
# cll.insert_at_last(40)
# cll.insert_after(cll.search(10),50)
# for x in cll:
#     print(x,end=" ")
# print()
# cll.delete_first()
# cll.delete_last()
# cll.delete_item(30)
cll.print_list()
            

          
    

    
    
        

                
        


                      


                
