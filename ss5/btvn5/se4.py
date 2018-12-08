print("Answer the following algebra question: ")

ques={
  "If x=8 then what is value of 4(x+3) ?" : [35,36,40,44],
  "Jack scored these marks in 5 math tests 49, 81, 72, 66 and 52. What is the mean ?" : [55,65,75,85],
}

ans={
  "If x=8 then what is value of 4(x+3) ?": 4,
  "Jack scored these marks in 5 math tests 49, 81, 72, 66 and 52. What is the mean ?" : 2,
}

total=0

for i in ques:
  print(i)
  a = ques[i]
  for e,a in enumerate(ques[i], 1):
    print(e, a, sep=". ")
    
  c=input("Your choice: ")
  if c==ans[i]:
    print("bingo")
    total+=1
  else:
    print(":(")


print("You correctly answer", total, "out of 2 questions")