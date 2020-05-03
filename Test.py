import json

json_file = open("products.json")
products = json.load(json_file)
print(type(json.dumps(products)))