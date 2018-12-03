favs = ["origin", "steam", "uplay"]
print(favs)



while True:
    n=int(input("muon xoa vi tri nao? "))
    favs.pop(n)
    if n >=len(favs):
        print("ko xoa dc")
    else:
        print(favs)
        break

