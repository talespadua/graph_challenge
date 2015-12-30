from flask import Flask, request
import networkx as nx
import json

#
# class
def calculate_cost(distance, autonomy, litre_value):
    cost = (distance/autonomy) * litre_value


def get_best_way(origin, destiny):
    pass

app = Flask(__name__)

G = nx.Graph()

with open('maps.json') as json_file:
    map = json.load(json_file)


for points in map[0]['routes']:
    print points
    G.add_edge(points['origin'], points['destiny'], weight=float(points['distance']))

print nx.dijkstra_path(G, 'A', 'D')


@app.route('/get_best_route')
def index():
    map = request.args.get('map')
    origin = request.args.get('origin')
    destiny = request.args.get('destiny')
    autonomy = request.args.get('autonomy')
    litre_value = request.args.get('litre_value')
    print map, origin, destiny, autonomy, litre_value


app.run(debug=True)