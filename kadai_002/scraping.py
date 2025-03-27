from bs4 import BeautifulSoup
from urllib import request
import re


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
#print(main_text)

#ストップワードの削除
#対象文章の作成
target_text = ["近頃", "は", "大分方々", "の", "雑誌", "から", "談話", "を", "しろしろ", "と", "責められて", "、", "頭", "が", "がらん胴", "に", "なった", "から", "、", "当分", "品切れ", "の", "看板", "でも", "懸けたい", "くらい", "に", "思って", "います", "。"]

#結果格納変数の作成
result_text_list = list()

#ストップワードリストの作成
stopwords_text = '''
あそこ
あたり
あちら
あっち
あと
あな
あなた
あれ
いくつ
いつ
いま
いや
いろいろ
うち
おおまか
おまえ
おれ
がい
かく
かたち
かやの
から
がら
きた
くせ
ここ
こっち
こと
ごと
こちら
ごっちゃ
これ
これら
ごろ
さまざま
さらい
さん
しかた
しよう
すか
ずつ
すね
すべて
ぜんぶ
そう
そこ
そちら
そっち
そで
それ
それぞれ
それなり
たくさん
たち
たび
ため
だめ
ちゃ
ちゃん
てん
とおり
とき
どこ
どこか
ところ
どちら
どっか
どっち
どれ
なか
なかば
なに
など
なん
はじめ
はず
はるか
ひと
ひとつ
ふく
ぶり
べつ
へん
ぺん
ほう
ほか
まさ
まし
まとも
まま
みたい
みつ
みなさん
みんな
もと
もの
もん
やつ
よう
よそ
わけ
わたし
ハイ
上
中
下
字
年
月
日
時
分
秒
週
火
水
木
金
土
国
都
道
府
県
市
区
町
村
各
第
方
何
的
度
文
者
性
体
人
他
今
部
課
係
外
類
達
気
室
口
誰
用
界
会
首
男
女
別
話
私
屋
店
家
場
等
見
際
観
段
略
例
系
論
形
間
地
員
線
点
書
品
力
法
感
作
元
手
数
彼
彼女
子
内
楽
喜
怒
哀
輪
頃
化
境
俺
奴
高
校
婦
伸
紀
誌
レ
行
列
事
士
台
集
様
所
歴
器
名
情
連
毎
式
簿
回
匹
個
席
束
歳
目
通
面
円
玉
枚
前
後
左
右
次
先
春
夏
秋
冬
一
二
三
四
五
六
七
八
九
十
百
千
万
億
兆
下記
上記
時間
今回
前回
場合
一つ
年生
自分
ヶ所
ヵ所
カ所
箇所
ヶ月
ヵ月
カ月
箇月
名前
本当
確か
時点
全部
関係
近く
方法
我々
違い
多く
扱い
新た
その後
半ば
結局
様々
以前
以後
以降
未満
以上
以下
幾つ
毎日
自体
向こう
何人
手段
同じ
感じ
'''

stopwords_list = stopwords_text.split("\n")
stopwords_list = [word for word in stopwords_list if word]

#ストップワードの除去
for split_text in target_text:
  if split_text not in stopwords_list:
    result_text_list.append(split_text)
print(result_text_list)
