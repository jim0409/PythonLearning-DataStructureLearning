import pandas
dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')

currency = dfs[0].ix[:,0:5]
currency.columns = [u'col1',u'col2',u'col3',u'col4',u'col5']  #加入u表示 unicode 避免儲存成其他資料的時候會出現錯誤
currency[u'col1'] = currency[u'col1'].str.extract('\((\w+)\)')     #透過pandas的extract再透過正規表達法取出USD
print(currency)

currency.to_excel('currency.xlsx')



#
# import requests
# res1 = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# content1 = res1.text
# content1 = res1.json()
# print(type(content1))
#
# res2 = requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
# content2 = res2.text
# # content2 = res2.json()   並非所有的request下來的資料都可以宣告成json陣列
# print(type(content2))

