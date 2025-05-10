student ={
    "name" : "alex wilter",
    "subjects" : {
        "phy" : 97,
        "chem": 98,
        "math" : 90,
    }
}

print(len(list(student.keys())))
print(list(student.values()))
print(student.items())
# pairs = list(student.items())
# print(pairs[0])

# # print(student["name2"]) #error
# print("hi")
# print("samira")
# print("learning")

print(student.get("name2")) # no error -> None

new_dict = {"city" : "Dhaka", "age": 16}
student.update(new_dict)
print(student)