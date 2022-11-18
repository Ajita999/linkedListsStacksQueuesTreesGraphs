class Node:
  def __init__(self,value):
    self.node = {
      "value":value,
      "next": None
    }

  def get(self):
    return self.node
    
class Stack():
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    return self.top

  def push(self, value):    
    node = Node(value)
    new_node = node.get()
    new_node['next'] = self.top
    if self.length == 0:
      self.bottom = new_node
    self.top = new_node
    self.length +=1


  def pop(self):
    if not self.top:
      return 
    if self.top == self.bottom:
      self.top = None
      self.bottom = None
      return
    self.top = self.top['next']
    self.length -=1
      
      
      
      

myStack = Stack()
myStack.push("Discord")
myStack.push("Google")
myStack.push("Meta")
myStack.pop()
print(myStack.peek())

    