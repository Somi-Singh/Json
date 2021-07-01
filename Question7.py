import json
dic={"name":"Abhishek","designation":"CEO of""    ""navgurukul","gender":"male","age":29}
with open("text.json","w") as f:
    json.dump(dic,f,indent=4)
js=json.dumps(dic)
print(type(js))