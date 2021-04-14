# 디버깅은 논리적인 오류를 잡아내는 작업 
# DemoLoop.py 
for x in [2,3,4,5,6]:
    print("--{0}단--".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

#break, continue구문 
lst = [1,2,3,4,5,6,7,8,9,10]
#디버깅 모드로 실행중이면 여기서 멈추도록 한다(중지점, 중단점, Break Point)
for item in lst:
    if item > 5:
        break 
    print("Item:{0}".format(item))


