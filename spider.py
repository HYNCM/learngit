import requests
from pyquery import PyQuery
import csv
#新建csv
path='F:/data/dianpin.csv'
csvf=open(path,'a+',encoding='utf-8',newline='')
fieldnames=['hotel_name','addr1','addr2']
writer=csv.DictWriter(csvf,fieldnames=fieldnames)
writer.writeheader()
template='http://www.dianping.com/shanghai/hotel/p{page}'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) >AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36"}
for p in range(1,51):
	print(p)
	url=template.format(page=p)
	resp=requests.get(url,headers=headers)
	doc=PyQuery(resp.text)
	#存储数据

for hotel in doc.items('.hotel-block'):
		hotel_name=hotel('.hotel-name-link').text()
		addr1=hotel('.place a').text()
		addr2=hotel('.walk-dist').text()[1:]
		data={'hotel_name':hotel_name,
	      'addr1':addr1,
	      'addr2':addr2}
		writer.writerow(data)
csvf.close()