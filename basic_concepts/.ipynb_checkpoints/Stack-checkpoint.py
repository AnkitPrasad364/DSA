'''Stack Data Structure - Overview

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle, meaning the last element added to the stack is the first one to be removed.

Key Operations:
	1.	Push(X): Adds an element X to the top of the stack.
	2.	Pop(): Removes and returns the top element from the stack.
	3.	Peek() / Top(): Returns the top element without removing it.
	4.	isEmpty(): Checks if the stack is empty.
	5.	Size(): Returns the number of elements in the stack.

Implementation Methods:
	•	Using Arrays/List (Fixed or dynamic size)
	•	Using Linked List (Dynamic memory allocation)

Time Complexity:
	•	Push, Pop, Peek → O(1) (Constant time)
	•	Searching for an element → O(n) (Linear time)

Real-World Applications:
	•	Undo/Redo operations in editors.
	•	Browser back/forward history.
	•	Expression evaluation (postfix, prefix, infix conversion).
	•	Function call stack (recursion handling).
'''
#stack linked list implementation
class Node:
    def __init__(self.value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        return self.top==None
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
    def peek(self):
        if(self.isEmpty()):
            return 'Stack Empty'
        else:
            return self.top.data
    def pop(self):
        if(self.isEmpty()):
            return 'Stack Empty'
        else:
            self.top=self.top.next
    def traverse(self):
        temp=self.top
        while temp!=None:
            print(temp.data)
            temp=temp.next
    #reversal of string using a stack
    def reverse_string(text):
        s=Stack()
        for i in text:
            s.push(i)
        res=''
        while(not s.isEmpty()):
            res+=s.pop()
        print(res)
    def text_editor(text,pattern):
        u=Stack()
        r=Stack()
        for i in text:
            u=push(i)
        for i in pattern:
            if i=='u':
                data=u.pop()
                r.push(data)
            else:
                data=r.pop()
                u.push(data)
        res=''
        while(not u.isEmpty()):
            res=u.pop()+res
    #celebrity problem Stack
    '''you are given a n*n matrix and you have to return a value which should be between 1 and n
    n  not inclusive.And there is possibility of 0 celeb but it's not possible to have more than one celeb
    '''
    
 