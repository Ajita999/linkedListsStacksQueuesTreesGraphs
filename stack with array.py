
class Stack():
  def __init__(self):
    self.stack = []

  def peek(self):
    return self.stack[len(self.stack)-1]

  def push(self, value):    
    self.stack.append(value)


  def pop(self):
    self.stack.pop()


  def showStack(self):
    return self.stack
      
      
      
      

myStack = Stack()
myStack.push("Discord")
myStack.push("Google")
myStack.push("Meta")
myStack.pop()
print(myStack.peek())
print(myStack.showStack())

    