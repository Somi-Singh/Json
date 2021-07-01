import json
py =  { "name":"david", "class":1, "age":6}

js = json.dumps(py)
print(py)
print(js)
print(type(js))
print(type(py))
