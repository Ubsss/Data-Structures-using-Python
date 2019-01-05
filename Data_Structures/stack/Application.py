# from stack.Stack import Stack
from Data_Structures.stack.Stack_Using_Array import Stack

myStack = Stack()

myStack.push(656)
myStack.push(745)
myStack.push(232)

myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.traverse()
print(myStack.stack_size())

