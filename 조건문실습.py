# [실습문제] 자판기 만들기 (조건문만 사용)
from random import choice

# 아래 메뉴를 참고하여 자판기 프로그램을 작성하시오.

# 1. 콜라 - 1100원
# 2. 사이다 - 1000원
# 3. 커피 - 700원
# 4. 생수 - 600원

# [처리조건]
# 1)사용자로부터 구매할 음료 번호(1~4)를 입력 받는다.
# 2)메뉴에 없는 번호를 입력하면 "존재하지 않는 메뉴입니다." 출력 후 종료한다.
# 3)올바른 번호를 입력했다면, 선택한 음료의 이름가 가격을 안내하고
#   누입할 금액을 입력 받는다.
# 4)투입한 금액이 음료 가격보다 적으면
#   "금액이 부족합니다. 000원이 부족합니다." 를 출력하고 종료한다.
#   (부족한 금액이 정확히 계산되어 출력되어야 함)
# 5)투입한 금액이 음료 가격 이상이면
#   "000가 나왔습니다. 잔돈 000원을 거슬러 드립니다."  를 출력한다.
#   (거스름돈이 정확히 계산되어 출력되어야 함)

# ** 반복문(while, for), 딕셔너리는 사용하지 말고 조건문(if/elif/else)만으로 작성할 것
coke = 1100
cider = 1000
coffee = 700
water = 600
menu = input("구매할 음료를 선택하세요. \n 1. 콜라 \n 2. 사이다 \n 3. 커피 \n 4. 생수 \n 번호 입력: ")
if menu == "1":
    print(f"콜라를 선택하셨습니다. 가격은 {coke}원 입니다.")
    cost = int(input("누입할 금액 입력: "))
    if cost < coke:
        print(f"금액이 부족합니다. {coke-cost}원이 부족합니다.")
        exit
    elif cost > coke:
        print(f"콜라가 나왔습니다. 잔돈 {cost-coke}원을 거슬러 드립니다.")
    else:
        print("콜라가 나왔습니다.")
elif menu == "2":
    print(f"사이다를 선택하셨습니다. 가격은 {cider}원 입니다.")
    cost = int(input("누입할 금액 입력: "))
    if cost < cider:
        print(f"금액이 부족합니다. {cider - cost}원이 부족합니다.")
        exit
    elif cost > cider:
        print(f"사이다가 나왔습니다. 잔돈 {cost - cider}원을 거슬러 드립니다.")
    else:
        print("사이다가 나왔습니다.")
elif menu == "3":
    print(f"커피를 선택하셨습니다. 가격은 {coffee}원 입니다.")
    cost = int(input("누입할 금액 입력: "))
    if cost < coffee:
        print(f"금액이 부족합니다. {coffee - cost}원이 부족합니다.")
        exit
    elif cost > coffee:
        print(f"커피가 나왔습니다. 잔돈 {cost - coffee}원을 거슬러 드립니다.")
    else:
        print("커피가 나왔습니다.")
elif menu == "4":
    print(f"생수를 선택하셨습니다. 가격은 {water}원 입니다.")
    cost = int(input("누입할 금액 입력: "))
    if cost < water:
        print(f"금액이 부족합니다. {water - cost}원이 부족합니다.")
        exit
    elif cost > water:
        print(f"생수가 나왔습니다. 잔돈 {cost - water}원을 거슬러 드립니다.")
    else:
        print("생수가 나왔습니다.")
else:
    print("존재하지 않는 메뉴입니다.")


# choice = int(input("음료 번호 입력: "))
# if choice == 1:
#     name = "콜라"
#     price = 1100
# elif choice == 2:
#     name = "사이다"
#     price = 1000
# elif choice == 3:
#     name = "커피"
#     price = 700
# elif choice == 4:
#     name = "생수"
#     price = 600
# else:
#     name = "없음"
#     price = 0
#
# if name == "없음"
#     print("존재하지 않는 메뉴 입니다.")
# else:
#     print(f"{name}({price}원)을 선택 했습니다.")
#     money =int(input("투입할 금액을 입력하세요: "))
#
#     if money < price:
#         print(f"투입 금액이 부족합니다. {price - money}원 부족")
#     else:
#         change = money - price
#         print(f"{name}가 나왔습니다. 잔돈 {change}원을 거슬러 드립니다.")













