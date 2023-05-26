import requests

global_url = 'http://localhost:5001'

def listIncidencias(doc):
    data = requests.post(
        f'{global_url}/api/cliente/incidencias', 
        json = {
            'num_doc' : doc
        }
    )

    return data.json()
