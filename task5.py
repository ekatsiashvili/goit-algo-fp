import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def dfs_traversal(node, visited, colors):
    if node is None:
        return

    visited.add(node)
    color = generate_color(len(visited))
    colors[node.id] = color

    dfs_traversal(node.left, visited, colors)
    dfs_traversal(node.right, visited, colors)

def bfs_traversal(root):
    visited = set()
    queue = [root]
    colors = {}

    while queue:
        node = queue.pop(0)
        if node:
            visited.add(node)
            color = generate_color(len(visited))
            colors[node.id] = color

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors

def generate_color(step):
    # Генерування кольору на основі кроку обходу
    red = int(25 + step * 200 / 1000)  # Червоний
    green = int(70 + step * 150 / 1000)  # Зелений
    blue = int(240 - step * 140 / 1000)  # Синій
    return "#{:02X}{:02X}{:02X}".format(red, green, blue)

def visualize_tree_traversal(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    plt.figure(figsize=(12, 8))

    # Візуалізація обходу у глибину
    dfs_colors = {}
    dfs_traversal(root, set(), dfs_colors)
    nx.draw(tree, pos=pos, node_color=[dfs_colors[node] for node in tree.nodes()], with_labels=True,
            arrows=False, node_size=2000, font_size=12, cmap=plt.cm.Blues, label='DFS Traversal')

    plt.title('Depth-First Search Traversal')
    plt.show()

    plt.figure(figsize=(12, 8))

    # Візуалізація обходу в ширину
    bfs_colors = bfs_traversal(root)
    nx.draw(tree, pos=pos, node_color=[bfs_colors[node] for node in tree.nodes()], with_labels=True,
            arrows=False, node_size=2000, font_size=12, cmap=plt.cm.Reds, label='BFS Traversal')

    plt.title('Breadth-First Search Traversal')
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходів дерева
visualize_tree_traversal(root)
