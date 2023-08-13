
import json

def load_data():
    with open("zomato/db.json","r") as f:
        return json.load(f)
    
def save_data(data):
    with open('zomato/db.json','w') as f:
        return json.dump(data, f)