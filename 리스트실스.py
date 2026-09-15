# 3개의 햄버거와 2개의 음료의 가격을 입력받아 제일 싼 세트 메뉴의 가격 구하기 (50원 할인)
# - 콘솔로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# - 햄버거 3개 중 가장 싼 가격을 선택하고 음료들 중 싼 음료의 가격을 합산하고 여기서 50원 할인
# burger1 = int(input("첫 번째 버거 가격: "))
# burger2 = int(input("두 번째 버거 가격: "))
# burger3 = int(input("세 번째 버거 가격: "))
# drink1 = int(input("첫 번째 음료 가격: "))
# drink2 = int(input("두 번째 음료 가격: "))
# set = [burger1, burger2, burger3, drink1, drink2]

# print(f"제일 싼 세트 메뉴: {min(set[0:3])+min(set[3:5])-50}")

# 리스트 순회하기 : 자동차 이름을 5대 입력 받음
# - 범위기반 for문으로 순회해서 출력: for i in range()
# - 시퀀스 for문으로 순회해서 출력: for e in 시퀀스
# - 오름차순, 내림차순 출력
cars = list(input("자동차 이름 5대 연속 입력: ").split())
for i in range(len(cars)):
    print(f"{i+1}번째 자동차 {cars[i]}", end=" ")
print()
for j in cars:
    print(j, end=" ")
print()
cars.sort()
print(cars)
print()
cars.sort(reverse=True)
print(cars)
