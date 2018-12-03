
favs = ["origin", "steam", "uplay"]
print(favs)

while True:

    n=int(input("muon thay doi gi? "))
    
    
    if n >=len(favs):
        print("ko doi dc")
    else:
        h=str(input("thanh cai gi? "))
        favs[n]=h
        print(favs)
        break



