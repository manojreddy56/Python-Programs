class Graph:
    def __init__(self):
        self.g = dict()
    
    def insert_vertex(self, vertex):
        self.g[vertex] = []
        
    def add_edge(self, start, end, wt):
        l = (end, wt)
        self.g[start].append(l)
        
    def delete_edge(self, start, end, wt):
        for edge in self.g[start]:
            if edge == (end, wt):
                ind = self.g[start].index(edge)
                del self.g[start][ind]
                
    def remove_vertex(self, vertex):
        del self.g[vertex]
        for v in self.g:
            for e in self.g[v]:
                if vertex in e:
                    self.g[v].remove(e)
                    
    def dfs(self, vertex):
        stack = [vertex]
        visited = [vertex]
        
        while len(stack) != 0:
            top = stack[-1]
            count = 0
            for adj_v in self.g[top]:
                if adj_v[0] not in visited:
                    stack.append(adj_v[0])
                    visited.append(adj_v[0])
                    count += 1
                    break
            if count == 0:
                stack.pop()
                
        return visited
    
    def bfs(self, vertex):
        queue = [vertex]
        visited = [vertex]
        
        while(len(queue) != 0):
            current = queue[0]
            count = 0
            for adj_v in self.g[current]:
                if adj_v[0] not in visited:
                    visited.append(adj_v[0])
                    queue.append(adj_v[0])
                    count += 1
                    break
            if count == 0:
                queue.pop(0)
        return visited
                
    
g1 = Graph()
g1.insert_vertex("A")
g1.insert_vertex("B")
g1.insert_vertex("C")
g1.insert_vertex("D")
g1.add_edge("A", "B", 4)
g1.add_edge("B", "A", 4)
g1.add_edge("B", "C", 5)
g1.add_edge("B", "D", 3)
g1.add_edge("C", "B", 5)
g1.add_edge("C", "D", 2)
g1.add_edge("D", "C", 2)
g1.add_edge("D", "B", 3)
#g1.delete_edge("B", "A", 4)
#g1.remove_vertex("B")

print(g1.g)

print(g1.dfs("A"))
print(g1.bfs("A"))