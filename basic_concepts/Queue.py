# Node class to represent each element in the queue
class Node:
    def __init__(self, value):
        self.data = value  # Stores the data value
        self.next = None   # Pointer to the next node (initially None)

# Queue class implementing a linked list-based queue
class Queue:
    def __init__(self):
        self.front = None  # Points to the front element of the queue
        self.rear = None   # Points to the rear element of the queue

    # Method to add an element to the queue (enqueue operation)
    def Enqueue(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.rear is None:   # If queue is empty, both front and rear point to the new node
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Link the last node to the new node
            self.rear = new_node       # Update the rear pointer to the new node

    # Method to remove an element from the front of the queue (dequeue operation)
    def Dequeue(self):
        if self.front is None:  # If the queue is empty, return a message
            return "Queue is Empty"
        temp = self.front       # Store the current front node
        self.front = self.front.next  # Move front to the next node
        if self.front is None:  # If queue becomes empty, reset rear to None
            self.rear = None
        return temp.data  # Return the dequeued value

    # Method to traverse and print all elements in the queue
    def traverse(self):
        temp = self.front
        while temp is not None:  # Traverse till the end of the queue
            print(temp.data, end=" ")  # Print each node's value
            temp = temp.next
        print()  # Newline for better readability

    # Method to check if the queue is empty
    def is_empty(self):
        return self.front is None  # Returns True if front is None (queue is empty)

    # Method to return the size of the queue
    def size(self):
        temp = self.front
        counter = 0
        while temp is not None:  # Traverse the queue and count nodes
            counter += 1
            temp = temp.next
        return counter  # Return the total count of elements in the queue

    # Method to return the front item without removing it
    def front_item(self):
        if self.front is None:  # If queue is empty, return message
            return 'Empty'
        return self.front.data  # Return the front element's data

    # Method to return the rear item without removing it
    def rear_item(self):
        if self.rear is None:  # If queue is empty, return message
            return 'Empty'
        return self.rear.data  # Return the rear element's data

# Creating a queue instance
q = Queue()  # Initialize an empty queue

print(q.is_empty())  # Check if queue is empty (Expected: True)

# Enqueue operations (adding elements to the queue)
q.Enqueue(10)  # Adding 10
q.Enqueue(20)  # Adding 20
q.Enqueue(30)  # Adding 30
q.Enqueue(40)  # Adding 40
q.Enqueue(50)  # Adding 50
q.Enqueue(60)  # Adding 60

q.traverse()  # Print the current queue elements (Expected: 10 20 30 40 50 60)

print("Dequeued:", q.Dequeue())  # Dequeue the front element (Expected: 10)
q.traverse()  # Print queue after dequeuing one element (Expected: 20 30 40 50 60)

print("Queue is empty:", q.is_empty())  # Check if queue is empty (Expected: False)
print("Queue size:", q.size())  # Get the size of the queue (Expected: 5)
print("Front item:", q.front_item())  # Get the front item (Expected: 20)
print("Rear item:", q.rear_item())  # Get the rear item (Expected: 60)