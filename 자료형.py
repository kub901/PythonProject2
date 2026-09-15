# 자료형(data type)은 데이터를 저장하는 방식과 연산할 수 있는 방법을 정의하는 데이터의 형태를 의미
# python에서는 변수를 선언할 때 자료형을 명시 하지 않아도 되며, 값이 할당될 때 자동으로 자료형이 결정됨
text = "안녕하세요. 파이썬입니다"
print(type(text))
text = 100
print(type(text))
text = 3.14
print(type(text))
text = None
print(type(text))
text = False
print(type(text))

# 문자열: 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음, "", '', """ """,''' '''
text1 = "안녕하세요. 파이썬 입니다."
print(text1)
print(text1[0]) # 해당 인덱스의 내용을 추출
print(text1[7:10]) #슬라이싱
print(text1 + "!!!!!!")
print(text1 * 3)

# 숫자형(number) : 정수, 실수, 복소수형이 있음, 사칙연산 가능
num1 = 10
num2 = 4
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

# 불리언(boolean) : 참과 거짓 두가지의 값만 가짐
# age = int(input("나이를 입력: "))
# is_adult = False
# if age >= 18:
#     is_adult = True
# else:
#     is_adult = False

print(bool(1))   # true
print(bool(-1))  # true
print(bool(0))   # False
print(bool(""))  # False
print(bool(" ")) # true
print(bool(None))# False

# 형변환: 데이터를 다른 자료형으로 변환할 때 사용
print("100"+str(200))
print(int("100")+200)

# 사용자에게 나이를 입력받아 다음 조건에 따라 메세지를 출력하는 프로그램을 작성하세요
# 19세 이상이면 "성인입니다." 출력
# 19세 미만이면 "미성년자입니다." 출력
# age = int(input("나이 입력: "))
# if age >= 18:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")
# # sentence = "python programing is fun"
# # 첫 6글자("python")만 출력하세요.
# sentence = "python programming is fun"
# print(sentence[0:7])




























