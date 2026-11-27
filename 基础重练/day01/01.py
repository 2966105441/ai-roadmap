height = 1.75
Weight = 70
BMI = Weight / height ** 2
print(f"BMI = {BMI:.1f}")
if BMI < 18.5:
    print("偏瘦")
elif BMI < 24:
    print("正常")
elif BMI < 28:
    print("偏胖")
else:
    print("肥胖")