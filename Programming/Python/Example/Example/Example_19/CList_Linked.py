import os
import sys


# 연결 리스트
class CList_Linked:
	# 노드
	class CNode:
		# 초기화
		def __init__(self, a_tVal):
			self.m_tVal = a_tVal
			self.m_oNode_Next = None
	
	# 초기화
	def __init__(self):
		self.m_nNumValues = 0
		self.m_oNode_Head = self.createNode(None)
	
	# 노드를 생성한다
	def createNode(self, a_tVal):
		return CList_Linked.CNode(a_tVal)
