#!/usr/bin/env python
# coding: utf-8

# # 파이썬 시작하기

# In[ ]:


#01
print("Hello World")
print('Hello World')

#문자열은 따옴표, 혹은 작은 따옴표로 print 한다


# In[ ]:


#02
print("Mary's cosmetics")
#문자열 내에 작은 따옴표가 있을 경우 큰 따옴표로 print 한다


# In[ ]:


#03
print('신씨가 소리질렀다. "도둑이야".')
#문자열 내에 큰 따옴표가 있을 경우 작은 따옴표로 print 한다


# In[ ]:


#04
print('C:\Windows')
#운영체제에 따라 역슬래시(\)가 원화로 표현될 수 있음


# In[ ]:


#05
print("안녕하세요.\n만나서\t\t반갑습니다.")
#'\n'은 줄바꿈, '\t'는 탭 


# In[ ]:


#06
print ("오늘은", "일요일")
#여러 개 print 하고 싶을 경우 쉼표(,)로 구분하기


# In[ ]:


#07
#내가 생각한 답
print("naver"";kakao"";sk"";samsung")
#교안 답안 
print("naver", "kakao", "sk", "samsung", sep=";")
#sep=";"은 공백 대신 세미콜론(;) 출력해달라는 인자 


# In[ ]:


#08
print("naver", "kakao", "sk", "samsung", sep="/")


# In[ ]:


#09
print("first", end=" "); print("second")
#줄바꿈없이 여러 문자열을 출력할 경우 end="" 써주기 


# In[ ]:


#10
print(5/3)


# # 파이썬 변수

# In[ ]:


#11
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

#'총 평가금액'이라고 띄어서 작성하면 에러 발생
# 바인딩 = 변수의 값을 지정해준다(선언)


# In[ ]:


#12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79


# In[ ]:


#13
#내가 쓴 정답
s = "hello!"
t = " python"
print(s + t)

#교안 정답
s = "hello"
t = "python"
print(s+"!", t)


# In[ ]:


#14
#예상 정답 = 8 
2 + 2 * 3 


# In[ ]:


#15
a = "132"
print(type(a))
# int = 정수, str = string = 문자열 = 텍스트 


# In[ ]:


#16
num_str = "720"  #형변환이라고 한다
num_int = int(num_str)
#문자열인 num_str을 정수로 변환해주고, 그걸 num_int라고 선언할게 
print(num_int+1, type(num_int))
#정수로 바뀌었기 때문에 +1과 같은 연산도 가능하다 


# In[ ]:


#17
num = 100
num_str = str(num)
#num_str이 문자열로 잘 바뀌었는지 type을 찍어보자 
print(num_str, type(num_str))


# In[ ]:


#18
str = "15.79"print
result = float(str)
print(result, type(result))


# In[ ]:


#19
year = "2020"
int_year = int(year)
#1차 정답 print(year, year+1, year-2) 오답!
#2차 정답 
print(int_year, int_year-1, int_year-2)
#교안 정답 
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1)  # 2019


# In[ ]:


#20
에어컨 = 48584
총금액 = (에어컨 * 36)
print(총금액)


# # 파이썬 문자열

# In[ ]:


#21
letters = "python"
letters[0], letters[2]
#교안 정답
print(letters[0], letters[2])


# In[ ]:


#22
license_plate = "24가 2210"
#1차 정답 (오답) license_plate[-4:-1]
license_plate[-4:]
#교안 정답
print(license_plate[-4:])


# In[ ]:


#23
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4], sep="")
#교안 정답
print(string[::2])
#슬라이싱 할 때 '시작 인덱스 : 끝 인덱스 : 오프셋' 지정 가능 


# In[ ]:


#24
string = "PHTHON"
reverse = string[::-1]
print(reverse)

#교안 정답
string = "PHTHON"
print(string[::-1])


# In[ ]:


#25
phone_number = "010-1111-2222"
replace_number = phone_number.replace("-", " ")
print(replace_number)


