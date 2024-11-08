import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Building edges
edges = [
    ('A', 'B', 2), ('A', 'C', 7),
    ('B', 'D', 1), ('B', 'E', 5),
    ('C', 'D', 3), ('C', 'F', 10),
    ('D', 'E', 6), ('D', 'F', 4),
    ('E', 'Z', 3), ('F', 'Z', 3)
]

G.add_weighted_edges_from(edges)

# original graph
position = nx.spring_layout(G)
plt.figure(figsize=(10, 6))
nx.draw(G, position, with_labels=True, node_color='green', node_size=800, font_size=20)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, position, edge_labels=labels)
plt.title("Original Graph")
plt.show(block=False)
plt.pause(2)
plt.close()

print("Using Prim's Algorithm to find MST.\n")

def prim_mst(graph, start_node):
    mst = []
    visited = set([start_node])
    edges = []

    # Adding edges from the start node to edges list
    for neighbor in graph[start_node]:
        weight = graph[start_node][neighbor]['weight']
        edges.append((weight, start_node, neighbor))

    # Sorting by weight
    edges.sort(key=lambda x: x[0])

    # visualization
    plt.figure(figsize=(10, 6))
    nx.draw(G, position, with_labels=True, node_color='pink', node_size=800, font_size=20)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, position, edge_labels=labels)

    while edges:
        # Edge with the smallest weight
        weight, frm, to = edges.pop(0)

        if to not in visited:
            # Adding the edge to the MST
            visited.add(to)
            mst.append((frm, to, weight))
            print(f"Added edge: {frm} - {to} ;; weight {weight}")

            # Draw the current MST step
            nx.draw_networkx_edges(G, position, edgelist=[(frm, to)], width=3.0, edge_color='yellow')
            plt.pause(1)

            # Adding all edges from the new node to edges list
            for neighbor in graph[to]:
                if neighbor not in visited:
                    weight = graph[to][neighbor]['weight']
                    edges.append((weight, to, neighbor))

            # Sort edges by weight again
            edges.sort(key=lambda x: x[0])

    plt.title("MST Creation")
    plt.show(block=False)
    plt.pause(2)
    plt.close()

    print("\nFinal MST:")
    for edge in mst:
        print(edge)
    return mst

# Running from node 'A'
mst = prim_mst(G, 'A')

# Depicting the final MST
mst_graph = nx.Graph()
mst_graph.add_weighted_edges_from(mst)

plt.figure(figsize=(10, 6))
nx.draw(mst_graph, position, with_labels=True, node_color='purple', node_size=800, font_size=20)
mst_labels = {(u, v): d['weight'] for u, v, d in mst_graph.edges(data=True)}
nx.draw_networkx_edge_labels(mst_graph, position, edge_labels=mst_labels)
plt.title("Final MST")
plt.show(block=False)
plt.pause(2)
plt.close()
