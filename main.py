from flask import Flask, request
import networkx as nx
import json

#
# class
def calculate_cost(distance, autonomy, litre_value):
    cost = (distance/autonomy) * litre_value
    return cost


def get_best_way(origin, destiny):
    pass

app = Flask(__name__)

G = nx.Graph()

with open('maps.json') as json_file:
    map = json.load(json_file)


for points in map[0]['routes']:
    G.add_edge(points['origin'], points['destiny'], weight=float(points['distance']))

optimal_path = nx.dijkstra_path(G, 'A', 'D')
optimal_path_lenght = nx.dijkstra_path_length(G, 'A', 'D')

print optimal_path, optimal_path_lenght

@app.route('/get_best_route')
def index():
    map = request.args.get('map')
    origin = request.args.get('origin')
    destiny = request.args.get('destiny')
    autonomy = float(request.args.get('autonomy'))
    litre_value = float(request.args.get('litre_value'))

    optimal_path = nx.dijkstra_path(G, origin, destiny)
    optimal_path_lenght = nx.dijkstra_path_length(G, origin, destiny)

    cost = calculate_cost(optimal_path_lenght, autonomy, litre_value)

    data = {}
    data['path'] = optimal_path
    data['cost'] = cost

    json_response = json.dumps(data)

    return json_response


app.run(debug=True)