# In[ ]:


#연습용
a = '1234'
a1 = a.replace("1", "5")
print(a1)


# In[ ]:


#26
phone_number = "010-1111-2222"
replace_number = phone_number.replace("-", "")
print(replace_number)


# In[ ]:


#27
url = "http://sharebook.kr"
#내가 제출한 정답
print(url[-2:])
#교안 정답
url_split = url.split('.')
print(url_split[-1])


# In[ ]:


#28
lang = 'python'
lang[0] = 'P'
print(lang)
#한 번 선언(바인딩)이 되면, 바꿀 수 없다. 고로 'p'로 이미 선언 되었기 떄문에 'P'로 다시 선언할 수 없다


# In[ ]:


#29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)


# In[ ]:


#30
#string = string.replace('b', 'B')라고 선언하지 않아서 오류 발생할 것 같다
string = 'abcd'
string.replace('b', 'B')
print(string)
#문자열은 변경할 수 없는 자료형이어서 원본 그대로 출력해준다

string = 'abcd'
string = string.replace('b', 'B')
print(string)
#예상대로 이렇게 하니까 B로 출력이 된다


# In[ ]:


#31
a = "3"
b = "4"
print(a + b)
#예상 : 3 4 라고 출력 될 것이다


# In[ ]:


#32
print("Hi" * 3)
# 예상 : HiHiHI 라고 출력 될 것이다


# In[ ]:


#33
print("-" * 80)


# In[ ]:


#34
t1 = "python"
t2 = "java"
t = t1 + " " + t2 + " "
print(t * 5)


# In[ ]:


#35
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))


# In[ ]:


#36
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))


# In[ ]:


#37
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')


# In[ ]:


#38 
상장주식수 = "5,969,782,550"
콤마없애기 = 상장주식수.replace(",", "")
print(콤마없애기)
정수타입 = int(콤마없애기)
print(정수타입, type(정수타입))


# In[ ]:


#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])


# In[ ]:


#40
data = "   삼성전자    "
공백없음 = data.strip()
print(공백없음)


# In[ ]:


#41
ticker = "btc_krw"
ticker1 = ticker.upper
print(ticker.upper())


# In[ ]:


#42
ticker = "BTC_KRW"
ticker2 = ticker.lower
print(ticker.lower())


# In[ ]:


#43
a = "hello"
#내가 쓴 정답
a1 = a.replace("h", "H")
print(a1)
#교안 정답
a2 = a.capitalize()
print(a2)


# In[ ]:


#44
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
#몰라서 찾아봤음!


# In[ ]:


#45
file_name = "보고서.xlsx"
#내가 쓴 정답
file_name.endswith("xlsx" or "xls")
#교안 정답
file_name.endswith(("xlsx", "xls"))


# In[ ]:


#46
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")


# In[ ]:


#47
a = "hello world"
a.split()


# In[ ]:


#48
ticker = "btc_krw"
ticker.split("_")


# In[ ]:


#49
date = "2020-05-01"
date.split("-")


# In[ ]:


#50
data = "039490     "
data.rstrip()


# # 파이썬 리스트

# ## 리스트 생성

# In[ ]:


#51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]


# In[ ]:


#52
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)


# In[ ]:


#53
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)


# In[ ]:


#54
#방법1
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove("럭키")
print(movie_rank)
#방법2
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)


# In[ ]:


#55
#내가 작성한 답안 = 결과는 동일한데, 틀린 건지 점검 필요
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)
#교안 답안
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)


# In[ ]:


#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)


# In[ ]:


#57
nums = [1, 2, 3, 4, 5, 6, 7]
print("max:", max(nums))
print("min:", min(nums))


# In[ ]:


#58
nums = [1, 2, 3, 4, 5]
print(sum(nums))


# In[ ]:


#59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
#1차 답안 (오답)
#print(count(cook))

#2차 답안
print(len(cook))


