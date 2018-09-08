import random
import time

def dfs(graph, start, goal):
  visited, stack = [],[start]
  while stack:
    vertex = stack.pop()
    if vertex == goal:
      return True
    if vertex not in visited:
      visited.append(vertex)
      stack.extend(graph[vertex] - set(visited))
  return False

def bfs(graph, start, goal):
  visited, queue = [],[start]
  while queue:
    vertex = queue.pop(0)
    if vertex == goal:
      return True
    if vertex not in visited:
      visited.append(vertex)
      queue.extend(graph[vertex] - set(visited))
  return False

vert = int(input("Enter the number of vertices: "))+1
max_edge = int(input("Enter the max number of edges per vertex: "))
search_numbers = int(input("How many random searches do you want to perform?: "))

nodes = set(range(1,vert))
g = {}
for node in nodes:
  g[node] = set(random.sample(nodes-{node},random.randint(0,max_edge)))
print("Graph Created...")

dfs_count = 0
bfs_count = 0

for i in range(search_numbers):
  s = random.randint(1,vert-1)
  goal = random.randint(1,vert-1)
  times = []
  print('--------------------------------')
  print('Start:',s,'Goal:',goal)
  start = time.time()
  print("DFS",dfs(g,s,goal))
  total = time.time() - start
  times.append(total)
  print("Time: ", total)
  start = time.time()
  print("BFS",bfs(g,s,goal))
  total = time.time() - start
  times.append(total)
  print("Time", total)
  if(times[0]<times[1]):
    print("DFS better")
    dfs_count += 1
  else:
    print("BFS better")
    bfs_count += 1
print('--------------------------------')
print('Total: ','DFS',dfs_count,'BFS',bfs_count)
