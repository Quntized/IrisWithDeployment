def function1():
    print("Inside function1")

print("Is it inside main or not i donot know,let's check: ",__name__)

if __name__ == '__main__':
    print("Is __name__ is __main__ . ",__name__)
else:
    print("Whatever!!!")