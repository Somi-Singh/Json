import json
def com(obj):
    if "i" in obj:
        return complex(obj["real"],obj["img"])
    return obj
wc=json.loads('{"i":true,"real":4,"img":5}')
print(com(wc))