# In[ ]:


#60
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))


# In[ ]:


#61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])


# In[ ]:


#62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])


# In[ ]:


#63 
#외워서 풀었는데 이해는 잘 안 됐음 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])


# In[ ]:


#64
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)


# In[ ]:


#65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])


# In[ ]:


#66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#내가 쓴 정답 (오답)
#print(" ".join(interest))
print(" ".join(interest))


# In[ ]:


#67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))


# In[ ]:


#68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))


# In[ ]:


#69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)


# In[ ]:


#70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort(reverse=True)
print(data)


# # 파이썬 튜플

# In[ ]:


#71
my_variable = ()
print(type(my_variable))


# In[ ]:


#72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')


# In[ ]:


#73
#내가 쓴 답안 (오답) -> 1만 쓰면 정수로 인식함
#t = (1)
#type(t)
t = (1,)
type(t)


# In[ ]:


#74
#오류 발생 원인 추측 : 튜플은 값을 변경할 수 없다 
t = (1, 2, 3)
t[0] = 'a'


# In[ ]:


#75
#원칙적으로는 튜플에 괄호를 함께 데이터를 정의해야 하지만, 편의상 괄호 없이도 동작함!
t = 1, 2, 3, 4
type(t)


# In[ ]:


#76
# 튜플은 값을 변경할 수 없으니, 리스트와 달리 t.upper 함수가 동작하지 않는다.
# 새로운 튜플을 만들고 t라는 변수를 업데이트 하면 기존의 튜플은 자동으로 삭제된다.
t = ('a', 'b', 'c')
t = ('A', 'B', 'C')
print(t)


# In[ ]:


#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)


# In[ ]:


#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data)


# In[ ]:


#79
#오류 발생할 줄 알았는데 아니었음 
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)


# In[ ]:


#80
#몰라서 정답 참고함!
a = range(2, 99, 2)
print(tuple(a))


# # 파이썬 딕셔너리

# In[ ]:


#81
#몰라서 구글링함!!!!
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)


# In[ ]:


#82
#맞긴 했는데 제대로 이해는 못함 그냥 외웠음
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)


# In[ ]:


#83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)


# In[ ]:


#84
temp = {}
type(temp)


# In[ ]:


#85
temp = {'메로나': '1000', '폴라포': '1200', '빵빠레': '1800'}
type(temp)


# In[ ]:


#86
temp = {'메로나': '1000', '폴라포': '1200', '빵빠레': '1800'}
temp['죠스바'] = '1200'
temp['월드콘'] = '1500'
print(temp)


# In[ ]:


#87
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
#내가 쓴 정답
print('메로나 가격: ', ice.get('메로나')) 
#교안 정답
print("메로나 가격: ", ice["메로나"])


# In[ ]:


#88
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)


# In[ ]:


#89
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice['메로나']
print(ice)


# In[ ]:


#90
#오류 발생 원인 추측 : 가격이 선언이 안 되어서 ?
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#가격을 임의로 지정해주니 오류가 발생하지 않는다 
icecream['누가바'] = 1500
print(icecream)


# In[ ]:


#91
inventory = {"메로나": [300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
type(inventory)


# In[ ]:


#92
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
#거의 근접했는데 대괄호 위치 때문에 오답
#print(inventory["메로나"[0]], "원")
print(inventory["메로나"][0], "원")


# In[ ]:


#93
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][1], "개")


# In[ ]:


#94
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory["월드콘"] = [500, 7]
print(inventory)


# In[ ]:


#95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#내가 쓴 정답
print(icecream.keys())
#교안 정답
ice = list(icecream.keys())
print(ice)


# In[ ]:


#96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)


# In[ ]:


#97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(sum(ice))
#교안 정답 = 선언하지않고 바로 출력
print(sum(icecream.values()))


# In[ ]:


#98
#구글링해서 알았음!
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)


# In[ ]:


