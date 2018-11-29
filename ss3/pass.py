loop=True
while loop:
    n = input("pass: ")
    if len(n)>8:
        if (not n.islower()) and (not n.isupper()) and (not n.isdigit()):
            loop=False


print("access granted")