# web2.py 
#웹서버에 요청
import urllib.request
#웹크롤링 
from bs4 import BeautifulSoup

#실행된 페이지 결과(문자열)
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체 생성
soup = BeautifulSoup(data, "html.parser")

#다중라인 주석: ctrl + / 
# <td class="title">
# 	<a href="/webtoon/detail.nhn">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
# 리스트 객체 
cartoons = soup.find_all("td", class_="title")
f = open("c:\\work\\webtoon.txt", "wt")
for item in cartoons:
    title = item.find("a")
    print(title.text)
    f.write(title.text + "\n")

f.close()



