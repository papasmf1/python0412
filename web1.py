# web1.py
from bs4 import BeautifulSoup

#문자열을 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#문서 전체를 보기
#print( soup.prettify() )
#find_all("태그")
#print( soup.find_all("p") )
#<p class="outer-text"> 필터링 
#print( soup.find_all("p", class_="outer-text") ) 

#검색을 해서 태그 안쪽의 컨텐츠 
for tag in soup.find_all("p", class_="outer-text"):
    print( tag.text )

    
