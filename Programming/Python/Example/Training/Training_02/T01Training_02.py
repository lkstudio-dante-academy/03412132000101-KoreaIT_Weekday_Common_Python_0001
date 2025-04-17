import os
import sys

# Training 2
def start(args):
	nVal = int(input("정수 (2 ~ 9) 입력 : "))
	
	# 범위 내의 수를 입력했을 경우
	if nVal >= 2 and nVal <= 9:
		while nVal < 10:
			i = 1
			print(f"=====> {nVal} 단 <=====")
			
			while i < 10:
				print(f"{nVal} * {i} = {nVal * i}")
				i += 1
				
			print()
			nVal += 1
			
	else:
		print("2 ~ 9 범위 내의 수를 입력하세요.")
		