# class1.py 
# 클래스 형식 정의
class Person:
    #초기화 메서드(인스턴스의 멤버변수 초기화)
    def __init__(self):
        self.name = "default name"    
    def print(self):
        print("My name is {0}".format(self.name) )

#인스턴스 생성
p1 = Person()
#두번째 복사본 생성
p2 = Person()
p2.name = "전우치"

p1.print()
p2.print() 

