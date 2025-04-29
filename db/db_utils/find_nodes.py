from pymongo import MongoClient
import json
import logging
import argparse
from deepdiff import DeepDiff

log_format = '[%(asctime)s] [%(levelname)s] - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)

parser = argparse.ArgumentParser()
parser.add_argument('--server-url', dest='server_url', required=True, help='URL of the mongodb server (mongodb://user:password@host).')
parser.add_argument('--database-name', dest='database_name', required=True, help='Name of the database where the data shall be stored.')
parser.add_argument('--collection-name', dest='collection_name', required=True, help='Name of the collection, where the nodes shall be stored.')
parser.add_argument('--node-id', dest='node_id', required=True, help='ID of the first node for the comparison.')

args = parser.parse_args()

# client = MongoClient(args.server_url)
# collection = client[args.database_name][args.collection_name]


# cursor = collection.find({})
# for node in cursor:
#     logging.info(node)


def get_all():
    logging.info(f'db_server_url: {args.server_url}; db_name: {args.database_name}; db_collection_name: {args.collection_name}')
    
    client = MongoClient(args.server_url)
    collection = client[args.database_name][args.collection_name]
    cursor = collection.find({}, projection={'_id': False})
    for node in cursor:
        logging.info(f'----{node}')
        
    nodes = []
    cursor.rewind()
    for node in cursor:
        logging.info(node)
        nodes.append(json.dumps(node))
        
    return nodes

nodes = get_all()