# for 문 : 정해진 범위만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스:
# for 변수 in range(시작값, 최종값, 증감값):
from email.mime import text

ive = ["안유진", "장원영", "이서", "가을", "레이", "리즈"]
for e in ive:   # 시퀀스형 데이터를 자동으로 반복 수행 하면서 요소의 값을 복사 하면서 수행
    print(e, end=' ')

print()

for i in range(0, len(ive), 2):
    print(ive[i], end=' ')


print()

for i in range(len(ive) - 1, 0 - 1, -1):
    print(ive[i], end=' ')

print()

# 1~100 사이의 3의 배수 출력하기
cnt=0
for i in range(1, 100+1):
    if i % 3 == 0:
        print(f"{i}", end=' ')
        cnt += 1
        if cnt >=10:
            print()
            cnt = 0

print()
# 입력 받은 수의 범위 내의 7의 배수를 출력.
# 한줄에 10개 씩 출력
# 정렬을 적용해 줄 맞추기{n:5}
# cnt = 0
# num = int(input("정수 입력: "))
# for i in range(1, num + 1):
#     if i % 7 == 0:
#         print(f"{i:3}", end=' ')
#         cnt += 1
#         if cnt >=10:
#             print()
#             cnt = 0
#
# print()
# 입력 문자열을 뒤집어 출력하기
# 입력:abcdef => fedcba
# eng =["a", "b", "c", "d", "e", "f"]
# for e in range(len(eng)-1, 0 -1, -1):
#     print(eng[e], end='')
#
# text = input("\n문자 입력: ")
# for i in range(len(text)-1, -1, -1):
#     print(text[i], end=' ')

print()

print()
# 입력 받은 문자열에서 대문자는 소문자로, 소문자는 대문자로 변경해서 출력하기
# text = input("\n문자 입력: ")
# new_text = ""
# for e in text:
#     if e.isupper():
#         new_text += e.lower()
#     elif e.islower():
#         new_text += e.upper()
#     else:
#         new_text += e
#
# print(new_text)





# for e in range(0, len(eng)):
#     print(eng[e].upper(), end='')
#
# print()
#
# for e in range(0, len(eng)):
#     print(eng[e].lower(), end='')

# 정수값을 입력 받아 3의 배수, 5의 배수이면 값을 출력, 한 줄에 5개씩 출력
# number = int(input("정수 입력: "))
# cnt = 0
# for i in range(1, number + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         print(f"{i:3}", end=' ')
#         cnt += 1
#         if cnt >=5:
#             print()
#             cnt = 0
#
# print()

# num = int(input("정수 입력: "))
# for e in num:
#     if e % 3 == 0 or e % 5 == 0:
#         print(e, end=' ')
#         cnt += 1
#         if cnt >=5:
#             print()
#             cnt = 0

# 이중 for문
# 입력 받은 수가 10이라면 10 * 10의 행렬 출력
# num = int(input("정수 입력: "))
# for i in range(1,num+1):   # 1 ~ num까지
#     for j in range(1, num+1):
#         print("*", end=' ')
#     print()

# 단일 for문으로 변경해서 출력 해보기
# num = int(input("정수 입력: "))
# cnt = 0
# for i in range(1, num * num + 1):
#     print(f"{i:3}", end=' ')
#     if i % num == 0:
#         print()

# 2 ~ 9단 까지 구구단 출력하기
num =int(input("2~9 중 입력: "))
for i in range(1, num * 9 + 1):
    if i % num == 0:
        print(f"{i:3}", end=' ')