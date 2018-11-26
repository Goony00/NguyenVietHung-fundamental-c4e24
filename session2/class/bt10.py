a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))

d=b*b-4*a*c
a2=2*a
sqrt_d=d**0.5
if d<0:
    print("vo nghiem")
elif d==0:
    x=-b/a2
    print("phuong trinh co nghiem kep", x)
else: 
    x1=(-b+sqrt_d)/a2
    x2=(-b-sqrt_d)/a2
    print("pt co 2 nghiem pb la", x1, x2)