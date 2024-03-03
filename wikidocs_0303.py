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
str = "15.79"
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


# In[4]:


#43
a = "hello"
#내가 쓴 정답
a1 = a.replace("h", "H")
print(a1)
#교안 정답
a2 = a.capitalize()
print(a2)


# In[7]:


#44
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
#몰라서 찾아봤음!


# In[15]:


#45
file_name = "보고서.xlsx"
#내가 쓴 정답
file_name.endswith("xlsx" or "xls")
#교안 정답
file_name.endswith(("xlsx", "xls"))


# In[17]:


#46
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")


# In[22]:


#47
a = "hello world"
a.split()


# In[25]:


#48
ticker = "btc_krw"
ticker.split("_")


# In[26]:


#49
date = "2020-05-01"
date.split("-")


# In[27]:


#50
data = "039490     "
data.rstrip()

