class Node:
  def __init__(self,value):
    self.node = {
      "value":value,
      "left": None,
      "right": None
    }

    
class BinarySearchTree():
  def __init__(self):
    self.root = None
    

  def insert(self,value):
    if self.root == None:
      new_node = Node(value)
      self.root = new_node.node

    else:
      temp_root = self.root
      while(1):
        
        if value >= temp_root['value']:
          if temp_root['right'] == None:
            new_node = Node(value)
            temp_root['right'] = new_node.node
            break
          else:
            temp_root = temp_root['right']
  
        else:
          if temp_root['left'] == None:
            new_node = Node(value)
            temp_root['left'] = new_node.node
            break
          else:
            temp_root = temp_root['left']

    return self.root

  def lookup(self, value):
    temp_root = self.root

    while(temp_root is not None):
      if temp_root['value'] == value:
        return temp_root

      elif temp_root['value'] > value:
        temp_root = temp_root['left']
      else:
        temp_root = temp_root['right']

    return "Not Found"

  def remove(self, value):
    if self.root is None:
      return False
      
    temp_root = self.root
    parent = None

    while(temp_root is not None):
      if temp_root['value'] == value:

        if temp_root['right'] is None:
          if parent is None:
            self.root = temp_root['left']
          else:

            if temp_root['value'] < parent['value']:
              parent['left'] = temp_root['left']
            elif temp_root['value'] > parent['value']:
              parent['right'] = temp_root['right']
          
          
      elif temp_root['value'] > value:
        parent = temp_root
        temp_root = temp_root['left']
        
      else:
        parent = temp_root
        temp_root = temp_root['right']

    return "Not Found"
      

      
          
        
    
      
bst = BinarySearchTree()
bst.insert(9)
bst.insert(20)
bst.insert(7)
bst.insert(8)
print(bst.lookup(2))
bst.remove(7)






    