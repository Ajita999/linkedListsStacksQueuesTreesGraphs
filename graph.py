    
class Graph():
  def __init__(self):
    self.total_nodes = 0
    self.adjacent_list = {}
    

  def addNode(self, node):
    self.adjacent_list[node] = []
    self.total_nodes +=1

   
  def addVertex(self, node1, node2):
    if node1 not in self.adjacent_list or node2 not in self.adjacent_list:
      return False
      
    else:
      self.adjacent_list[node1].append(node2)
      self.adjacent_list[node2].append(node1)
      
      

  def showConnections(self):
    print(self.adjacent_list)
          
        
    
      
graph = Graph()
graph.addNode(9)
graph.addNode(20)
graph.addNode(7)
graph.addNode(8)
graph.addVertex(8,7)
graph.addVertex(8,20)
graph.addVertex(9,20)
graph.addVertex(9,7)

graph.showConnections()





    