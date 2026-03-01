import pytest
from src.data_structures import Stack, Queue

def test_stack():
    stack = Stack()
    
    # Test empty stack
    assert stack.is_empty() == True
    assert stack.size() == 0
    
    # Test push
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.is_empty() == False
    
    # Test peek
    assert stack.peek() == 3
    assert stack.size() == 3  # Peek shouldn't remove item
    
    # Test pop
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True
    
    # Test pop from empty stack
    with pytest.raises(IndexError):
        stack.pop()

def test_queue():
    queue = Queue()
    
    # Test empty queue
    assert queue.is_empty() == True
    assert queue.size() == 0
    
    # Test enqueue
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.size() == 3
    assert queue.is_empty() == False
    
    # Test dequeue (FIFO)
    assert queue.dequeue() == 'a'
    assert queue.size() == 2
    assert queue.dequeue() == 'b'
    assert queue.dequeue() == 'c'
    assert queue.is_empty() == True
    
    # Test dequeue from empty queue
    with pytest.raises(IndexError):
        queue.dequeue()
