from bs4 import BeautifulSoup
from urllib import request
import re
from stopwords import stopwords_text


url = 'https://www.aozora.gr.jp/cards/000148/files/2371_13943.html'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

#本文の切り出しとタグの削除
main_text = soup.find('div', class_='main_text')
tags_to_delete = main_text.find_all(['rp', 'rt'])
for tag in tags_to_delete:
    tag.decompose()
main_text = main_text.get_text()

#改行等削除
main_text = re.sub(r"[\u3000 \n \r]", "", main_text)
print(main_text)

#ストップワードの削除
#対象文章の作成
target_text = ["近頃", "は", "大分方々", "の", "雑誌", "から", "談話", "を", "しろしろ", "と", "責められて", "、", "頭", "が", "がらん胴", "に", "なった", "から", "、", "当分", "品切れ", "の", "看板", "でも", "懸けたい", "くらい", "に", "思って", "います", "。"]

#結果格納変数の作成
result_text_list = list()

#ストップワードリストの作成
stopwords_list = stopwords_text.split("\n")
stopwords_list = [word for word in stopwords_list if word]

#ストップワードの除去
for split_text in target_text:
  if split_text not in stopwords_list:
    result_text_list.append(split_text)
print(result_text_list)
