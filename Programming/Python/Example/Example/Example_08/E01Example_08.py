import os
import sys

"""
함수 (Function) 란?
- 명령문의 일부 or 전체를 따로 분리해서 재사용 할 수 있는 기능을 의미한다. (+ 즉, 함수를 활용하면 중복적으로
발생하는 명령문을 최소화 시키는 것이 가능하다.)

함수 내부에는 명령문이 존재하며 해당 명령문은 함수가 호출 (실행) 되면 동작한다. (+ 즉, 함수가 호출되지 않으면
함수 내부에 존재하는 명령문은 동작하지 않는다는 것을 알 수 있다.)

Python 의 함수는 수학에서의 함수와 달리 입력과 출력이 존재하거나 없을 수 있다는 차이점이 존재한다. (+ 즉,
입력과 출력의 존재 여부에 따라 4 가지 유형이 존재한다는 것을 알 수 있다.)

Python 함수 유형
- 입력 O, 출력 O
- 입력 O, 출력 X
- 입력 X, 출력 O
- 입력 X, 출력 X

Python 함수 구현 방법
- def + 함수 이름 + 매개 변수 (입력) + 함수 몸체

Ex)
def someFunc(a_nValA, a_nValB):
	return a_nValA + a_nValB
	
nVal = someFunc(10, 20)

위와 같이 함수를 호출 (실행) 하면 함수 내부에 존재하는 명령문이 동작한다는 것을 알 수 있다.
"""

# Example 8 (함수 - 1)
def start(args):
	oTokens = input("수식 입력 : ").split()
	oOperator = oTokens[1]
	
	nValA = int(oTokens[0])
	nValB = int(oTokens[2])
	
	nResult = getResult_Calc(nValA, oOperator, nValB)
	print(f"결과 : {nResult}")

# 계산 결과를 반환한다
def getResult_Calc(a_nValA, a_oOperator, a_nValB):
	# + 일 경우
	if a_oOperator == "+":
		"""
		return 키워드란?
		- 프로그램의 현재 흐름을 종료하고 함수를 호출한 곳으로 이동시키는 역할을 수행하는 키워드를 의미한다.
		(+ 즉, return 키워드를 활용하면 함수를 즉시 종료 시키는 것이 가능하다.)
		
		또한 return 키워드는 프로그램의 흐름을 함수를 호출한 곳으로 이동시키면서 데이터를 전달하는 것이
		가능하다. (+ 즉, return 키워드에 데이터를 명시 할 경우 해당 데이터를 함수를 호출한 곳으로
		전달한다는 것을 알 수 있다.)
		"""
		return a_nValA + a_nValB
	
	# - 일 경우
	elif a_oOperator == "-":
		return a_nValA - a_nValB
	
	# * 일 경우
	elif a_oOperator == "*":
		return a_nValA * a_nValB
	
	# / 일 경우
	elif a_oOperator == "/":
		return a_nValA / a_nValB
	
	"""
	None 키워드란?
	- 아무런 의미 없는 데이터라는 것을 알리는 역할을 수행하는 키워드를 의미한다. (+ 즉, None 키워드를 활용하면
	자료형에 상관 없이 의미 없는 데이터를 통일 시키는 것이 가능하다.)
	"""
	return None
