from flask import Flask, request
import networkx as nx
import json


# Mesh objects stores the name of the logistic mesh
class Mesh:
    def __init__(self, name):
        self.name = name
        self.graph = None

    def add_graph(self, graph):
        self.graph = graph


# Calculate the cost of the trip based on distance and vehicle efficiency
def calculate_cost(distance, autonomy, litre_value):
    cost = (distance/autonomy) * litre_value
    return cost


# Return the graph of the specific mesh name in the mesh_list
def get_mesh(mesh_list, name):
    for m in mesh_list:
        if m.name == name:
            return m.graph
    return None

# Init Flask app
app = Flask(__name__)
# List of Mesh objects
logistic_meshs = []
# Load maps.json file
with open('maps.json') as json_file:
    map_list = json.load(json_file)

# Load a Graph for each
for map in map_list:
    mesh = Mesh(map['map_name'])
    graph = nx.Graph()
    for points in map['routes']:
        graph.add_edge(points['origin'], points['destiny'], weight=float(points['distance']))
    mesh.add_graph(graph)
    logistic_meshs.append(mesh)


@app.route('/get_best_route')
def index():
    map_name = request.args.get('map_name')
    origin = request.args.get('origin')
    destiny = request.args.get('destiny')
    autonomy = request.args.get('autonomy')
    litre_value = request.args.get('litre_value')

    graph = get_mesh(logistic_meshs, map_name)
    # Error treatment
    if graph is None:
        return "The map with name \'{0}\' doesn't exists".format(map_name)
    if origin not in graph:
        return "this mesh doesn't have the origin node \'{0}\'".format(origin)
    if destiny not in graph:
        return "this mesh doesn't have the destiny node \'{0}\'".format(destiny)
    if autonomy is None:
        return "Missing autonomy"
    if autonomy is None:
        return "Missing autonomy"
    if float(autonomy) < 0 or float(litre_value) < 0:
        return "Autonomy and litre value must be positive numbers"

    optimal_path = nx.dijkstra_path(graph, origin, destiny)
    optimal_path_lenght = nx.dijkstra_path_length(graph, origin, destiny)

    cost = calculate_cost(optimal_path_lenght, float(autonomy), float(litre_value))

    data = dict()
    data['path'] = optimal_path
    data['cost'] = cost

    json_response = json.dumps(data)

    return json_response


app.run(debug=True)
