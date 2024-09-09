import networkx as nx
import matplotlib.pyplot as plt
import folium

def visualize_graph(G, title):
    plt.figure(figsize=(15, 8))
    pos = nx.get_node_attributes(G, 'pos')
    node_labels = nx.get_node_attributes(G, 'name')
    node_colours = list(nx.get_node_attributes(G, 'colour').values())
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=100, node_color=node_colours, font_size=8)
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.7)
    plt.title(title)
    plt.show()

def create_folium_map(G, zoom_start=12):
    positions = nx.get_node_attributes(G, 'pos')
    node_labels = nx.get_node_attributes(G, 'name')
    node_colors = nx.get_node_attributes(G, 'colour')

    if not positions:
        raise ValueError("Graph nodes must contain a 'pos' attribute with (longitude, latitude).")

    latitudes = [pos[1] for pos in positions.values()]
    longitudes = [pos[0] for pos in positions.values()]

    center_lat = sum(latitudes) / len(latitudes)
    center_lon = sum(longitudes) / len(longitudes)

    folium_map = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_start)

    for node, pos in positions.items():
        node_name = node_labels.get(node, f"Node {node}")
        color = node_colors.get(node, 'blue')
        folium.CircleMarker(location=[pos[1], pos[0]], radius=6, color=color, fill=True, fill_color=color, tooltip=node_name).add_to(folium_map)

    for u, v in G.edges():
        if u in positions and v in positions:
            folium.PolyLine(locations=[(positions[u][1], positions[u][0]), (positions[v][1], positions[v][0])], color='blue', weight=2).add_to(folium_map)

    return folium_map
