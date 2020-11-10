'''
* 다음 조건을 만족하는 함수 powerMod(a,N,M)을 작성하시오. 

(단, 입력 N에 대한 다항식 시간 알고리즘이 되도록 작성해야 하며, 이진법 표현을 구할 때 필요한 함수는 직접 구현해서 사용해야 함)

입력: a 자연수
입력: N, M은 60자리 이상 (70자리이하의) 자연수 

출력: a**N % M (즉, a의 N제곱을 M으로 나눈 나머지)

Hint1)
import random
random.randint(a,b)를 이용하여 조건에 맞는 N,M을 생성

Hint2)
자연수의 이진법 전개와 지수법칙을 이용
'''

import random
import sys
sys.setrecursionlimit(10000) # 재귀한도를 늘려줍니다.

max_digit_60 = pow(10, 59) # 60자리수의 첫번째
max_digit_70 = pow(10, 70) # 71자리수의 첫번째
a = random.randint(1, max_digit_70)
N = random.randint(max_digit_60, max_digit_70)
M = random.randint(max_digit_60, max_digit_70)

def Binary(num, list=[]):
    if num > 0:
        list.append(num % 2)
        return Binary(num // 2)
    else:
        return ''.join(map(str, list[::-1]))

def powerMod(a, N, M):
    if N == 1:
        return a % M
    r = powerMod(a, N // 2, M)
    r = r * r % M
    if(N & 1) == 1: # 홀수 판별
        r = r * a % M
    return r

print(powerMod(a, N, M))