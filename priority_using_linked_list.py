class Node:
    def __init__(self, item, priority, next=None):
        self.item = item
        self.priority = priority  # Require valid priority
        self.next = next

class Priority:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data, priority):
        if priority is None:
            raise ValueError("Priority cannot be None")
        if not isinstance(priority, (int, float)):
            raise TypeError("Priority must be a number")
        
        n = Node(data, priority)
        if not self.start:  # Empty queue
            self.start = n
            self.item_count += 1
        elif priority < self.start.priority:  # Higher priority than start
            n.next = self.start
            self.start = n
            self.item_count += 1
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
            self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        value = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return value

    def size(self):
        return self.item_count  # Return 0 for empty queue

# Test code
d1 = Priority()
d1.push('akshay', 1)
d1.push(4, 6)
d1.push(2, 5)
d1.push(1, 4)
d1.push(1, 3)
d1.push(1, 2)
print(d1.pop())  # Output: akshay
print(d1.size())  # Output: 5

