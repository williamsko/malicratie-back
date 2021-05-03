import requests
import json
from os import environ

def send_request(url,data,method, h=None):
    headers = {}
    if h:
        headers.update(h)

    if method == 'POST':
        headers.update({'content-type': 'application/json'})
        response = requests.post(url=url,data=json.dumps(data),headers=headers,verify=True)
        if response.status_code != 200 :
            return TransactionPipelineError(message='CONNECTION_TO_PARTNER_ERROR')
        return response.json()
    elif method == 'GET':
        response = requests.get(url=url,params=data)
        if response.status_code != 200 :
            return TransactionPipelineError(message='CONNECTION_TO_PARTNER_ERROR')
        return response.json()
    else:
        return return TransactionPipelineError(message='METHOD_NOT_YET_SUPPORTED_ERROR')
