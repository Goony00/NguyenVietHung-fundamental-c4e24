
price = {
    "awp": "4750$",
    "m4a4": "3100$",
    "negev": "2000$"
}
print(*price)
n=input("gun: ")


if n in price:
    print(price[n])
else:
    print("not found")