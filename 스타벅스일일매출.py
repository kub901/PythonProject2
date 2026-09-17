# 스타벅스 판매량 구하기
file_name = "스타벅스일일매출.txt"
dates = []
espresso = [] # 빈 리스트 생성
americano =[]
cafelatte =[]
cappuccino = []

with open(file_name, "r", encoding="utf-8") as file:
    header = file.readline().split()  # 줄 바꿈 기준으로 한줄을 읽어 들임

    for e in file:
        data_list = e.split()
        dates.append(data_list[0])
        espresso.append(int(data_list[1]))   # 10
        americano.append(int(data_list[2]))  # 50
        cafelatte.append(int(data_list[3]))  # 45
        cappuccino.append(int(data_list[4]))  # 20

# 제목 / 전제 판매량 / 일 평균 판매량
print("제목\t\t\t  전체 판매량\t\t일 평균 판매량")
print("----------------------------------------")
print(f"{header[1]:8}  {sum(espresso):10}  {sum(espresso) / len(espresso):14.2f}")
print(f"{header[2]:8}  {sum(americano):10}  {sum(americano) / len(americano):14.2f}")
print(f"{header[3]:8}  {sum(cafelatte):10}  {sum(cafelatte) / len(cafelatte):14.2f}")
print(f"{header[4]:8}  {sum(cappuccino):10}  {sum(cappuccino) / len(cappuccino):14.2f}")

# 1. 각 메뉴별 전체 판매량
def total_sales_func():
    print("\n 전체 판매량")
    print(f"{header[1]:<12}: {sum(espresso)}")
    print(f"{header[2]:<12}: {sum(americano)}")
    print(f"{header[3]:<12}: {sum(cafelatte)}")
    print(f"{header[4]:<12}: {sum(cappuccino)}")
    print("---------------------------------")

# 2. 각 메뉴별 일 평균 판매량
def avg_sales_func():
    days = len(dates)  # 리스트에 포함된 날짜의 갯수
    print("\n 일 평균 판매량")
    print(f"{header[1]:<12}: {sum(espresso) / days:.2f}")
    print(f"{header[2]:<12}: {sum(americano) / days:.2f}")
    print(f"{header[3]:<12}: {sum(cafelatte) / days:.2f}")
    print(f"{header[4]:<12}: {sum(cappuccino) / days:.2f}")
    print("---------------------------------")

# 3. 판매량이 가장 높은 메뉴 구하기
def most_sold_menu_func():
    # total_list: 각 메뉴에 대한 총수량 정보 저장
    total_list = [sum(espresso), sum(americano), sum(cafelatte), sum(cappuccino)]
    max_value = max(total_list)  # 리스트에서 가장 큰값 추출
    max_index = total_list.index(max_value)  # 해당 인덱스 추출
    # header[1] ~ header[4]에 해당 메뉴명이 있으므로 +1 필요
    print(f"\n 가장 많이 팔린 메뉴는 '{header[max_index + 1]}' ({max_value}개)")
    print("---------------------------------")
# 4. 판매량이 가장 적은 메뉴 구하기
def least_sold_menu_func():
    total_list = [sum(espresso), sum(americano), sum(cafelatte), sum(cappuccino)]
    min_value = min(total_list)
    min_index = total_list.index(min_value)
    print(f"\n 가장 적게 팔린 메뉴는 '{header[min_index + 1]}' ({min_value}개)")
    print("---------------------------------")
# 5. 판매량이 가장 많은 날짜 구하기
def best_sales_day_func():
    total_per_day = []
    for i in range(len(dates)):
        total = espresso[i] + americano[i] + cafelatte[i] + cappuccino[i]
        total_per_day.append(total)
    max_sales = max(total_per_day)
    max_index = total_per_day.index(max_sales)
    print(f"\n 가장 많이 팔린 날은 '{dates[max_index]}' ({max_sales}개)")
    print("---------------------------------")

# 6. 반복문으로 구성된 메뉴 만들기
while True:
    print("\n===== Starbucks 매출 분석 =====")
    print("[1] 각 메뉴별 전체 판매량")
    print("[2] 각 메뉴별 일 평균 판매량")
    print("[3] 판매량이 가장 높은 메뉴")
    print("[4] 판매량이 가장 적은 메뉴")
    print("[5] 판매량이 가장 많은 날짜")
    print("[0] 종료")
    choice = int(input("메뉴를 선택하세요: "))

    if choice == 1:
        total_sales_func()
    elif choice == 2:
        avg_sales_func()
    elif choice == 3:
        most_sold_menu_func()
    elif choice == 4:
        least_sold_menu_func()
    elif choice == 5:
        best_sales_day_func()
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("유효한 번호를 입력하세요.")

