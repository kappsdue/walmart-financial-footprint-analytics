import conf
import requests
import json

def get_data():
    response = requests.get(url=conf.base_url, headers=conf.headers)
    print(response.status_code)
    return response.json()

#mannually created data and raw folder
def save_json(data, filename="data/raw/companyfacts.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_json(filename="data/raw/companyfacts.json"):
    with open(filename, "r") as file:
        return json.load(file)


# final build 23 jul 26
