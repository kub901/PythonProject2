# update 함수 사용하기: 딕셔너리 데이터를 한꺼번에 변경 가능
# coffee_menu.update({"Americano": 3000, "Espresso": 3000, "Latte": 4500, "Moca": 5000})
# print(coffee_menu)
from 조건문실습 import coffee

# 문제1
student_score={"철수": 90, "영희": 85, "민수": 78}
print(student_score)
# 문제2
print(coffee_menu["Moca"])
print(coffee_menu.get("Cappuccino"))
# 문제3
coffee_menu["Cappuccino"]=4800
del coffee_menu["Moca"]
print(coffee_menu)
# 문제4
for e in coffee_menu:
    if coffee_menu[e]>=4000:
        print(f"{e} - {coffee[e]}")
# 문제5
for key, value in coffee_menu.items():
    coffee_menu[key] = int(value * 1.1)
print(coffee_menu)

if "라떼" in coffee_menu:
    print("라떼 메뉴가 있습니다.")
else:
    print("라뗴 메뉴가 없습니다.")