# 이름 입력
# 나이 입력: 1~199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# 성별 입력: 영문자(M과m은 남성)(F와f는 여성)으로 입력받고 나머지는 재입력 요청




# 짝수/홀수 개수 세기
# 정수를 하나씩 계속 입력받다가 -1이 입력되면 반복을 종료. 그동안 입력받은 숫자 중 짝수의 개수와 홀수의 개수를 각각 출력
# while과 break 사용
even_cnt = 0
odd_cnt = 0
while True:
    n = int(input("정수 입력(-1 종료): "))
    if n == -1: break
    if n % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print(f"짝수 개수: {even_cnt}")
print(f"홀수 개수: {odd_cnt}")


# 구구단 중 특정 단만 출력
# 2~9 사이의 정수를 입력
while True:
    dan = int(input("2~9 사이의 정수 입력: "))
    if 2 <= dan <= 9:
        break
    print("잘못된 입력입니다.")

for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")