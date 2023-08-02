height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")




bmi = int(weight) / float(height) ** 2

bmi_as_int = float(bmi)

print(round(bmi_as_int, 1))
