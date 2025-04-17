import os
import sys

# Training 1
def start(args):
	nScore = int(input("점수 입력 : "))
	nScore_Detail = nScore % 10
	
	oGrade = ""
	oGrade_Detail = ""
	
	# F 학점 일 경우
	if nScore < 60:
		oGrade = "F"
	
	else:
		# A 학점 일 경우
		if nScore >= 90:
			oGrade = "A"
			
		# B 학점 일 경우
		elif nScore >= 80:
			oGrade = "B"
			
		# C 학점 일 경우
		elif nScore >= 70:
			oGrade = "C"
			
		else:
			oGrade = "D"
			
		# + 학점 일 경우
		if nScore >= 100 or (nScore_Detail >= 7 and nScore_Detail <= 9):
			oGrade_Detail = "+"
			
		else:
			oGrade_Detail = "-" if nScore_Detail <= 3 else "0"
			
	print(f"학점 : {oGrade}{oGrade_Detail}")
	