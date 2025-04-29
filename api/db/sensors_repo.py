import settings
from pymongo import MongoClient

def get_all(offset, limit):
    
    client = MongoClient(settings.DB_URL)
    collection = client[settings.DB_DATABASE_NAME][settings.DB_COLLECTION_NAME]
    cursor = collection.find({}, projection={'_id': False}, skip=offset, limit=limit)
    nodes = []
    for node in cursor:
        nodes.append(node)
        
    return nodes


def get_count():
    
    client = MongoClient(settings.DB_URL)
    collection = client[settings.DB_DATABASE_NAME][settings.DB_COLLECTION_NAME]
    count = collection.estimated_document_count()
    return count


def get(id):
    
    client = MongoClient(settings.DB_URL)
    collection = client[settings.DB_DATABASE_NAME][settings.DB_COLLECTION_NAME]
    node = collection.find_one({'id': id}, projection={'_id': False})
    if node is None:
        raise Exception(f"Node {id} not found")
    return node

