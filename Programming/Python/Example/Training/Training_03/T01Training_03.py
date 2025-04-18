import os
import sys

import random

"""
Python 연습 문제 3
- 업/다운 게임 제작하기
- 1 ~ 99 범위의 수 중 정답에 해당하는 수 1 개 추출
- 사용자로부터 수를 입력 받아 정답 여부 검사
- 사용자가 입력한 수가 정답과 일치 할 경우 게임 종료
- 사용자가 입력한 수가 정답이 아닐 경우 수를 가이드 메세지를 출력 후 게임 계속 진행

Ex)
정답 : 85

정수 입력 : 70
정답은 70 보다 큽니다.

정수 입력 : 90
정답은 90 보다 작습니다.

정수 입력 : 85
프로그램을 종료합니다.
"""

# Training 3
def start(args):
	nAnswer = random.randrange(1, 100)
	print(f"정답 : {nAnswer}\n")
	
	while True:
		pass
	
	print("프로그램을 종료합니다.")
