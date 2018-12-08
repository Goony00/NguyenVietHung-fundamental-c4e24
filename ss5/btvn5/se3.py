x=8
t=4*(x+3)
answer= [35,36,40,44]

print("Answer the following algebra question: ")
print("If x=8 then what is value of 4(x+3) ?")

for i,answer in enumerate(answer, 1):
  print(i, answer, sep=". ")

ans=int(input("Your answer: "))

if ans==4:
  print("bingo")
else:
  print(":(")