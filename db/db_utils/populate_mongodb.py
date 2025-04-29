"""
This script populates a MongoDB collection with JSON data from a specified directory.
The script connects to a MongoDB server, reads JSON files from a given directory, and inserts or updates
documents in the specified collection. It provides options to replace existing documents or skip updates
for existing entries.
Modules:
    - pymongo: Used to connect to and interact with MongoDB.
    - pathlib: Used to handle file paths and iterate over JSON files in the directory.
    - json: Used to parse JSON files.
    - logging: Used to log information and errors.
    - argparse: Used to parse command-line arguments.
Command-line Arguments:
    --server_url: The URL of the MongoDB server (e.g., mongodb://user:password@host).
    --database_name: The name of the database where the data will be stored.
    --collection_name: The name of the collection where the nodes will be stored.
    --store_path: The path to the directory containing the JSON files with node configurations.
    --replace_existing: A flag to indicate whether to replace existing nodes or skip updates (true if one of: true, t, 1, yes).
Functions:
    - None (the script executes as a standalone program).
Usage:
    Run the script from the command line with the required arguments. For example:
        python populate_mongodb.py --server_url mongodb://localhost:27017 \
                                   --database_name my_database \
                                   --collection_name my_collection \
                                   --store_path /path/to/json/files \
                                   --replace_existing true
"""

from pymongo import MongoClient
from pathlib import Path
import json
import logging
import argparse
import os

log_format = '[%(asctime)s] [%(levelname)s] - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)

parser = argparse.ArgumentParser()
parser.add_argument('--server_url', dest='server_url', default=os.environ.get('SERVER_URL'), help='URL of the mongodb server (mongodb://user:password@host). May be provided as environment variable SERVER_URL.')
parser.add_argument('--database_name', dest='database_name', default=os.environ.get('DATABASE_NAME'), help='Name of the database where the data shall be stored. May be provided as environment variable DATABASE_NAME.')
parser.add_argument('--collection_name', dest='collection_name', default=os.environ.get('COLLECTION_NAME'), help='Name of the collection, where the nodes shall be stored. May be provided as environment variable COLLECTION_NAME.')
parser.add_argument('--store_path', dest='store_path', default=os.environ.get('SOTRE_PATH'), help='Path to the folder where the json files that contains the node configuration are stored. May be provided as environment variable STORE_PATH.')
parser.add_argument('--replace_existing', dest='replace_existing', default=os.environ.get('REPLACE_EXISTING'), help='Weather replace existing nodes or skip it. May be provided as environment variable REPLACE_EXISTING.') 

args = parser.parse_args()
logging.info(args)

if not args.server_url:
    logging.error('server_url is missing.')
    exit(parser.print_help())
elif not args.database_name:
    logging.error('database_name is missing.')
    exit(parser.print_help())
elif not args.collection_name:
    logging.error('collection_name is missing.')
    exit(parser.print_help())
elif not args.store_path:
    logging.error('store_path is missing.')
    exit(parser.print_help())              
elif not args.replace_existing:
    logging.error('replace_existing is missing.')
    exit(parser.print_help())

args.replace_existing = args.replace_existing.lower() in ("yes", "true", "t", "1")

client = MongoClient(args.server_url)
collection = client[args.database_name][args.collection_name]
nodes = collection.nodes

json_files = Path(args.store_path).glob("*.json")
for json_file in json_files:
    with open(json_file) as node_file:
        node_id = json_file.parts[-1].split('.')[0]

        node = json.load(node_file)
        node['id'] = node_id
        
        db_node = collection.find_one({'id': node_id})
        
        if db_node != None:
            if args.replace_existing:
                db_node = collection.replace_one({'id': node_id}, node)
                logging.info(f'node [id: {node_id}] recreated')
            else:
                logging.info(f'node [id: {node_id}] already exists, update skipped')
        else:
            node['id'] = node_id
            db_node_id = collection.insert_one(node)
            logging.info(f'node [id: {node_id}] created')


