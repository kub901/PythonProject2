# 외장함수: 파이썬에거 기본 제공, 단 import 해서 사용
import datetime
import random
# 랜덤 함수: 난수 발생기
# randint(m,n): 지정된 범위 안의 임의의 정수 생성

from random import randint
for i in range(20):
    print(f"{random.randint(1, 10)}", end=" ") # 1 ~ 10 사이의 임의의 값 생성
print()

#  randrange(m,n,p)
for i in range(20):
    print(f"{random.randrange(1,10,2)}", end=" ") # 1 ~ 10 미만 까지 임의의 값 생성
print()
# 무인도 탈출 게임
# 두개의 주사위를 굴려 같은 값이 나오면 "무인도를 탈출 했습니다. 탈출시도 횟수, 두개의 주사위 값"
n=0
while True:
    rand1 = random.randint(1,6)
    rand2 = random.randint(1,6)
    n += 1
    if rand1 == rand2:
        print(f"무인도를 탈출 했습니다. 탈출 시도 횟수: {n}, 두 개의 주사위 값: {rand1}, {rand2}")
        n = 0
        break
print()
# 로또 번호 생성 하기 (1~45사이의 임의의 수 7개, 단, 중복 되면 안됨)
lotto = []
while True:
    value = random.randint(1, 45)
    if value not in lotto: # 생성된 난수가 로또 리스트에 포함되어 있지 않으면,
        lotto.append(value) # 리스트의 마지막에 값 추가
    if len(lotto) == 6: break # 중복되지 않은 번호가 6개가 되면 반복문 탈출
print(lotto)

# 날짜 및 시간 관련 처리 모듈
from datetime import datetime
datetime.today() # 운영체제로 부터 시간 가져 오기
datetime.today().year  # 현재 연도 가져오기
datetime.today().month # 현재 월 가져오기
datetime.today().day  # 현재 일 가져오기
datetime.today().hour # 현재 시간 가져오기

print(datetime.today().year)
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)


# 오늘은 2024년 10월 12일 토요일 10시31분 입니다.
# 현재 시간 가져오기
# %Y: 4자리 연도
# %m: 2자리 월
# %d: 2자리 일
# %A: 요일 표시
# %H: 24시간 형식의 시간
# %M: 분 표시
now = datetime.now()
# 원하는 출력 형식 만들기
fromatted = now.strftime("오늘은 %Y년 %m월%d일 %A %H시%M분 입니다.")
print(fromatted)

# 실습1: 나의 생일까지 남은 일수 계산하기
# 오늘 날짜와 올해 생일(예:12월 25일)까지 남은 일수를 계산해보세요
today = datetime.today()
birthday = datetime(today.year, 12, 25)
print(f"생일까지 남은 날: {(birthday-today).days}")


# 실습2: 요일별 인사말 출력하기
# 오늘 요일에 따라 다른 메시지를 출력해보세요
# 월~금: "오늘은 평일입니다. 힘내세요!"
# 토, 일: "오늘은 주말입니다. 푹 쉬세요!"
weekday = today.weekday()
if 0 <= weekday <=4: print("오늘은 평일입니다. 힘내세요!")
else: print("오늘은 주말입니다. 푹 쉬세요!")

# if now.strftime("%A") == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
#     print("오늘은 평일입니다. 힘내세요!")
# else:
#     print("오늘은 주말입니다. 푹 쉬세요!")


# 실습3: 현재 시간대별 인사말 만들기
# 현재 시각(hour)에 따라 다른 인사말을 출력해보세요
# 06~11시: "좋은 아침입니다."
# 12~17시: "좋은 오후입니다."
# 18~22시: "좋은 저녁입니다."
# 그 외 : "늦은 밤이네요, 얼른 주무세요"
hour = datetime.today().hour
if 6 <= hour <= 11:
    print("좋은 아침입니다.")
elif 12 <= hour <=17:
    print("좋은 오후입니다.")
elif 18 <= hour <=22:
    print("좋은 저녁입니다.")
else:
    print("늦은 밤이네요, 얼른 주무세요.")
# 실습4: 원하는 형식으로 파일명 생성하기
# strftime을 활용해서 로그 파일명을 만들어 보세요.
# 예 : "backup_20261014_1530.txt"같은 형식
form = now.strftime("backup_%Y%m%d _%H%M.txt")
print(form)

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))
print(math.ceil(100.01))
print(math.floor(100.9))

# from simple_colors import *
#
# print(green('hello'))
# print(yellow('hello', 'bold'))
# print(red('hello', ['bold', 'underlined']))

# 실습문제1: 가위바위보 승부 판정(random)
# 컴퓨터가 random.randin로 가위0 바위1 보2 중 하나를 뽑고, 사용자가 입력한 값과 비교해서 승패를 판정하는 프로그램 작성
# 무승부가 나오면 같은 값이 나올 때까지가 아니라,
# 무승부 횟수를 세어 "총 N 번 만에 승부가 났습니다"를 출력하도록 반복문 구성
# 힌트: 무인도 탈출 게임의 while true +cnt 재사용
#  출력 예시: 무승부! 다시 도전합니다...-> 당신의 승리! 총 3번만에 승부가 났습니다.
cnt =0
choices = ["가위","바위","보"]

while True:
    computer = random.randint(0, 2)
    user = int(input("가위(0) 바위(1) 보(2) 중 입력: "))
    cnt += 1
    if user == computer:
        print(f"무승부! {choices[user]}, 다시 도전합니다.....")
        continue

    if user - computer == 1 or -2:
        print(f"컴퓨터:{choices[computer]}, 당신의 승리! 총 {cnt}번만에 승부가 났습니다.")
        cnt = 0

    elif user - computer == -1 or 2:
        print(f"컴퓨터:{choices[computer]}, 컴퓨터의 승리!")
    break
