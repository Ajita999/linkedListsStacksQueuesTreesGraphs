class Node:
  def __init__(self,value):
    self = {
      "value":value,
      "next": None
    }
    return self
    
class DoublyLinkedList:
  def __init__(self, value):
    self.head = {
      "value": value,
      "next": None,
      "previous":None
    }
    self.tail = self.head
    self.length = 1

  def append(self, value):
    new_node = {
      "value": value,
      "next": None,
      "previous": None
    }
    self.tail['next'] = new_node
    new_node['previous'] = self.tail
    self.tail = new_node
    self.length=self.length+1

  def prepend(self, value):
    new_node = {
      "value": value,
      "next": self.head,
      "previous":None
    }
    self.head = new_node
    self.length +=1

  def printList(self):
    list = []
    current_node = self.head
    while(current_node != None):
      list.append(current_node['value'])
      current_node = current_node['next']
    return list

  def insert(self,index,value):

    if index >=self.length:
      self.append(value)
      return
    
    if index==0:
      self.prepend(value)
      return 

    new_node = {
      "value": value,
      "next": None,
      "previous": None
    }
      
    current_node = self.head
    for i in range(0,index+1):
      if i == index-1:
        new_node['next'] = current_node['next']
        new_node['previous'] = current_node
        current_node['next'] = new_node
        self.length +=1
        return
        
      else:
        current_node = current_node['next']
    return

  def remove(self,index):
    if index>self.length:
      print("Out of Index")
      return
    
    if index==0:
      self.head = self.head['next']
      self.head['previous'] = None
      self.length -= 1
      return
      
    current_node = self.head
    for i in range(0,index+1):
      if i == index-1:
        current_node['next'] = current_node['next']['next']
        current_node['next']['previous'] = current_node
        self.length -= 1
        return
      else:
        current_node = current_node['next']
      
      

myLinkedList = DoublyLinkedList(10)
print(myLinkedList)
myLinkedList.append(5)
myLinkedList.append(18)
myLinkedList.prepend(-7)
myLinkedList.append(98)
myLinkedList.insert(2,35)
myLinkedList.insert(0,73)
myLinkedList.insert(10,90)
print("List", myLinkedList.printList())
myLinkedList.remove(3)
print("Head",myLinkedList.head)
print("Tail",myLinkedList.tail)
print("Length",myLinkedList.length)
print("List", myLinkedList.printList())
    