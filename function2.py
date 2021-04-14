# function2.py
#전역변수와 지역변수 충돌
x = 5 
def func(a):
    return x+a 

#호출
print( func(1) )

def func2(a):
    x = 2 
    return x+a 

#호출
print( func2(1) )

#불변형식
a = 1.2
print( id(a) )
a = 2.3 
print( id(a) )

#가변형식
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )


#함수의 매개변수(인자, 파라메터)로 전달(Pass By Reference)
#가변형식
wordlist = ["J","A","M"]
def change(x):
    #지역변수로 복사해서 변경(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#함수 호출
change(wordlist)
print("함수호출후:", wordlist)

#불변형식으로 된 전역변수에 함수 내부에서 읽기/쓰기 작업
g = 1 
def testScope(a):
    #불변형식을 맵핑(전역변수)
    global g 
    #지역변수
    g = 2 
    return g+a 

#함수 호출
print( testScope(1) )
print("전역변수 g:", g)

#기본값을 지정
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자(파라메터명을 상세하게 기술)
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

#호출 
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="test.com") )


