collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1) 
# collection.remove(7) key error 
collection.add((1,2,3))
# collection.clear() ->> clear the values
print(len(collection))


collection = {"gellow", "hi", "GOOD"}
print(collection.pop())

print(collection)



set1 ={1,2,3}
set2 = (2,3,4)

print(set1.union(set2)) #{1,2,3,4}
print(set1)
print(set2)

print(set1.intersection(set2)) #{2,3}