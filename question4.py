import json
py= {"4":5,"6":7,"1":3,"2":4}
s=(json.dumps(py,sort_keys=True,indent=4))
print(s)
print(type(s))
