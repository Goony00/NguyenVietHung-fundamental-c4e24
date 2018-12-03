import random

n=random.randint(1,10)


while True:
    
    i=int(input("Đoán xem? ~(˘▾˘~) :      "))
    
    if (n-i)<0:
       print("A little too large ¯\_(ツ)_/¯")
       print()
    elif (n-i)>0:
        print("Too small ლ(ಠ益ಠლ)")
        print()
    else:
        print()
        print("Nice try (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
        break


 