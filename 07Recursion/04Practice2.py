#print all elements to the list
def print_list(list, idx=0):
    if(idx == len(list)) :
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango","lichi"]
print_list(fruits)