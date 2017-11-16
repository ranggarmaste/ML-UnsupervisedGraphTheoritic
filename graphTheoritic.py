# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
from collections import defaultdict
from collections import OrderedDict

#Class to represent a graph
class Graph:
 
    def __init__(self, vertices, graph):
        self.V= vertices #No. of vertices
        self.graph = graph # default dictionary 
                                # to store graph
         
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's 
        # algorithm
    # graph theoritic is just a special kind of MST 
    # if MST stop when there are V-1 edge, graph theoritic stop at V-k
    def KruskalMST(self, k):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
            # Step 1:  Sort all the edges in non-decreasing 
                # order of their
                # weight.  If we are not allowed to change the 
                # given graph, we can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])
 
        parent = [] ; rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        # Number of edges to be taken is equal to V-1 
        while e < self.V -k:
 
            # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            # If including this edge does't cause cycle, 
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
            # Else discard the edge
 
        # print the contents of result[] to display the built MST
        print("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u,v,weight))
 

 
 
# load up data
def load_dataset():
  maxs = [0,0,0,0,0,0]
  mins = [10e9, 10e9, 10e9, 10e9, 10e9, 10e9]


  with open('CensusIncome/CencusIncome.data.txt', 'r') as f:
      for line in f:
          data = line.split(',')
          try:
              p = [int(data[0]), int(data[2]), int(data[4]), int(data[10]), int(data[11]), int(data[12])]
          except:
              print(data)

              
          for i in range(len(p)):
              if maxs[i] < p[i]:
                  maxs[i] = p[i]
              if mins[i] > p[i]:
                  mins[i] = p[i]

  dataset = []
  with open('CensusIncome/CencusIncome.data.txt', 'r') as f:
      count = 0
      for line in f:        
          data = line.split(',')
          try:
              p = [int(data[0]), int(data[2]), int(data[4]), int(data[10]), int(data[11]), int(data[12])]
              for i in range(len(p)):
                  p[i] = p[i] / (maxs[i] - mins[i])
              dataset.append(p)
          except:
              print(data)
  return dataset
  
# Driver code
dataset = load_dataset()

attr_count = len(dataset[0])
dataset_dimension = len(dataset)


min_set = []
for i in range(dataset_dimension):
    for k in range(i, dataset_dimension, 1):
        sumsqr = 0
        for q in range(attr_count):
            t = dataset[i][q] - dataset[k][q]
            sumsqr += t * t
        
        min_set.append([i,k,sumsqr])
        if len(min_set) > 1000000:
          print("cut ", i, k)
          smin_set = sorted(min_set,key=lambda item: item[2])
          min_set = smin_set[:dataset_dimension]

g = Graph(dataset_dimension, min_set)
          
print("Start Kruskal")

g.KruskalMST()
 
#This code is contributed by Neelam Yadav
