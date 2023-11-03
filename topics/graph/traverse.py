import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Create a simple graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Depth-First Search
print("DFS Traversal:")
visited_dfs = set()
dfs(G, 1, visited_dfs)

# Create a copy of the graph to visualize DFS traversal
G_dfs = G.copy()
pos = nx.spring_layout(G_dfs)
nx.draw(G_dfs, pos, with_labels=True, node_color='lightblue')
plt.title('DFS Traversal')
plt.show()

# Breadth-First Search
print("\nBFS Traversal:")
bfs(G, 1)

# Create a copy of the graph to visualize BFS traversal
G_bfs = G.copy()
pos = nx.spring_layout(G_bfs)
nx.draw(G_bfs, pos, with_labels=True, node_color='lightgreen')
plt.title('BFS Traversal')
plt.show()
