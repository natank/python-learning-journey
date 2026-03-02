class Stack:
    """Simple stack implementation using list"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

class Queue:
    """Simple queue implementation using list"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    # Test data structures
    print("Stack testing:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack size: {stack.size()}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    
    print("\nQueue testing:")
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print(f"Queue size: {queue.size()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Queue size after dequeue: {queue.size()}")
