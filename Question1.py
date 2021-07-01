import json
js =  '{ "name":"John", "age":30, "city":"New York"}'
py = json.loads(js)
print(py)
print(type(py))
