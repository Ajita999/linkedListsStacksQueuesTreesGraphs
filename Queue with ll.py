class Node:
  def __init__(self,value):
    self.node = {
      "value":value,
      "next": None
    }

  def get(self):
    return self.node
    
class Queue():
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    return self.first

  def enqueue(self, value):    
    node = Node(value)
    new_node = node.get()
    
    if self.length == 0:
      self.last = new_node
      self.first = new_node
    else:
      self.last['next'] = new_node
      self.last = new_node
    self.length +=1


  def dequeue(self):
    if not self.first:
      return 
    if self.first == self.last:
      self.first = None
      self.last = None
      return
    self.first = self.first['next']
    self.length -=1
      
      
      
      

myStack = Queue()
myStack.enqueue("Discord")
myStack.enqueue("Google")
myStack.enqueue("Meta")
myStack.dequeue()
print(myStack.peek())

    