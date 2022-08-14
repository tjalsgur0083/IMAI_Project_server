import pyrebase
import json

with open("./firebase.json") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
## db를 연결하는 코드