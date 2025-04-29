from  __main__ import app
import settings
import os
import hashlib
import logging
import sensors
from flask import json, request
import db.sensors_repo as sensors_repo


@app.route('/api/ealite/configurations/<device_id>', methods=['GET'])
def get_configuration(device_id):
    response = app.response_class(mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    try:
        etag = request.headers.get('If-None-Match')
        sensor = json.dumps(sensors_repo.get(device_id))
        sensor_hash =  hashlib.md5(sensor.encode('utf-8')).hexdigest()
        if ((etag is None) or (etag != sensor_hash)):
            response.headers['ETag'] = sensor_hash
            response.status = 200
            response.response = sensor
        else:
            response.status = 304
    except Exception as ex:
        logging.error(f'unable to load config for {device_id}: {ex}')
        response.response = json.dumps({"message": f"unable to get configuration"})
        response.status = 500
        
    return response


@app.route('/api/ealite/decodedconfigurations/<device_id>', methods=['GET'])
def get_decodedconfiguration(device_id):
    response = app.response_class(mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    try:
        sensor_data = sensors_repo.get(device_id)
        
        decoded_sensor_capabilities = []
        
        for capability in sensor_data['datapoints']:
            type, model, value_type, conversion_type, operations_type = sensors.decode_cap(int(capability['d']))
            cap_desc = {"type": type.name, 
                        "model": model.name, 
                        "valueType": value_type.name,
                        "conversionType": conversion_type.name,
                        "operationsType": operations_type.name,
                        "fullName": f'{type.name}-{model.name}-{value_type.name}-{conversion_type.name}-{operations_type.name}',
                        "timeseries": capability['u'],
                        "capability": capability['d']}
            decoded_sensor_capabilities.append(cap_desc)
        
        response.status = 200
        response.response = json.dumps(decoded_sensor_capabilities)
    except Exception as ex:
        logging.error(f'unable to load config for {device_id}: {ex}')
        response.response = json.dumps({"message": f"unable to get configuration"})
        response.status = 500
        
    return response


@app.route('/api/ealite/encodecap', methods=['GET'])
def get_encodecap():
    response = app.response_class(mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'

    type = request.args.get('type', default=None, type=str)
    model = request.args.get('model', default=None, type=str)
    value_type = request.args.get('valueType', default=None, type=str)
    conversion_type = request.args.get('conversionType', default=None, type=str)
    operations_type = request.args.get('operationsType', default=None, type=str)
    
    try:
        encoded_sensor_capability = sensors.encode_cap(
            sensors.Type[type],
            sensors.Model[model],
            sensors.Value_Type[value_type],
            sensors.Conversion_Type[conversion_type],
            sensors.Operations_Type[operations_type]
        )
        
        response.status = 200
        response.response = json.dumps({"raw": str(encoded_sensor_capability), "hex": hex(encoded_sensor_capability)})
    except Exception as ex:
        logging.error(f'unable to encode based on the given parameters: {ex}')
        response.response = json.dumps({"message": f"unable to encode"})
        response.status = 500
        
    return response


@app.route('/api/ealite/decodecap', methods=['GET'])
def get_decodecap():
    response = app.response_class(mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'

    capability = request.args.get('capability', default=None, type=str)
    if capability.startswith('0x'):
        capability = int(capability, 16)
    
    logging.info(f'decoding capability: {capability}')
    
    try:
        decoded_sensor_capability = sensors.decode_cap(int(capability))
        
        result = {"type": decoded_sensor_capability[0].name,
                  "model": decoded_sensor_capability[1].name,
                  "valueType": decoded_sensor_capability[2].name,
                  "conversionType": decoded_sensor_capability[3].name,
                  "operationsType": decoded_sensor_capability[4].name}
        
        logging.info(f'decoded capability: {result}')
         
        response.status = 200
        response.response = json.dumps(result)
    except Exception as ex:
        logging.error(f'unable to decode based on the given parameters: {ex}')
        response.response = json.dumps({"message": f"unable to decode"})
        response.status = 500
        
    return response


@app.route('/api/ealite/configurations', methods=['GET'])
def get_configurations():
    response = app.response_class(mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    try:
        offset = request.args.get('offset', default=0, type=int)
        limit = request.args.get('limit', default=99999, type=int)
        
        response.response = json.dumps(sensors_repo.get_all(offset=offset, limit=limit))            
        response.status = 200
    except Exception as ex:
        logging.error(f'unable to load configurations: {ex}')
        response.response = json.dumps({"message": f"unable to get configurations"})
        response.status = 500
        
    return response


@app.route('/api/ealite/configurationsCount', methods=['GET'])
def get_configurations_count():
    response = app.response_class(mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    try:
        response.response = json.dumps(sensors_repo.get_count())            
        response.status = 200
    except Exception as ex:
        logging.error(f'unable to load configurations: {ex}')
        response.response = json.dumps({"message": f"unable to get configurations count"})
        response.status = 500
        
    return response


@app.route('/api/ealite/types/<capability>', methods=['GET'])
def get_type(capability):
    response = app.response_class(mimetype='application/json', status=200)
    type, model, value_type, conversion_type, operations_type = sensors.decode_cap(int(capability))
    
    cap_desc = {"type": type.name, 
                "model": model.name, 
                "valueType": value_type.name,
                "conversionType": conversion_type.name,
                "operationsType": operations_type.name,
                "fullName": f'{type.name}-{model.name}-{value_type.name}-{conversion_type.name}-{operations_type.name}'}
    response.response = json.dumps(cap_desc)

    return response
