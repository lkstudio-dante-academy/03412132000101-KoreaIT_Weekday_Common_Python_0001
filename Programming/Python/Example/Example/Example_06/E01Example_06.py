import os
import sys

import random

"""
컬렉션 (Collection) 이란?
- 여러 데이터를 관리 및 제어 할 수 있는 기능을 의미한다. (+ 즉, 컬렉션을 활용하면 여러 데이터를 제어해서
다양한 결과를 출력하는 프로그램을 제작하는 것이 가능하다.)

컬렉션은 내부적으로 데이터를 관리하는 형태에 따라 크게 선형 컬렉션과 비선형 컬렉션으로 구분된다.

선형 컬렉션 (Linear Collection) 이란?
- 내부적으로 데이터를 1 차원의 형태로 관리하는 컬렉션을 의미한다. (+ 즉, 데이터를 단순한 형태로 관리한다는
것을 알 수 있다.)

선형 컬렉션은 데이터를 관리하는 형태가 단순하기 때문에 구현이 용이하지만 관리되는 데이터의 개수가 많을수록
효율이 떨어지는 단점이 존재한다. (+ 즉, 선형 컬렉션은 일반적으로 개수가 적은 데이터를 관리하는데
효율적이라는 것을 알 수 있다.)

Python 선형 컬렉션 종류
- 리스트 (List)
- 튜플 (Tuple)

리스트 (List) 란?
- 관리되는 데이터 간에 순서가 존재하는
"""

# Example 6 (컬렉션 - 1)
def start(args):
	oTupleValues = (1, 2, 3, 4, 5)
	print("=====> 튜플 요소 <=====")
	
	for nVal in oTupleValues:
		print(f"{nVal}, ", end="")
		
	print()
	oListValues = []
	
	for i in range(0, 10):
		"""
		random 모듈이란?
		- 난수를 생성하기 위한 다양한 기능을 제공하는 모듈을 의미한다. (+ 즉, random 모듈을 활용하면
		실행 할 때마다 다른 결과를 출력하는 프로그램을 제작하는 것이 가능하다.)
		
		Ex)
		nVal = random.randrange(1, 100)
		
		위와 같이 random 모듈에 존재하는 randrange 함수를 호출하면 범위 내에 존재하는 수를 무작위로
		추출하는 것이 가능하다.
		"""
		nVal = random.randrange(1, 100)
		
		"""
		append 함수는 데이터를 리스트의 가장 마지막에 추가하는 역할을 수행한다. (+ 즉, append 함수를 활용하면
		특정 데이터를 리스트에 추가하는 것이 가능하다.)
		"""
		oListValues.append(nVal)
		
	print("\n=====> 리스트 요소 <=====")
	
	for nVal in oListValues:
		print(f"{nVal}, ", end="")
		
	nVal_Insert = int(input("\n\n정수 입력 (삽입) : "))
	
	"""
	insert 함수는 데이터를 리스트의 특정 위치에 추가하는 역할을 수행한다. (+ 즉, insert 함수를 활용하면
	데이터를 원하는 위치에 추가하는 것이 가능하다.)
	"""
	oListValues.insert(0, nVal_Insert)
	
	print("\n=====> 리스트 요소 - 삽입 후 <=====")
	
	for nVal in oListValues:
		print(f"{nVal}, ", end="")
		
	nVal_Remove = int(input("\n\n정수 입력 (제거) : "))
	
	"""
	remove 함수는 데이터를 리스트로부터 제거하는 역할을 수행한다. (+ 즉, remove 함수를 활용하면
	원하는 데이터를 리스트에서 제거하는 것이 가능하다.)
	
	단, 리스트에 존재하지 않는 데이터를 remove 함수로 제거를 시도 할 경우 내부적으로 예외가 발생하기
	때문에 주의가 필요하다. (+ 즉, 데이터의 존재 여부를 확실 할 수 없다면 if 조건문을 활용해 데이터의
	존재 여부를 검사해야한다는 것을 알 수 있다.)
	
	Ex)
	oListValues = [ 1, 2, 3 ]
	
	if 4 in oListValues:
		oListValues.remove(4)
		
	위와 같이 in 키워드를 활용하면 특정 데이터의 존재 여부를 검사하는 것이 가능하다.
	
	또한 remove 함수는 1 개의 데이터만 제거하기 때문에 제거하고 싶은 데이터가 리스트에 중복으로 존재 할 경우
	가장 순서가 낮은 데이터가 제거된다. (+ 즉, 중복되는 데이터를 모두 제거하고 싶다면 반복문 등을
	활용해야한다는 것을 알 수 있다.)
	
	Ex)
	oListValues = [ 1, 2, 1, 3, 4 ]
	
	while 1 in oListValues:
		oListValues.remove(1)
		
	위와 같이 in 키워드와 반복문을 활용하면 리스트에 존재하는 특정 데이터를 모두 제거하는 것이 가능하다.
	"""
	oListValues.remove(nVal_Remove)
	
	print("\n=====> 리스트 요소 - 제거 후 <=====")
	
	for nVal in oListValues:
		print(f"{nVal}, ", end="")
		
	nIdx_Remove = int(input("\n\n위치 입력 (제거) : "))
	
	"""
	del 키워드는 위치 (인덱스 번호) 를 기반으로 데이터를 제거하는 역할을 수행한다. (+ 즉, del 키워드를
	활용하면 특정 위치에 존재하는 데이터를 제거하는 것이 가능하다.)
	
	단, del 키워드는 remove 함수와 마찬가지로 잘못된 위치를 입력했을 경우 내부적으로 예외가 발생하기 때문에
	주의가 필요하다.
	"""
	del oListValues[nIdx_Remove]
	
	print("\n=====> 리스트 요소 - 제거 후 <=====")
	
	for nVal in oListValues:
		print(f"{nVal}, ", end="")
		