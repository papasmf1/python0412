# class2.py 
# 클래스 형식 정의
class Person:
    #위치를 잘 본다~~
    num_person = 0 
    #초기화 메서드(인스턴스의 멤버변수 초기화)
    def __init__(self):
        self.name = "default name"    
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name) )

#인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person() 

print("인스턴스 갯수:{0}".format(Person.num_person) )


#런타임시에 멤버를 추가
Person.title = "new title"
print( p1.title )
print( p2.title )
print( Person.title )

#인스턴스에 추가
p1.age = 30
print(p1.age)
print(p2.age)
print(Person.age)
