# src/main.py
from src import extract_osm_geodata, extract_route_elements, extract_node_elements, create_route_graph, create_folium_map

def main():
    query = """
    [out:json];
    area[name="Berlin"]->.searchArea;
    relation["route"~"subway"](area.searchArea);
    out meta;
    >;
    out body;
    """

    subway_data = extract_osm_geodata(query)
    route_elements = extract_route_elements(subway_data)
    node_elements = extract_node_elements(subway_data)
    graph = create_route_graph(route_elements, node_elements)

    map = create_folium_map(graph, zoom_start=12)
    map.show_in_browser()

if __name__ == "__main__":
    main()
