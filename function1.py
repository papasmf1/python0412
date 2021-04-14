# function1.py 
#함수를 정의
def setValue(newValue):
    #함수 내부에서 초기화(지역변수)
    x = newValue
    print("함수내부:", x)

#호출
setValue(5)

#튜플을 리턴하는 경우
def swap(x,y):
    return y,x 

#호출
print( swap(5,6) )

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수는 함수안에서 접근 
    retList = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#호출
print( intersect("HAM","SPAM") )

print( dir() )
print("--------------")
print( globals() )


