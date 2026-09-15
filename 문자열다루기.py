# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음(전부 문자열)
# "", '', """ """, ''' '''
# 인덱싱과 슬라이싱
# 인덱싱은 인덱스로 원하는 값을 추출
text = "안녕하세요. 파이썬 입니다"
print(text[0]) # 안
print(text[7]) # 파
print(text[-1]) # 다

print(text[7:11])
print(text[::-1]) # 처음부터 마지막까지 역순으로 출력
print(text[:5])

from datetime import  datetime
current_year = datetime.now().year

# 주민등록번호를 입력 : 010222-3164414
# id = input("주민 번호를 입력: ")
# key = int(id[7])
# year = int(id[:2])
# mon =int(id[2:4])
# day =int(id[4:6])
# # 생년월일 : 2001년2월22일
# if key == 1 or key == 2:
#     year += 1900
#     print(f"{year + 1900}년{mon:02}월{day:02}일")
# else:
#     year += 2000
#     print(f"{year + 2000}년{mon:02}월{day:02}일")
# # 성별 : 남성
# if key == 1 or key == 3:
#     print("성별 : 남성")
# else:
#     print("성별 : 여성")
# # 나이 : 25살
# print(f"나이 : {current_year - year}살")

# 대소문자 바꾸기: upper() lower()
a = "Hello Python Program.."
print(a.upper())
print(a.lower())

# isupper(), islower()
# 입력받은 문자열에서 소문자는 대문자로 대문자는 소문자로 변경
for e in a:
    if e.islower():
        print(f"{e.upper()}", end="")
    elif e.isupper():
        print(f"{e.lower()}", end="")
    else:
        print(e, end="")
print()
# 문자열 변경 : replace("", "")
input_str = "Hello Python Program"
new_str = input_str.replace("Python", "JavaScript")
print(new_str)

# 문자 개수 세기 : count
text = "Google kakao naver openAI oole"
print(text.count("a"))

# 문자열 길이 : len()
text = "Hello World"
print(len(text))

# 문자열 찾기 : find() rfind() index()
# find() : 찾은 부분 문자열의 첫 번째 인덱스를 반환. 부분 문자열을 찾지 못하면 -1을 반환
# index() : 찾은 부분 문자열의 첫 번째 인덱스를 반환. 부분 문자열을 찾지 못하면 ValueError 예외를 발생시킴
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장")) # 0
print(phrase.rfind("가장")) # 뒤에서 부터 찾지만 인덱스는 앞에서 부터

print(phrase.index("포기"))

print(phrase.find("나에게")) # 찾는 결과가 없으면 -1
# print(input_b.index("나에게")) 해당 단어가 없으므로 에러가 발생

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 양옆의 공백제거
# strip(): 양쪽 공백 제거
# lstrip(): 왼쪽 공백 제거
# rstrip(): 오른쪽 공백 제거
input_a ="""
    안녕하세요.
문자열 함수를 알아 봅니다

    """
print(input_a.strip())