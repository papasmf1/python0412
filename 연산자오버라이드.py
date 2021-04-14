#연산자 오버라이드 
class NumBox:
	def __init__(self, num):
		self.Num = num
	# + 연산자를 메서드로 재정의 
	#def __add__(self, num):
	def add(self, num):
		self.Num += num
	# - 연산자를 재정의 
	# def __sub__(self, num):
	def remove(self, num): 
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(110) 
print(n.Num)
n.remove(50)
print(n.Num)
