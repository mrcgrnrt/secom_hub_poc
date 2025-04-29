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
parser.add_argument('--node-01-id', dest='node_01_id', required=True, help='ID of the first node for the comparison.')
parser.add_argument('--node-02-id', dest='node_02_id', required=True, help='ID of the second node for the comparison.')

args = parser.parse_args()

client = MongoClient(args.server_url)
collection = client[args.database_name][args.collection_name]
nodes = collection.nodes

def get_node(node_id):
    node = collection.find_one({'id': node_id})
    if node == None:
        logging.error(f'node with id {node_id} does not exist')
    return node

node_01 = get_node(args.node_01_id)
node_02 = get_node(args.node_02_id)
if node_01 != None and node_02 != None:
    diff = DeepDiff(node_01, node_02)
    logging.info(f'{diff}')
    for change in diff['values_changed']:
        logging.info(f'{change}')
