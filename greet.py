def greet(name):
    name = "my friend" if name == None else name

    if(name.isupper()):
        return "HELLO " + name + "!"
    else:
        return "Hello, " + name + "."

