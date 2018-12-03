print("Hello, my name is Hung and these are my sheep's sizes")
sizes=[5, 7, 300, 90, 24, 50, 75]
print(sizes)

x=max(sizes)
print("Now my biggest sheep has size", x, end=" ")
print("let's shear it")

print("After shearing, here is my flock")
sizes[sizes.index(x)]=8            
print(sizes)
print()

n=int(input("How many months? "))

for i in range(n):
    print("MONTH", i+1, " :")
    
    for i in range(len(sizes)):
        sizes[i]= int(sizes[i]) + 50
    
    print("One month has passed, now here is flock")
    print(sizes)

    x=max(sizes)
    print("Now my biggest sheep has size", x, end=" ")
    print("let's shear it")

    print("After shearing, here is my flock")
    sizes[sizes.index(x)]=8            
    print(sizes)
    print()
    # list[i]=x: thay the gia tri o vi tri i bang gia tri x; 
    # list.index(v): vi tri cua gia tri v



