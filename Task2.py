Names = ["yanyan","loyloy","tingting","marmar"]
enter = input("clear or not? ")
if enter == "clear":
    Names.clear()
    print(Names)
elif enter == "not":
    print(Names)
else:
    print("error")