import networkx as nx

def extract_route_elements(osm_data):
    route_elements = [element for element in osm_data['elements'] if 'tags' in element and 'route' in element['tags']]
    return route_elements

def extract_node_elements(osm_data):
    node_elements = {element['id']: element for element in osm_data['elements'] if element['type'] == 'node'}
    return node_elements

def create_route_graph(route_elements, node_elements):
    G = nx.Graph()
    for route in route_elements:
        stop_nodes = [member for member in route['members'] if 'stop' in member['role']]

        for node in stop_nodes:
            ref = node['ref']
            if ref in node_elements:
                node_data = node_elements[ref]
                name = node_data['tags'].get('name', str(ref))
                colour = route['tags'].get('colour', '#808080')
                G.add_node(ref, pos=(node_data['lon'], node_data['lat']), name=name, colour=colour)

        for i in range(len(stop_nodes) - 1):
            G.add_edge(stop_nodes[i]['ref'], stop_nodes[i + 1]['ref'])
    return G