#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
#내가 쓴 정답 (오답) -> 그냥 묶으면 될 줄 알았지만, 오답
result = {keys : vals}
print(result)
#교안 정답
result = dict(zip(keys, vals))
print(result)


# In[ ]:


#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)


# # 파이썬 분기문

# In[ ]:


#101
#파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
#bool 타입!


# In[ ]:


#102
#출력 결과 예상 : False (정답)
print(3 == 5)


# In[ ]:


#103
#출력 결과 예상 : True (정답)
print(3 < 5)


# In[ ]:


#104
#출력 결과 예상 : True (정답)
x = 4
print(1 < x < 5)


# In[ ]:


#105
#출력 결과 예상 : True (정답)
print ((3 == 3) and (4 != 3))


# In[ ]:


#106
#에러 발생 원인 설명 : 지원하지 않는 연산자
print(3 => 4)


# In[ ]:


#107
#코드 출력 결과 예상 : False (오답)
if 4 < 3:
    print("Hello World")
# 조건을 만족하지 않아 아무 결과도 출력되지 않는다. 


# In[ ]:


#108
#코드 출력 결과 예상 : Hi, there (정답)
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")


# In[ ]:


#109
#코드 출력 결과 예상 : 열이 맞지 않아 에러 발생 (오답)
if True :
    print ("1")
    print ("2")
else :
    print("3")
#여기까지가 if 문인데, True라고 이미 명시되어 있으니, 1과 2를 print하고 else 문은 생략
print("4")
#4를 출력하라고 했으니 1, 2, 4가 출력되는 것


# In[ ]:


#110
#코드 출력 결과 예상 : 5 (오답)
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
#3이 출력되는 이유 = if True라고 해서 들어가봤더니 if False가 나옴. 고로 else에 해당하는 3이 출력되는 것이고 1, 2는 출력되지 않는다


# In[ ]:


#111
#내가 쓴 정답 : 출력하라는 말이 아니었다 (오답)
a = "안녕하세요"
print(a * 2)
#교안 정답
user = input("입력:")
print(user * 2)


# In[ ]:


#해설 영상 정답
data = input("")
print(data * 2)


# In[ ]:


#112
#내가 쓴 정답 : 에러 발생(정수가 아니어서 안 된다고 한다)
#data = input("숫자를 입력하세요:")
#print(data +10)

#교안 정답
user = input("숫자를 입력하세요: ")
print(10 + int(user))


# In[ ]:


#113
user = input("")
if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")


# In[ ]:


#114
#내가 쓴 정답 : 동일하게 작동함
user = input("입력값: ")
if int(user) + 20 > 255:
    print("255")
else:
    print(20 + int(user))


# In[ ]:


#교안 정답
user = input("입력값: ")
num = 20 + int(user)
if num > 255:
    print(255)
else:
    print(num)


# In[ ]:


#115
user = input("입력값: ")
num = int(user) - 20
if num > 255:
    print(255)
elif num < 0:
    print(0)
else :
    print(num)


# In[ ]:


#116

#내가 쓴 if 문 -> 얼렁뚱땅 썼는데 역시나 오답
#if time(user) == "%h:00" :
#if time[user] == "%h:00":

#교안 정답
time = input("현재시간: ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")


# In[ ]:


#117
#1차 시도 = input을 두 번 하게 설계되었다. 왜지???
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if input(user) in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")


# In[ ]:


#2차 시도 (정답)
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")


# In[ ]:


#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("종목명: ")
if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")


# In[ ]:


#119
#딕셔너리라고 user(keys)라고 작성해야 하나 싶었는데 그대로 작성하면 되는 거였음!
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가 좋아하는 계절은: ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")


# In[ ]:


#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은? ")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")


# In[ ]:


#121
user = input("")
if user.islower():
    print(user.upper())
else:
    print(user.lower())


# In[ ]:


#122
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")


# In[ ]:


#123
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")


# In[ ]:


#124
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)


# In[ ]:


#125
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")


