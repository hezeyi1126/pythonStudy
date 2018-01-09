#http请求库
import urllib.request  

#解析html  
from lxml import etree

#解析json字符串
import json

#网址  
#url = "http://www.douban.com/"  
#baseurl = "http://www.douyu.com"
baseurl = "https://www.douyu.com"
#paraurl = "/directory"
paraurl = "/gapi/rkc/directory/0_0/1"


#url = baseurl + paraurl
url = "https://www.panda.tv/cate"


#请求
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

opener = urllib.request.build_opener()
opener.addheaders = [headers]




#爬取结果  
response = opener.open(url)


if str(response.getcode())=='200':
	data = response.read()  
	data = data.decode('utf-8')#设置解码方式  
	#print(data) #打印结果
	#解析a标签
	#tree = etree.HTML(data)
	#amarks = tree.find(u".//div[@class='box list channel']")
	#text = json.loads(data)#解析json字符串
	print(data)
	#for x in text['data']['rl']:
		
		#for y in x:
		#	print(x[y]);
		
		#print(str(x['rid']) + '---name:' + str(x['rn']))
	#print(len(text['data']['rl']))xx