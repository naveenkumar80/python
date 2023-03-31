# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(type(height))
# print(type(weight))
height=float(height)
weight=int(weight)
BMI=weight/(height*height)
BMI=str(BMI)
print("your BMI is " + BMI )