# In[ ]:


#126
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")


# In[ ]:


#127
주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")


# In[ ]:


#128
주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")


# In[ ]:


#129
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")


# In[ ]:


#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")


# # 파이썬 반복문

# In[ ]:


#131
#출력 결과 예측 : 사과, 귤, 수박이 차례대로 출력된다. (정답)
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)


# In[ ]:


#132
#출력 결과 예측 : "사과", "귤", "수박"으로 출력된다 (오답)
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
#for문의 핵심은 들여쓰기된 코드가 자료구조에 저장된 개수만큼 반복된다.


# In[ ]:


#133
for 변수 in ["A", "B", "C"]:
  print(변수)

print("A")
print("B")
print("C")


# In[ ]:


#134
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

print("출력:", "A")
print("출력:", "B")
print("출력:", "C")


# In[ ]:


#135
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
    
변수 = "A"
b = 변수.lower()
print("변환:", b)
변수 = "B"
b = 변수.lower()
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)


# In[ ]:


#136
#내가 쓴 정답
for 변수 in [10, 20, 30]:
  print("변수 =", 변수)
#교안 정답
리스트 = [10, 20, 30]
for 변수 in 리스트:
  print(변수)


# In[ ]:


#137
t1 = (10, 20, 30)
for 변수 in (10, 20, 30):
    print(변수)


# In[ ]:


#138
list = [10, 20, 30]
for 변수 in list:
    print("-------")


# In[ ]:


#139
print("++++")
list = [10, 20, 30]
for 변수 in list:
    print(변수)


# In[ ]:


#140
list = [1, 2, 3, 4]
for 변수 in list:
    print("-------")


# In[ ]:


#141
리스트 = [100, 200, 300]
for 변수 in 리스트:
    print(변수 + 10)


# In[ ]:


#142
리스트 = ["김밥", "라면", "튀김"]
for 변수 in 리스트:
    print("오늘의 메뉴:", 변수)


# In[ ]:


#143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 변수 in 리스트:
    print(len(변수))


# In[ ]:


#144
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수, len(변수))


# In[ ]:


#145
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수[0])


# In[ ]:


#146
리스트 = [1, 2, 3]
for 변수 in 리스트:
    print("3 *", 변수)
    #교안에 적힌 다른 답안
    print("3 x " + str(변수))


# In[ ]:


#147
리스트 = [1, 2, 3]
for 변수 in 리스트:
    print("3 *", 변수, "=", 3 * 변수)
#교안에 적힌 다른 답안
리스트 = [1, 2, 3]
for 변수 in 리스트:
  print("3 x {} = {}".format(변수, 3 * 변수))


# In[ ]:


#148
#내가 쓴 정답
리스트 = ["가", "나", "다", "라"]
리스트 = 리스트[1:]
for 변수 in 리스트:
    print(변수)
    
#교안 정답
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[1:]:
  print(변수)


# In[ ]:


#149
#내가 쓴 정답
리스트 = ["가", "나", "다", "라"]
리스트 = 리스트[::2]
for 변수 in 리스트:
    print(리스트)
#교안 정답
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[::2]:
  print(변수)


# In[ ]:


#150
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[: :-1]:
  print(변수)


# In[ ]:


#151
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 < 0 : 
        print(변수)


# In[ ]:


#152
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
    if 변수 % 3 == 0:
        print(변수)


# In[ ]:


#153
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
    if 변수 % 3 == 0 and 변수 < 20:
        print(변수)


# In[ ]:


#154
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
    if len(변수) >= 3:
        print(변수)


# In[ ]:


#155
#오답
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.isupper() == True:
        print(변수)
        
#정답
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper():
    print(변수)


# In[ ]:


#156
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.islower():
        print(변수)


# In[ ]:


#157
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수[0].upper(), 변수[1:])


# In[ ]:


#158
#1차 시도
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
    print(변수.split("."))
    
