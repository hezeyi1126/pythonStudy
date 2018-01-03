#用于保存文件
import os 
#http请求库
import urllib.request  
#解析html  
from lxml import etree

#网址  
#url = "http://www.douban.com/"  
baseurl = "http://456wp.com"
paraurl = "/htm/piclist4/"
#文件保存路径
baseimgPath = r'F:\img'

url = baseurl + paraurl
#url = "http://456wp.com/htm/piclist4/"  
  

#请求
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

opener = urllib.request.build_opener()
opener.addheaders = [headers]

#request = urllib.request.Request(url)  

#创建保存目录
if not os.path.isdir(baseimgPath):
   	os.mkdir(baseimgPath)
  
#爬取结果  
#response = urllib.request.urlopen(request)  
response = opener.open(url)
#if response.getcode()=='200'
data = response.read()  
data = data.decode('utf-8')#设置解码方式  
#print(data) #打印结果

#解析a标签
tree = etree.HTML(data)
#hrefs = tree.xpath(u"//a")
amarks = tree.find(u".//div[@class='box list channel']").findall(u".//a")

for amark in amarks:
	urlParten = amark.get('href');
	response = opener.open(baseurl + urlParten)
	if response.getcode() == 200:
		data = response.read().decode('utf-8')
		print('开始保存图片-----------------------------------------------------------------------------------')
		#print(urlParten)

		imgPath = baseimgPath+ '\\' + amark.xpath('string(.)').strip()
		imgPath = imgPath.replace('/','-')
		if not os.path.isdir(imgPath):		#建立页面对应的目录
   			os.mkdir(imgPath)
		#解析a标签
		tree = etree.HTML(data)
		imgs = tree.xpath(u".//img")
		imgurl = ''
		index = 1
		
		for img in imgs:
			imgurl = img.get('src')
			filename=os.path.join(imgPath,str(index)+'.jpg')
			if not os.path.exists(filename):
				print('保存---------------' + imgurl + '开始')
				res=opener.open(imgurl)
				try:
					if str(res.status)!='200':
						print('未下载成功：',imgurl)
						continue
				except Exception as e:
					print('未下载成功：',imgurl)
				with open(filename,'wb') as f:
					f.write(res.read())
					print('下载完成\n')
					index+=1
			
		
	#break
	#print(baseurl + div.get('href'))


#for href in hrefs:
 # print(href.text)
 
  
  
 



#print(tree)
  
#打印爬取网页的各类信息  
  
#print(type(response))  
#print('--------------------------------------------------') 
#print(response.geturl())  
#print('--------------------------------------------------') 
#print(response.info())  
#print('--------------------------------------------------') 
#print(response.getcode())  
