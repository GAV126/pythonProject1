def calculate_BMI(weight,height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <=25:
        category = "正常"
    elif BMI<=30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"你的BMI分類為:{category}")
    print(f"你的BMI:{BMI:.2f}")
 #   return BMI
#result = calculate_BMI(1.8,70)
weight = int(input("請輸入體重的內容(kg):"))
height = float(input("請輸入身高的內容(m):"))


calculate_BMI(weight,height)