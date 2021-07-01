import json 
dictionary ={ 
    "name" : "somi singh", 
    "rollno" : 40, 
    "cgpa" : 8.6, 
    "phonenumber" : "8423012627"
} 
   
with open("sample.json", "w") as outfile: 
    json.dump(dictionary, outfile)