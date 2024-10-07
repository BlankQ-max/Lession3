Names = ["yanyan","loyloy","tingting","marmar"]
num = input("remove or not? ")
if num == "remove":
    enter = input("who to remove? ")
    if enter == "yanyan":
        Names.pop(0)
        print(Names)
    elif enter == "loyloy":
        Names.pop(1)
        print(Names)
    elif enter == "tingting":
        Names.pop(2)
        print(Names)
    elif enter == "marmar":
        Names.pop(3)
        print(Names)
    else:
        print("error")
elif num == "not":
    print(Names)
else:
    print("error")