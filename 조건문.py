# 제어문 : 프로그램의 흐름을 제어하는 데 사용
# - 조건문 : 입력 값에 따라 특정 코드 블록을 선택적으로 실행(if문, 3항연산자)
# - 반복문 : 조건이 충족되는 동안 특정 코드 블록을 반복 실행(while문, for문)

num  = int(input("정수 입력: "))

# 양수 / 음수 구분 하기
if num >= 0:
    print(f"{num}은 양수 입니다.")
else:
    print(f"{num}은 음수 입니다.")

# 홀수 / 짝수 구분하기
if num % 2 == 0:
    print(f"{num}은 짝수 입니다.")
else:
    print(f"{num}은 홀수 입니다.")

# M이면 남성, F면 여성
gender = input("m/f 성별 입력: ").upper()
if gender == "M":
    print("남성 입니다.")
elif gender == "F":
    print("여성 입니다.")
else:
    print("잘 못 입력하셨습니다.")

# 학생의 이름, 국어, 영어, 수학 성적을 입력 받음
# 각각의 성적이 0~100 사이가 아니면 성적이 잘 못 입력 되었습니다. 출력 후 종료
# 성적이 정상 입력 되었다면, 총점과 평균 구하기
# 평균이 90점 이상이면 이름과 등급 A
# 평균이 80점 이상이면 이름과 등급 B
# 평균이 70점 이상이면 이름과 등급 C
# 평균이 60점 이상이면 이름과 등급 D
# 나머지는 이름과 등급 F

# kor, eng, mat = map(int,input("국어 영어 수학: ").split())


name = input("이름 입력: ")
while True:
    kor = int(input("국어 점수 입력: "))
    eng = int(input("영어 점수 입력: "))
    mat = int(input("수학 점수 입력: "))
    if  0 <= kor <= 100 and  0 <= eng <= 100 and 0 <= mat <= 100:
        break
    print("성적이 잘 못 입력 되었습니다.")
total = kor + eng + mat
avg = total / 3
print(f"총점:{total}, 평균: {avg:.2f}")
if avg >= 90:
        print(f"{name} A")
elif avg >= 80:
        print(f"{name} B")
elif avg >= 70:
        print(f"{name} C")
elif avg >= 60:
        print(f"{name} D")
else:
        print(f"{name} F")


# 계절을 영문으로 입력 받아 계절에 맞는 문구 출력하기
# spring, summer, autumn, winter 입력 받아서 계절에 맞는 문구 출력
# 단, 비교의 편의를 위해 입력 받은 문자열은 대문자로 변환해서 비교하기
season = input("계절 영문 입력: ").upper()
if  season == "SPRING":
    print("새로운 시작을 품고 피어나는 봄날처럼, 당신의 오늘에도 따스한 햇살이 가득하기를.")
elif season == "SUMMER":
    print("푸른 바다와 청량한 바람처럼, 당신의 순간들이 시원하고 생기 넘치길 바랍니다.")
elif season == "AUTUMN" or season == "FALL":
    print("선선한 바람에 마음이 한결 가벼워지는 가을, 당신의 하루도 풍성하게 물들기를.")
else:
    print("차분하게 내려앉는 겨울 공기 속에서도, 당신의 마음만큼은 따뜻함으로 온전히 차오르길.")