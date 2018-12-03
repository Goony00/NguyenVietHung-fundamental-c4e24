from random import randint

word="hexagon"
characters=list(word)

while len(characters)>0:
    #1. Select character randomly
    #1.1. Random -> number 0 -> len() -1
    #1.2. number -> index
    i=randint(0, len(characters)-1)
    ch=characters[i]

    #2. Print selected character
    print(ch, end=" ")

    #3. Remove selected character
    characters.pop(i)

print()

guess=input("doan xem? ")
if guess==word:
    print("gud")
else:
    print("bad")
