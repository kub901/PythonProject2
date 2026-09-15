# 기본 메뉴 추가
# {} 중괄호를 사용해 선어, 각 요소는 ,(쉼표)로 구분
# 키와 값은 :(콜론)으로 구분
# 딕셔너리 내부에 리스트를 가짐
from unicodedata import category

menu = {
    "americano": ["coffee", 2000,  "기본 커피 입니다."],
    "espresso": ["coffee", 2500, "진한 커피 입니다."],
    "latte": ["coffee", 4000, "우유가 들어 있는 커피"],
    "green tea": ["tea", 4500, "녹차 입니다."],
    "black tea": ["tea", 4500, "홍차 입니다."],
}

# 전체 메뉴 조회
# def는 함수를 만드는 키워드
def print_menu():
    for e in menu:
        print(f"{e} - {menu[e]}")

# 개별 메뉴 조회
def get_menu(name):
    if name in menu:  # 메뉴 딕셔너리에 전달 받은 이름이 있는 지 확인
        print(menu[name])
    else:
        print("찾는 메뉴가 없습니다.")
# 메뉴 추가
def add_menu(name, category, price, desc):
    if name not in menu:
        menu[name] = [category, price, desc]
        print(f"{name}메뉴가 추가되었습니다.")
    else:
        print("메뉴가 이미 존재합니다.")
# 메뉴 삭제
def del_menu(name):
    if name in menu:
        del menu[name]
        print(f"{name}메뉴가 삭제되었습니다.")
# 메뉴 수정
def up_menu(name):
    if name in menu:
        menu[name] = [category, price, desc]
        print(f"{name}메뉴가 수정되었습니다.")
    else:
        print("수정할 메뉴가 없습니다.")

# 파일에서 불러오기
def load_menu():
    try:    # 예외가 발생하기 쉬운구간에 사용
        with open("menu.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 존재 하지 않습니다.")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")

# 파일에 저장하기
def save_menu():
    with open("menu.json", "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)
        print("menu.json 파일이 저장되었습니다.")

# 전체 메뉴 만들기
# [1]전체 메뉴 보기 [2]개발 메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]메뉴 수정 [6]종료하기
while True:
    print("메뉴를 선택 하세요: ")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]종료 : "))

    if choice == 1:
        print_menu()
    elif choice == 2:
        name = input("조회할 메뉴 이름 입력: ")
        get_menu(name) # 매개 변수로 값을 전달
    elif choice == 3:
        name = input("추가할 메뉴 입력: ")
        category = input("분류 입력: ")
        price = int(input("가격 입력: "))
        desc = input("설명 입력: ")
        add_menu(name, category, price, desc)
    elif choice == 4:
        name = input("삭제할 메뉴 이름 입력: ")
        del_menu(name)
    elif choice == 5:
        name = input("수정할 메뉴 이름 입력: ")
        category = input("분류 입력: ")
        price = input("가격 입력: ")
        desc =  input("설명 입력: ")
        up_menu(name)
    elif choice == 6:
        menu = load_menu()
    elif choice == 7:
        save_menu()
    elif choice == 0:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("잘못된 메뉴 선택입니다.")
