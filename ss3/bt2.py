
favs = ["origin", "steam", "uplay"]
print(favs, sep=", ")

n=int(input("muon gi? "))

if n>= len(favs):
    print("ko co")
else:
    print(favs[n])

