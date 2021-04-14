# function3.py 
# 가변 인자를 처리하는 함수(*)
def union(*ar):
    res = []
    for item in ar:
        for x in item:
            if x not in res:
                res.append(x)
    return res 

#호출 
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )

#정의되지 않은 인자처리(**)
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

#호출
print( userURIBuilder("credu.com", "80", id="kim", pwd="1234") )
print( userURIBuilder("credu.com", "80", id="kim", pwd="1234", 
    name="mike", age="30") )

#람다 함수(이름이 없는 간결하게 함수를 정의하는 문법)
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )
print( (lambda x:x*x)(3) )
print( globals() )

#예를 들면 필터 함수 
lst = [10,25,30]

#함수를 호출하는 부분에서 바로 함수를 정의 
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)


#재귀 호출(자기 자신을 호출)
def factorial(x):
    if x == 1:
        return 1 
    return x * factorial(x-1)

#호출
print( factorial(3) )
print( factorial(10) )

#클래스를 정의(멤버를 구현하지 않은 경우)
class Demo:
    pass 

#문서화 작업
def add(x,y):
    """이 함수는 2개의 숫자를 
    입력받아서 덧셈을 수행합니다."""
    return x+y 

#호출
print( help(add) )


#열거가능한 형식
for i in [1,2,3]:
    print(i)

for char in "abc":
    print(char)

#만약에 저수준으로 구현 
s = "abc"
it = iter(s)
print( next(it) )
print( next(it) )
print( next(it) )

#제너레이터 패턴의 함수 
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

#호출
for char in reverse("gold"):
    print(char)

print("----abc()----")
#단순한 예제(값을 생성->추출->마지막에 반환)
def abc():
    data = "abcde"
    for char in data:
        yield char 

#호출
for char in abc():
    print(char)

