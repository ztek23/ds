class Graph :
  def __init__(self, n):
      self.n = n
      self.adjacent = [[]for i in range(n)]

  def create_edge(self,x,y):
      self.adjacent[x-1].append(y-1)
      self.adjacent[y-1].append(x-1)

  def dfs_app(self,source,visited,result):
      result.append(source)
      visited[source] = True
      for i in self.adjacent[source]:
          if visited[i] == False:
              self.dfs_app(i,visited,result)

  def dfs(self,source):
      visited = [False]*self.n
      res = []
      self.dfs_app(source,visited,res)
      return res

g = Graph(6)
g.create_edge(2,5)
g.create_edge(2,4)
g.create_edge(1,2)
g.create_edge(3,1)
g.create_edge(5,1)

result = g.dfs(1)
print(result)
