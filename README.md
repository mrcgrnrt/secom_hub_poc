# SECoM Hub Registry

**THE ACTUAL IMPLEMENTATION IS FULL OF BAD CODE, DOES NOT FOLLOW BEST PRACTICES AND IS NOT MEANT FOR ANY REAL USE. THE ONLY PURPOSE IS EDUCATIONAL USE.**

The SECoM Hub Registry is the central component of the SECoM Hub. It provides a management frontend to show known SECoM Nodes and their status and to edit their configuration. 

## Getting started

The SECoM Hub Registry is build from three main components:

* the database that stores the metadata and the current state of the SECoM Nodes
* the backend API that provides a standardized interface to the database
* the frontend that provides a web interface for the user

### database

* MongoDB is used as the database
* you can use the provided docker compose file to start a MongoDB instance and the management frontend
* to populate the database the script `db_utils/populate_mongodb.py` can be used
  * change into the `db_utils` directory
  * create a virtual environment and install the requirements (`python -m venv venv`, `. ./venv/bin/activate`, `pip install -r requirements.txt`)
  * run the script with `python populate_mongodb.py --server_url 'mongodb://root:example@localhost:27017' --database_name 'secom-registry' --collection_name 'nodes' --store_path './nodes' --replace_existing False`

### backend

* the backend is implemented in Python using Flask
* to start the backend
  * change into the `api` directory
  * set up an environment (e.g. `python -m venv venv`, `. ./venv/bin/activate`, `pip install -r requirements.txt`) 
  * adapt `.env` according to your needs
  * start the server `python device_registry.py`

### frontend

 * the frontend is implemented in React
 * to start the frontend
   * change into the `ui` directory
   * install the dependencies (`npm install`)
   * adapt `.env` according to your needs
   * start the server `npm start`
 * be aware that the configuration (API endpooints,...) is hard coded at the moment
 * the ui design is based on the [Infineon Digital Design System](https://infineon.github.io/infineon-design-system-stencil/?path=/docs/setup-installation-about--development)
