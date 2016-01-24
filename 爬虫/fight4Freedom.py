#encoding:utf-8
import urllib2
import sys
import os
from HTMLParser import HTMLParser

#创建子类，复写方法
class MyHTMLParser(HTMLParser):
	imgList = []
	Flag_Tag_a = ''
	queue = []
	URL_BASE = 'http://tieba.baidu.com'
	def __init__(self,imgList,queue):
		HTMLParser.__init__(self)
		self.queue = queue
		self.imgList = imgList
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			for attr in attrs:
				if attr[0]=='src' and attr[1] not in self.imgList:
					self.imgList.append(attr[1])
					pass
		elif tag == 'a':
			for attr in attrs:
				if attr[0]==u'href':
					self.Flag_Tag_a = self.URL_BASE+attr[1]
	def handle_endtag(self, tag):
		#print ("Encountered an end tag :", tag,self.getpos())
		if tag == 'a':
			self.Flag_Tag_a = ''
		return
	def handle_data(self, data):
		#print ("Encountered some data  :", data)
		return
	def handle_startendtag(self,tag,attrs):
		#HTMLParser.handle_startendtag(self,tag,attrs)
		#print ("Encountered a start-end tag:", tag,attrs)
		return
	def handle_data(self,data):
		if self.Flag_Tag_a == '':
			return
		else:
			#下面不decode会报：UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting 
			#不是很明白是为什么
			if data == u'下一页':
				#下面这里换成哈希会好一点
				if self.Flag_Tag_a not in self.queue:
					self.queue.append(self.Flag_Tag_a)
					print(u'添加网页'+self.Flag_Tag_a)
		return

def main():
	'''爬百度贴吧某个帖子里的所有图

		python xxx.py 贴吧url <output path>
	
	'''
	if len(sys.argv)<3:
		return
	inital_url = sys.argv[1]
	outputpath = sys.argv[2]
	imgList = []
	queue=[]
	queue.append(inital_url)
	parser = MyHTMLParser(imgList,queue)
	#获取所有图片链接
	while True:
		if len(queue)<=0:
			break
		url = queue.pop(0)
		#获取页面
		content = urllib2.urlopen(url).read()
		#百度贴吧是utf-8编码
		parser.feed(content.decode('utf-8'))
	#下载
	while os.path.isfile(outputpath):
		outputpath += '-tmp'
	if not os.path.exists(outputpath):
		os.mkdir(outputpath)
	index = 0
	for line in imgList:
		#不要后缀名，网页里很多后缀名都写错了，反而打不开
		out = open(outputpath+'/'+str(index),'w')
		out.write(urllib2.urlopen(line).read())
		out.close()
		index += 1
		print('完成'+str(index)+'个,共'+str(len(imgList))+'个')
	#过滤器
	#方案一，删除太小的
	for root,dirs,files in os.walk(outputpath):
		for file in files:
			if int(os.path.getsize(root+'/'+file))<10*1024:
				os.remove(root+'/'+file)
	#使用已知的广告图片匹配
		
if __name__ == '__main__':
	main()