#2차 시도 (교안 참고 / 분할 한 뒤에 추출)
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
    split = 변수.split(".")
    print(split[0])


# In[ ]:


#159
#1차 시도 
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".")
    if split[1] == "h":
        print(변수)


# In[ ]:


#160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    split = 변수.split(".")
    if split[1] == "h" or "c":
        print(변수)


# In[ ]:


#161
for i in range(100):
    print(i)


# In[ ]:


#162
for i in range(2002, 2050, 4):
    print(i)
    
#교안 정답 = 2051
for x in range(2002, 2051, 4) :
    print (x)


# In[ ]:


#163
for i in range(1, 30, 3) :
    print (i + 2)


# In[ ]:


#164
for i in range(99, 0, -1) :
    print (i)


# In[ ]:


#165
for i in range(10):
    print(i / 10)


# In[ ]:


#166
for i in range(1, 10):
    print("3 * ", i, "=", i * 3)


# In[ ]:


#167
for i in range(1, 10, 2):
    print("3 * ", i, "=", i * 3)


# In[ ]:


#168
for i in range(1, 10):
    print("합 : ", sum(i))
    
#교안 정답
hab = 0
for i in range(1, 11):
    hab += i
print ("합 :", hab)


# In[ ]:


#169
hab = 0
for i in range(1, 11, 2):
    hab += i
print ("합 :", hab)


# In[ ]:


#170
#1차 시도
x = 1
for i in range(1, 11):
    x *= i
print (x)

# + 누락
x = 1
for i in range(1, 11):
    x *= i
print (x)


# In[ ]:


#171
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])


# In[ ]:


#172
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i, price_list[i])


# In[ ]:


#173
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(3-i, price_list[i])

#교안 다른 정답
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])


# In[ ]:


#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90 + i * 10, price_list[i])


# In[ ]:


#175
my_list = ["가", "나", "다", "라"]
for i in range(0, 3):
    print(my_list[i], my_list[i+1])


# In[ ]:


#176
my_list = ["가", "나", "다", "라", "마"]
for i in range(0, 3):
    print(my_list[i], my_list[i+1], my_list[i+2])


# In[ ]:


#177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])


# In[ ]:


#178
#내가 쓴 정답 (오답)
my_list = [100, 200, 400, 800]
for i in range(len(my_list) +1):
    print(my_list[i + 1] - my_list[i])
    
#교안 정답 
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))


# In[ ]:


#179
#잘 모르겠어서 답안을 봤는데 abs가 적혀 있어서 일단 패스
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)


# In[ ]:


#180
#교안 정답 (일단 패스)
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])


# In[ ]:


#181
apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ]


# In[ ]:


#182
stock = [ ["시가", 100, 200, 300], ["종가", 80, 210, 330] ]


# In[ ]:


#183
stock = {
    "시가" : [100, 200, 300], "종가" : [80, 210, 330]
}


# In[ ]:


#184
stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200] }


# In[ ]:


#185
#내가 쓴 답(오답)
apart = [ [101, 102], [201, 202], [301, 302] ]
print(
    apart[0][0], "호", 
    apart[0][1], "호", 
    apart[1][0], "호", 
    apart[1][1], "호",
    apart[2][0], "호", 
    apart[2][1], "호", 
)

#교안 정답
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")


# In[ ]:


#186
#잘 몰라서 답안 확인함
for row in apart[::-1]:
    for col in row:
        print(col, "호")


# In[ ]:


#187
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")


# In[ ]:


#188
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
        print("--------")


# In[ ]:


#189
for row in apart:
    for col in row:
        print(col, "호")
    print("-----")


# In[ ]:


#190
for row in apart:
    for col in row:
        print(col, "호")
print("-----")


# In[ ]:


#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for line in data:
    for column in line:
        print(column * 1.00014)


# In[ ]:


#192
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for line in data:
    for column in line:
        print(column * 1.00014)
    print("-" * 4)


# In[ ]:


#193
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)


# In[ ]:


