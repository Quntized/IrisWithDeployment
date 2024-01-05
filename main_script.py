import module_script


print("I am calling function1 which is inside module_script.py file")
module_script.function1()
if __name__ == '__main__':
    print("__name__\__main__ = ",__name__)
else:
    print("__name__\__main__ , let's see: ",__name__)