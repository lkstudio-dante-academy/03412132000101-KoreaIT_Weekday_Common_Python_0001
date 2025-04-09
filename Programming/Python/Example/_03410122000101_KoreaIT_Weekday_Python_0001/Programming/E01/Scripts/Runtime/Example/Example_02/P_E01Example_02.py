import os
import sys

# Example 2 (자료형)
def start(args):
	nInt = 10
	fFloat = 3.14
	
	print("=====> 자료형 - 숫자 <=====")
	print(f"정수 : {nInt}")
	print(f"실수 : {fFloat}")
	
	oList = [ 1, 2, 3, 4, 5 ]
	oDict = { "Key_01": 1, "Key_02": 2, "Key_03": 3 }
	
	print("\n=====> 자료형 - 컬렉션 <=====")
	print(f"리스트 : {oList}")
	print(f"딕셔너리 : {oDict}")
	
	bIsBool = True
	oStr = "Hello, World!"
	
	print("\n=====> 자료형 - 기타 <=====")
	print(f"논리 : {bIsBool}")
	print(f"문자열 : {oStr}")
	