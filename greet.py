def greet(name):
    if(isinstance(name, list)):
        if(name.__len__() == 2):
            return "Hello, " + name[0] + " and " + name[1] + "."
        else:
            ret_str = "Hello, "
            i = 0
            while(i < name.__len__() - 1):
                ret_str = ret_str + name[i] + ", "
                i = i + 1
            return ret_str + "and " + name[name.__len__() - 1] + "."
    else:
        name = "my friend" if name == None else name

        if(name.isupper()):
            return "HELLO " + name + "!"
        else:
            return "Hello, " + name + "."



