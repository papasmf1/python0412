lst = [1,2,3,4,5,6,7,8,9,10]
#디버깅 모드로 실행중이면 여기서 멈추도록 한다(중지점, 중단점, Break Point)
# 선택한 라인들을 주석 처리: ctrl + / 
# /*  .... */
for item in lst:
    if item > 5:
        break 
    print("Item:{0}".format(item))


print("-------continue구문------")
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))


print("-------continue구문------")
for item in lst:
    if item % 2 == 1:
        continue
    print("Item:{0}".format(item))


#수열함수
print( list(range(10)) )
print( list(range(5,10)) )
print( list(range(1,11,1)) )
print( list(range(10,0,-1)) )

#for루프를 5번만 돌기
for i in range(10):
    print(i)


#리스트 컴프리헨션(파이썬스럽다~~)
lst = [1,2,3,4,5,6,7,8,9,10]
print( [i**2 for i in lst if i > 5] )

tp = ("apple", "banana", "kiwi")
print( [len(i) for i in tp] )

d = { 100:"apple", 200:"kiwi" }
print( [v.upper() for v in d.values()] )

#필터링 하는 함수
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#함수를 정의
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)


