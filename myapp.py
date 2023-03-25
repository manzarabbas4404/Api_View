import requests
import json
URL = "http://127.0.0.1:3000/StudentApi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':2}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)

    get_res = res.json()
    print(get_res)

get_data()
