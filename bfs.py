from collections import deque

# Define the graph using adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start, goal):
    """
    Breadth First Search Algorithm

    Parameters:
    graph : dictionary
        Graph represented as adjacency list
    start : string
        Starting node
    goal : string
        Goal node

    Returns:
    list
        Shortest path from start node to goal node
    """

    # Queue for BFS traversal
    queue = deque([start])

    # Set to keep track of visited nodes
    visited = set([start])

    # Dictionary for storing parent nodes
    parent = {start: None}

    # Continue traversal until queue becomes empty
    while queue:

        # Remove node from front of queue
        current = queue.popleft()

        # Check if goal node is reached
        if current == goal:

            # Reconstruct path
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            # Reverse path to obtain correct order
            path.reverse()

            return path

        # Explore neighboring nodes
        for neighbor in graph[current]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

                # Store parent relationship
                parent[neighbor] = current

    return None


# Main Program
if __name__ == "__main__":

    start_node = 'A'
    goal_node = 'F'

    print("BREADTH FIRST SEARCH (BFS)")
    print("==========================")
    print("Initial Node :", start_node)
    print("Goal Node    :", goal_node)
    print()

    path = bfs(graph, start_node, goal_node)

    if path:
        print("Search Path Found:")
        print(" -> ".join(path))
    else:
        print("No path found")