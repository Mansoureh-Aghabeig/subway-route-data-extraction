import requests

def extract_osm_geodata(query):
    """
    Extracts geodata from OpenStreetMap using the Overpass API.

    Parameters:
    query (str): The Overpass API query string to execute.

    Returns:
    dict: GeoJSON data retrieved by the query.
    """
    overpass_url = "https://lz4.overpass-api.de/api/interpreter"
    params = {'data': query}
    response = requests.get(overpass_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
