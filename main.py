from flask import Flask, request


def calculate_cost(distance, autonomy, litre_value):
    cost = (distance/autonomy) * litre_value


def get_best_way(origin, destiny):
    pass

app = Flask(__name__)

@app.route('/get_best_route')
def index():
    map = request.args.get('map')
    origin = request.args.get('origin')
    destiny = request.args.get('destiny')
    autonomy = request.args.get('autonomy')
    litre_value = request.args.get('litre_value')
    print map, origin, destiny, autonomy, litre_value

app.run(debug=True)