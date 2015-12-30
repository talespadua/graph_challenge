### Webservice for finding best route on a logistic mesh

##### The objective of this webservice is to load a logistic mesh and then return to the user the most cost-efficient path between two nodes of the mesh.

### Technologies used:
#### Language:
*  Python 2.7

#### Libs:
* ##### Flask

   Flask is a microframework for web development. It was chosen because it's very quick to make a webservice using it, requiring only a single file and a single route
* ##### Networkx

   NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It is used to generate graphs from the mesh points given.

* ##### json

   Standard python library to work with json data.

#### Data persistence:
* ##### JSON

  Initially my plan was to use MongoDB and the pymongo driver to store the logistic mesh data, but this would require testers to install MongoDB and populate the database from a json file. Besides that no data is being modified, so a database is not really required. I decided then to load data from a JSON file directly because that way very little code change will be needed in case I need to use MongoDB, and because with JSON I can easily represent complex object structures and parse it with python.

#### Communication:

   The client call a get_best_route method via HTTP GET method, and the server returns the information in JSON format. JSON was chosen because it is a format that can be parsed easily with all popular languages, so this example can get scale.  

### Installation:

   To install the packages needed with pip, go to the project folder and type:  
    `pip install -r requirements.txt`

### Running:

  To run the webserver, run the script with `python main.py`.  
  The application will run on localhost, with port 5000
