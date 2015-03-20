# coding: utf-8

print("BMI")

while True:
    height = 0.0
    weight = 0.0
    bmi = 0.0
    height = raw_input("身長は？（cm）=")
    height = float(height)
    if height==0:
        print("END")
        break
    elif 100 <= height <=300:
        height /= 100
    weight = raw_input("体重は？（kg）=")
    weight = float(weight)
    bmi = weight / (height * height)
    if bmi <= 18.5:
        print("痩せ形")
    elif bmi <= 25:
        print("普通体重")
    elif bmi <= 30:
        print("肥満（1度）")
    elif bmi <= 35:
        print("肥満（2度）")
    elif bmi <= 40:
        print("肥満（3度）")
    else:
        print("肥満（4度）")
