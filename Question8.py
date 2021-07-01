import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
list5=["name","designation","age","salary"]
d1={}
d2={}
d3={}
d4={}
dictionary={}
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        d1[list5[i]]=list1[i]
        d2[list5[i]]=list2[i]
        d3[list5[i]]=list3[i]
        d4[list5[i]]=list4[i]
        j=j+1
    dictionary["emp1"]=d1
    dictionary["emp2"]=d2
    dictionary["emp3"]=d3
    dictionary["emp4"]=d4
    i=i+1
print(dictionary)
f=open("course.json","w")
json.dump(dictionary,f,indent=6)
