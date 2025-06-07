
def check_for_word():
    word = "xlearning"
    with open("practice.txt","r") as f :
        data = f.read()
        if(data.find(word) != -1) :
            print("found")
        else:
            print("Not found")

check_for_word()