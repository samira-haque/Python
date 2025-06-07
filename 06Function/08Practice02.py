cities = ["delhi","Mumbai","Dhaka","Khulna","Bogura"]
heroes =["thor","ironman","captain america"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")


print_list(heroes)
print_list(cities)
print()