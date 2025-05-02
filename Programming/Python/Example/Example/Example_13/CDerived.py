import os
import sys

from Example.Example_13.CBase import CBase


# 자식 클래스
class CDerived(CBase):
	# 초기화
	def __init__(self, a_nVal, a_fVal, a_oStr):
		"""
		super 함수는 부모 객체에 대한 참조 값을 가져오는 역할을 수행한다. (+ 즉, super 함수를 활용하면
		부모 클래스에 존재하는 동일한 이름의 멤버에 접근하는 것이 가능하다.)
		
		자식 클래스는 부모 클래스 내부에 존재하는 멤버와 동일한 이름을 지니는 멤버를 정의하는 것이 가능하다.
		
		이때 자식 클래스의 우선 순위가 더 높기 때문에 부모 클래스에 존재하는 멤버를 지정하기 위해서는
		super 함수를 이용해서 직접 부모 클래스에 존재하는 멤버에 접근 한다는 것을 명시해줘야한다.
		
		__init__ 함수는 객체를 초기화하는 역할을 수행하는 함수이기 때문에 부모 클래스에 __init__ 함수가
		존재 할 경우 자식 클래스에서는 반드시 부모 클래스에 존재하는 __init__ 함수를 호출해줘야한다.
		"""
		super().__init__(a_nVal, a_fVal)
		self.m_oStr = a_oStr
	
	# 정보를 출력한다
	def showInfo(self):
		super().showInfo()
		print(f"문자열 : {self.m_oStr}")