#194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)


# In[ ]:


#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
    print(row[3])


# In[ ]:


#196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] > 150:
        print(i[3])


# In[ ]:


#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[0:]:
    if i[3] >= i[0] :
        print(i[3])


# In[ ]:


#198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

#1차 답안 (교안 참고)
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
    
#2차 답안(교안 참고)
volatility = []
for i in range(1, len(ohlc)):
    volatility.append(ohlc[i][1]-ohlc[i][2])
print(volatility)


# In[ ]:


#199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[0:]:
    if i[3] > i[0]:
        print(i[1] - i[2])


# In[ ]:


#200
#내가 쓴 정답 (오답)
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[0:]:
    print(sum(i[0]-i[3]))

#교안 정답
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])


# In[ ]:


#201
def print_coin():
    print("비트코인")


# In[ ]:


#202
print_coin()


# In[ ]:


#203
for i in range(100):
    print_coin()


# In[ ]:


#204
def print_coins():
    for i in range(100):
        print("비트코인")


# In[ ]:


print_coins()


# In[ ]:


#205
hello()
def hello():
    print("Hi")


# In[ ]:


def hello():
    print("Hi")


# In[ ]:


hello()


# In[ ]:


#206
#실행 결과 추측 : A, C, A가 출력될 것이다.  (오답)
def message() :
    print("A")
    print("B")

message()
print("C")
message()


# In[ ]:


#207
#출력 결과 예상 : A C B
print("A")

def message() :
    print("B")

print("C")
message()


# In[ ]:


#208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

#출력 결과 예상  : A C B E D


# In[ ]:


#209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

#추출 결과 예측 B A 


# In[ ]:


#210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

#추출 결과 예측 B C B C B C A 


# In[ ]:


#211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

#추출 결과 예상 : 안녕 HI


# In[ ]:


#212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

#추출 결과 예상 : 7 15


# In[ ]:


#213
def 함수(문자열) :
    print(문자열)

함수()
#오류 발생 원인 : 문자열을 불러오는 함수를 정의했는데 함수()로 호출해서?
#교안 정답 : 함수를 호출할 때 하나의 파라미터를 입력해야 한다


# In[ ]:


#214
def 함수(a, b) :
    print(a + b)

("안녕", 3)

#에러 발생 원인 : 3이 아니라 문자열을 불러올 수 있어서
#교안 정답 : 문자열과 숫자를 더할 수 없기 때문

함수("안녕", "반가워")
함수(2, 3)


# In[ ]:


#215
#내가 작성한 정답 (오답) -> string 누락
def print_with_smile():
    print(  ":D")
    
print_with_smile()


# In[ ]:


#216
def print_with_smile (string) :
    print (string + ":D")
    
print_with_smile("안녕하세요 ")


# In[ ]:


#217
def print_upper_price(int) :
    print(int * 1.3)

print_upper_price(10000)


# In[ ]:


#218
#1차 시도 =  (a, b) 누락
def print_sum():
    print(a + b)
    
def print_sum(a, b):
    print(a + b)


# In[ ]:


#219
def print_arithmetic_operation(a, b) :
    print(
        a + b, a - b, a * b, a / b
    )
    
print_arithmetic_operation(3, 4)


# In[ ]:


#교안 정답
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

print_arithmetic_operation(3, 4)


# In[ ]:


#220
#내가 쓴 정답 : 에러 발생 
def print_max(a, b, c) :
    if a > b and a > c :
        print(a)
    elif b > a and b > c :
        print(b)
    else c > a and c > b :
        print(c)

print_max(2, 3, 4)


# In[ ]:


#else를 elif로 바꾸고 else를 추가
def print_max(a, b, c) :
    if a > b and a > c :
        print(a)
    elif b > a and b > c :
        print(b)
    elif c > a and c > b :
        print(c)
    else : 
        print("확인이 불가합니다")

print_max(2, 3, 4)


# In[ ]:


#교안 정답
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

