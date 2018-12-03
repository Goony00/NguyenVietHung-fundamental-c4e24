items= ["T-Shirt", "Sweater"]

user = input("Welcome to our shop, what do you want (c, r, u, d)?  ")
print("Our items:", end=" ")
print( *items, sep=", ")

while True:
    if user=="c":
        h=input("Enter new item: ")
        items.append(h)
        print("Our items: ", end=" ")
        print(*items, sep=", ")
        break

    elif user=="r":
        break

    elif user=="u":
        n=int(input("Update position? "))
        if (n-1) >= len(items):
            print("Unavailable")
        else:
            h=str(input("New items: "))
            items[n-1]=h
            print("Our items: ", end=" ")
            print(*items, sep=", ")
            break
    
    elif user=="d":
        i=int(input("Delete position? "))
        n=i-1
        
        if n < len(items):
            items.pop(n)
            print("Our items: ", end=" ")
            print(*items, sep=", ")
            break
        else:
            print("Please try again")




    