h=float(input("nhap chieu cao (m): "))
w=float(input("nhap can nang (kg): "))

bmi=w/(h*h)
print("BMI=", bmi)

if bmi<16:
    print("Severly underweight")
elif 16<bmi<18.5:
    print("Underweight")
elif 18.5<bmi<25:
    print("Normal")
elif 25<bmi<30:
    print("Overweight")
else:
    print("Obese")
    