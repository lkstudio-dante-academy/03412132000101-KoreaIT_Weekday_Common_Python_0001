import os
import sys

"""
Python 연습 문제 8
- 하노이 탑 시뮬레이션 제작하기
- 사용자로부터 숫자를 입력 받아 해당 숫자에 맞는 하노이 탑 시뮬레이션 출력

Ex)
정수 입력 : 2
1 이동 : A -> B
2 이동 : A -> C
1 이동 : B -> C
"""


# Training 8
def start(args):
	nNum = int(input("정수 입력 : "))
	printResult_HanoiTower(nNum, "A", "C", "B")


# 하노이 탑 결과를 출력한다
def printResult_HanoiTower(a_nNum, a_oFrom, a_oTo, a_oBuffer):
	# 결과 출력이 불가능 할 경우
	if a_nNum <= 0:
		return
	
	printResult_HanoiTower(a_nNum - 1, a_oFrom, a_oBuffer, a_oTo)
	print(f"{a_nNum} 이동 : {a_oFrom} -> {a_oTo}")
	
	printResult_HanoiTower(a_nNum - 1, a_oBuffer, a_oTo, a_oFrom)
