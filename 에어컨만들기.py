# 에어컨 만들기
# 전원 ON/OFF
# 현재 온도 표시 기능: 기본값은 20도로 설정
# 온도 조절 기능 (1도씩 조절 가능), 원하는 온도 설정
# 바람 세기 조절 기능(1단계, 2단계, 3단계)

class AirCon:
    # 전원, 설정 온도, 바람 세기를 매개변수로 전달 받은 생성자 만들기
    def __init__(self, power, temp, fan_speed):
        self.power = power  # 전원 상태 (True 또는 False)
        self.temp = temp  # 설정 온도 (숫자)
        self.fan_speed = fan_speed  # 바람 세기 (숫자)
        self.current_temp = 20
    # 전원 ON/OFF
    def set_power(self):
        if self.power == True:
            self.power = False
            print("에어컨 전원을 껐습니다.")
        else:
            self.power = True
            print("에어컨 전원을 켰습니다.")
    # 온도 설정

    def show_temp(self):  # 현재온도
        print(f"현재 온도: {self.current_temp}도 / 설정 온도: {self.temp}도")

    def temp_up(self): # 온도 올리기
        if not self.power:
            print("\n[경고] 전원이 꺼져 있습니다. 전원을 먼저 켜주세요.")
            return

        if self.temp < 30:
            self.temp += 1
            print(f"\n[알림] 설정 온도를 올렸습니다. (설정: {self.temp}℃)")
        else:
            print("\n[경고] 설정할 수 있는 최대 온도는 30℃입니다.")

    def temp_down(self): # 온도 내리기
        if not self.power:
            print("\n[경고] 전원이 꺼져 있습니다. 전원을 먼저 켜주세요.")
            return
        if self.temp > 18:
            self.temp -= 1
            print(f"\n[알림] 설정 온도를 내렸습니다. (설정: {self.temp}℃)")
        else:
            print("\n[경고] 설정할 수 있는 최저 온도는 18℃입니다.")
    # 바람 세기
    def change_fan_speed(self):
        if not self.power:
            print("\n[경고] 전원이 꺼져 있습니다. 전원을 먼저 켜주세요.")
            return
        self.fan_speed += 1

        # 3단계를 넘어가면 다시 1단계로 되돌리기
        if self.fan_speed > 3:
            self.fan_speed = 1

        print(f"바람 세기: {self.fan_speed}단계")
    # 에어컨 정보 표시
    def display_info(self):
        print("\n=== [ 에어컨 디스플레이 ] ===")
        if self.power == False:
            print("상태: 전원 OFF")
            print("============================\n")
        else:
            print("상태: 전원 ON")
            print(f"현재 온도: {self.current_temp}℃")
            print(f"설정 온도: {self.temp}℃")
            print(f"바람 세기: {self.fan_speed}단계")
            print("============================\n")

# 에어컨 객체를 생성하고 메뉴를 구성해 동작 해보기
carrier = AirCon(False, 20,  1)
while True:
    # 현재 상태 표시
    carrier.display_info()

    # 메뉴 선택창 출력
    print("1. 전원 ON/OFF")
    print("2. 온도 올리기 (+1)")
    print("3. 온도 내리기 (-1)")
    print("4. 바람 세기 변경 (1->2->3)")
    print("5. 종료")

    choice = input("원하는 기능의 번호를 입력하세요: ")

    if choice == "1":
        carrier.set_power()
    elif choice == "2":
        carrier.temp_up()
    elif choice == "3":
        carrier.temp_down()
    elif choice == "4":
        carrier.change_fan_speed()
    elif choice == "5":
        print("\n에어컨 프로그램을 종료합니다.")
        break
    else:
        print("\n[오류] 올바른 번호를 입력해 주세요. (1~5)")



