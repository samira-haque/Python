info = {
    # "key" : "value"
    "name" : "SamiraHaque" ,
    "subjects" : ["python","C", "Java"],
    "topics" : ("dict", "set"),
    "learning" : "coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
    #12.99 : 94.4
}

print(info["name"])
print(info["topics"])
print(info["subjects"])
print(info["age"])

#print(info("surname"))

info["name"] = "Alex" #also add number or any value
info["surname"] = "Wilter"
print(info)

null_dict = {}
null_dict["name"] = "SamiraHaque"
print(null_dict)
