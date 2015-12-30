### Webservice for finding best route on a logistic mesh

##### The objective of this webservice is to load a logistic mesh and then return to the user the most cost-efficient path between two nodes of the mesh.

### Technologies used:
#### Language:
*  Python 2.7

#### Libs:
* ##### Flask

   Flask is a microframework for web development. It was chosen because it's very quick to make a webservice using it, requiring only a single file and a single route
* ##### Networkx

   NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It is used to generate graphs from the mesh points and to find the optimal path using Dijkstra's algorithm

* ##### json

   Standard python library to work with json data.

#### Data persistence:
* ##### JSON

  Initially my plan was to use MongoDB and the pymongo driver to store the logistic mesh data, but this would require testers to install MongoDB and populate the database from a json file. Besides that no data is being modified, so a database is not really required. I decided then to load data from a JSON file directly because that way very little code change will be needed in case I decide to use MongoDB, and because with JSON I can easily represent complex object structures and parse it with python.

#### Communication:

   The client call a get_best_route method via HTTP GET method, and the server returns the information in JSON format. JSON was chosen because it is a format that can be parsed easily with all popular languages, so this example can get scale.  

### Installation:

   To install the packages needed with pip, go to the project folder and type:  
    `pip install -r requirements.txt`

### Running:

  To run the webserver, run the script with `python main.py`.  
  The application will run on localhost, with port 5000  
  To request the optimal route make a HttpGet request on  `/get_best_route` with the following parameters:
  * map_name: Name of the map you want to use. (Available SP, RJ and RS)
  * origin: Node you want to leave from
  * destiny: Node you to to reach
  * autonomy: How many km/l you vehicle does
  * litre_value: Price of the litre of fuel

Exemple request:  
  http://localhost:5000/get_best_route?map_name=SP&origin=A&destiny=D&autonomy=10&litre_value=2.5

Returns:  
  {"path": ["A", "B", "D"], "cost": 6.25}

In case of some variable with undesireable value, the response will be a string with the specific error message
