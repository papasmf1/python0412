# DemoFile.py 

f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n")
f.write("두번째 라인\nabcd\n")
f.close()

#다시 파일을 열어서 읽기 
f = open("c:\\work\\demo.txt")
print( f.read() )
print( f.tell() )
#처음으로 돌아가기
f.seek(0)
print( f.readline() )
print( f.readline() )
#처음으로 돌아가기
f.seek(0)
result = f.readlines() 
print(result)
