class Node:
    """Class to represent a node in the linked list."""
    
    def __init__(self, value):
        self.data = value  # Store the node value
        self.next = None  # Pointer to the next node (initially None)


class LinkedList:
    """Class to represent a singly linked list."""
    
    def __init__(self):
        self.head = None  # Initially, the linked list is empty
        self.n = 0  # Count of nodes in the linked list

    def __len__(self):
        """Returns the number of nodes in the linked list."""
        return self.n

    def insert_head(self, value):
        """Inserts a new node at the head (beginning) of the linked list."""
        new_node = Node(value)  # Create a new node with the given value
        new_node.next = self.head  # Point new node to current head
        self.head = new_node  # Update head to the new node
        self.n += 1  # Increment node count

    def __str__(self):
        """Returns a string representation of the linked list."""
        curr = self.head
        result = ''
        while curr is not None:
            result += str(curr.data) + '->'  # Append current node's data to the string
            curr = curr.next  # Move to the next node
        return result[:-2] if result else result  # Remove the last '->' if the list is not empty

    def append(self, value):
        """Inserts a new node at the end (tail) of the linked list."""
        new_node = Node(value)  # Create a new node
        if self.head is None:  # If the list is empty, make new node the head
            self.head = new_node
            self.n += 1  # Increment node count
            return
        curr = self.head  # Start from the head
        while curr.next is not None:  # Traverse to the last node
            curr = curr.next
        curr.next = new_node  # Link the last node to the new node
        self.n += 1  # Increment node count

    def insert_after(self, after, value):
        """Inserts a new node after a node containing the given 'after' value."""
        new_node = Node(value)  # Create a new node
        curr = self.head  # Start from the head
        while curr is not None:
            if curr.data == after:  # Find the node with the given value
                break
            curr = curr.next

        if curr is not None:  # If the node is found
            new_node.next = curr.next  # Link new node to the next node
            curr.next = new_node  # Link current node to the new node
            self.n += 1  # Increment node count
        else:
            return "Item not found"  # Return message if the value is not found

    def clear(self):
        """Clears the entire linked list."""
        self.head = None
        self.n = 0

    def delete_head(self):
        """Removes the head (first node) of the linked list."""
        if self.head is None:
            return 'Empty LL'
        self.head = self.head.next  # Move head to the next node
        self.n -= 1  # Decrement node count

    def pop(self):
        """Removes the last node from the linked list."""
        if self.head is None:
            return 'Empty LL'

        curr = self.head
        # If there is only one item in the linked list
        if curr.next is None:
            self.delete_head()
            return
        
        while curr.next.next is not None:  # Traverse to the second last node
            curr = curr.next
        curr.next = None  # Remove the last node
        self.n -= 1  # Decrement node count

    def remove(self, value):
        """Removes a node with the given value from the linked list."""
        if self.head is None:
            return 'Empty LL'
        
        if self.head.data == value:
            # If the head node is to be removed
            return self.delete_head()

        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                break
            curr = curr.next

        # Two cases: item found or not found
        if curr.next is None:
            return 'Not found'
        else:
            curr.next = curr.next.next  # Skip over the node to be deleted
            self.n -= 1  # Decrement node count

    def search(self, item):
        """Finds the index of a specific value in the linked list, if present."""
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return 'Not found'

    def __getitem__(self, index):
        """Retrieves the value at the given index in the linked list."""
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return 'Index error'

    def replace_max(self, value):
        """Replaces the maximum value in the linked list with the given value."""
        if self.head is None:
            return 'Empty LL'

        temp = self.head
        max_node = temp  # Keep track of the node with max value

        while temp is not None:
            if temp.data > max_node.data:
                max_node = temp
            temp = temp.next
        
        max_node.data = value  # Replace the max node's value

    def sum_odd_nodes(self):
        """Calculates the sum of values at odd indices in the linked list."""
        temp = self.head
        counter = 0
        res = 0
        while temp is not None:
            if counter % 2 == 0:  # Check for odd index (0-based indexing)
                res += temp.data
            counter += 1
            temp = temp.next
        print(res)  # Print the sum of odd-indexed nodes

    def reverse(self):
        """Reverses the linked list in place."""
        prev_node = None
        curr_node = self.head  # Start from the head

        while curr_node is not None:
            next_node = curr_node.next  # Store reference to the next node
            curr_node.next = prev_node  # Reverse the link
            prev_node = curr_node  # Move prev_node forward
            curr_node = next_node  # Move curr_node forward
        
        self.head = prev_node  # Update head to new front of the list


# Example usage of the LinkedList class
L = LinkedList()
L.insert_head(1)   # Insert 1 at the head
L.insert_head(4)   # Insert 4 at the head
L.insert_head(10)  # Insert 10 at the head
L.insert_head(50)  # Insert 50 at the head
L.append(555)      # Append 555 at the end
L.insert_after(100, 123)  # Insert 123 after the node containing 1
L.remove(1)
L.remove(1232)
print(L)  # Print the linked list