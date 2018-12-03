items=["gg", "ez", "wp"]

lam= input("muon lam gi? c,r,u,d: ")
while True:
    if lam=="c":
        h=input("thich gi nua? ")
        items.append(h)
        print(*items, sep=", ")

    elif lam=="r":
        for index, items in enumerate(items):
            print(index+1, items, sep=". ")
        break

    elif lam=="u":
        n=int(input("muon thay doi gi? "))
        if n >=len(items):
            print("ko doi dc")
        else:
            h=str(input("thanh cai gi? "))
            items[n-1]=h
            print(items)
            break

    elif lam=="d":
        i=input("muon xoa cai gi? ")
        
        if i.isdigit():
            i = int(i)
            items.pop(i)
            if i>=len(items):
                print("ko xoa dc")
            else:
                print(items)
                break
        
        elif i.isalpha():
            items.remove(i)
            print(items)
            break
