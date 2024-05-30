import networkx as nx
import matplotlib.pyplot as plt

def visualize_heap(heap):
    heap_graph = nx.Graph()
    positions = {}

    # Додавання вершин до графу
    for i, node in enumerate(heap):
        heap_graph.add_node(i, value=node)

    # Обчислення позицій вершин на основі їхніх індексів у купі
    max_level = (len(heap) - 1).bit_length()  # Знаходження максимального рівня купи
    for i, node in enumerate(heap):
        level = (i + 1).bit_length() - 1  # Обчислення рівня вершини
        x = (i + 1) * (1 / (2 ** level))  # Обчислення позиції по x
        y = max_level - level  # Обчислення позиції по y (звернення купи)
        positions[i] = (x, y)

    # Додавання ребер між вершинами купи
    for i, _ in enumerate(heap):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(heap):
            heap_graph.add_edge(i, left_child)
        if right_child < len(heap):
            heap_graph.add_edge(i, right_child)

    # Відображення графу
    plt.figure(figsize=(10, 6))
    nx.draw(heap_graph, pos=positions, with_labels=True, node_size=2000, node_color='skyblue', font_size=12)
    plt.title('Binary Heap Visualization')
    plt.show()

# Test
heap = [3, 5, 8, 10, 12, 6, 9]
visualize_heap(heap)
