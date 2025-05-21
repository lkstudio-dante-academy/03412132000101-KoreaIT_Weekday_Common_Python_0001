import os
import sys

import threading

"""
웹 크롤링이란?
- 
"""


# Example 18 (웹 크롤링 - 1)
def start(args):
	oThreadA = threading.Thread(target = main_ThreadA)
	oThreadB = threading.Thread(target = main_ThreadA)
	
	oThreadA.start()
	oThreadB.start()
	
	# oThreadA.join()
	
	
# 쓰레드 A 메인 함수
def main_ThreadA():
	for i in range(0, 100000):
		print(f"{i + 1}")
		