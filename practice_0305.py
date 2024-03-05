#!/usr/bin/env python
# coding: utf-8

# # Q1 다음 코드의 결괏값은 무엇일까?
# ```
# a = 'Life is too short, you need python'
# if 'wife' in a: print('wife')
# elif 'python' in a and 'you' not in a : print('python')
# elif 'shirt' not in a : print('shirt')
# elif 'need' in a: print('need')
# else: print('none')
# ```

# In[3]:


#wife 없으니 생략
#python은 있는데 you가 있으면 안 된다고 하니 패스
#shirt가 없으니 출력
#need도 있으니 출력
#고로 shirt와 need가 출력될 것이다.

#오답 ! 순서대로 처리하다가 해당하는 elif 절이 있으니 하나만 출력 후 종료된 것으로 추정 


# # Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
# ```
# result = 0
# i = 1
# while i <= 1000:
#     if ?????  # 3으로 나누어 떨어지는 수는 3의 배수
#         result += i
#     i += 1
# print(result) # 166833 출력
# ```

# In[9]:


result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:  # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1
print(result)  # 166833 출력


# # Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# ```
# *
# **
# ***
# ****
# *****
# ```

# In[10]:


i = 1
while i <= 5:
    print('*' * i)
    i += 1


# # Q4 for문을 사용해 1부터 100까지의 숫자를 출력해보자
# ```
# for i in ???
#     print(i)
# ```

# In[11]:


#문제를 착각하고 while 문으로 작성해버림
i = 1
while i <= 100:
    print(i)
    i += 1


# In[15]:


for i in range(1, 101):
    print(i)


# # Q5 A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# for문을 사용하여 A 학급의 평균 점수를 구해보자.
# ```
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += ???? # A학급의 점수를 모두 더한다.
# average = ???? # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
# print(average)
# ```

# In[20]:


A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score  # A학급의 점수를 모두 더합니다.
average = total / len(A)  # 평균을 구하기 위해 총 점수를 총 학생수로 나눕니다.
print(average)


# # Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# ```
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
# if n % 2 == 1:
#     result.append(n*2)
# ```
# 위 코드를 리스트 내포(list comprehension)을 사용하여 표현해보자.
# ```
# numbers = [1, 2, 3, 4, 5]
# result = ?????
# print(result)
# ```

# In[22]:


#몰라서 구글링으로 찾아봤음,, 근데 이해가 잘 안 된다. 질문 필요 
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)


# ```
# "뭔가 하게 되면 나는 어떤 식으로든 성장한다."
# - 소설가 김연수
# ```