print_max(3, 3, 3)


# In[ ]:


#221
#내가 쓴 정답 : 에러 발생
def print_reverse("a") :
    print(a.reverse())

print_reverse("python")


# In[ ]:


#교안 정답
def print_reverse(a) :
    print(a[::-1])

print_reverse("python")


# In[ ]:


#222
def print_score(a):
    print(sum(a) / len(a))

print_score([40, 50, 60])


# In[ ]:


#223
def print_even(a):
    print(a[1::2])

print_even([1, 2, 3, 4, 5, 8, 19])


# In[ ]:


#교안 정답
def print_even (my_list) :
    for a in my_list :
        if a % 2 == 0 :
            print(a)
            
print_even([2, 4, 5, 7, 8, 9])


# In[ ]:


#224
def print_keys(a) :
    print(a.keys())

print_keys({"이름" : "김말똥", "나이" : 30, "성별" : 0})


# In[ ]:


#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(a) :
    print(my_dict[a])

print_value_by_key("10/27")


# In[1]:


#226
def print_5xn(s) :
    while len(s) != 0:
        print(s[:5])
        s = s[5:]
    
print_5xn("아이엠어보이유알어걸")


# In[ ]:


#교안 정답
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])


# In[2]:


#227
def print_mxn(a, b) :
    while len(a) != 0:
        print(a[:b])
        a = a[b:]

print_mxn("아이엠어보이유알어걸", 3)


# In[ ]:


#교안 정답
def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])


# In[ ]:


#228
#내가 쓴 정답 (오답)
def calc_monthly_salary(annual_salary) :
    print(annual_salary / 12)

calc_monthly_salary(12000000)

#교안 정답
def calc_monthly_salary(annual_pay) :
    monthly_pay = int(annual_pay / 12)
    return monthly_pay


# In[ ]:


#229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

# 추측 : "왼쪽 : 100", "오른쪽 : 200" (정답)


# In[ ]:


#230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

#추측 : "왼쪽 : 200", "오른쪽 : 100" (정답)


# In[ ]:


#231
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)

# 추측 : 에러 발생
# 이유 : result는 로컬변수인데 글로벌에서 호출했기 때문
# 오류를 해결하려면 def 안에 print(result)를 넣는다

def n_plus_1 (n) :
    result = n + 1
    print (result)
    
n_plus_1(3)


# In[ ]:


#232
#내가 쓴 답안 = 공백 존재
def make_url(a) :
    print("www.", a, ".com")
    
make_url("naver")


# In[ ]:


#교안 답안
def make_url(string) :
    return "www." + string + ".com"

make_url("naver")


# In[ ]:


#233
#1차 답안
def make_list(a) :
    print([a])
    
make_list("abcd")


# In[ ]:


#교안 답안 = list 함수 
def make_list (string) :
    return list(string)
    
make_list("abcd")


# In[ ]:


#234
#교안 답안
def pickup_even(a) :
    answer = []
    for i in a :
        if i % 2 == 0 :
            answer.append(i)
    return answer

pickup_even([3, 4, 5, 6, 7, 8])


# In[ ]:


#235
#내가 쓴 답안
def convert_int(a) :
    print(a.replace(",", ""))
    
convert_int("1,234,567")


# In[ ]:


#교안 정답
def convert_int(a) :
    return int(a.replace(",", ""))
    
convert_int("1,234,567")


# In[ ]:


#236
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

#실행 결과 예측 : def 밖에 있으니 print(C)만 동작해서 "C"일 줄 알았다

#교안 정답
a = 10 + 4 = 14
b = 14 + 4 = 18
c = 18 + 4 = 22
print(c) = 22


# In[ ]:


#237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#결과 예측 : 22 (정답)


# In[ ]:


#238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

#결과 예측 : a = 14, c = 140 -> 140


# In[ ]:


#239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#결과 예측 : 16


# In[ ]:


#240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

#결과 예측 : 28

