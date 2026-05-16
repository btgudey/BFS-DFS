# Search and Optimization Algorithms using Python

This project demonstrates the implementation of two fundamental Artificial Intelligence search algorithms:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)

The programs are implemented using Python and are designed to find a path from an initial node to a goal node in a graph.

---

# Objectives

- Understand uninformed search techniques in Artificial Intelligence
- Implement Breadth First Search (BFS)
- Implement Depth First Search (DFS)
- Display the search path from the start node to the goal node
- Compare BFS and DFS traversal methods

---

# Technologies Used

- Python 3
- Collections Module (`deque`)

---

# Graph Representation

The graph is represented using an adjacency list.

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
