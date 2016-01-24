#encoding:utf-8
'''python 使用urllib2,httplib和HTMLParser
	
	[1]urllib2和httplib都封装了很多HTTP操作(HTTP协议定义的操作)，利用它们可以简便的发送request，接收response。
	[2]理想的情况是：1.了解基本的tcp原理(至少三次握手，滑动窗口，同步拥塞，端口ip要知道)
				2.详细了解HTTP协议（这个有点...只知道cookie,session,Get,Post,其他不懂，更不懂报文格式）
				3.自己实现一次Web通信（2都不懂。。。）
	[3]一次HTTP连接：
				1.tcp连接到服务器 
				2.使用HTTP协议发送Get或Post request 
				3.获取并解析reponse（如果要完美模拟一个用户，这里要达到浏览器的解析水平，还要能执行javascript，汗）
	ps:不过有了urllib2和httplib帮忙，会容易很多～，httplib还是有点困难，各种重定向什么的还得自己解析。。。

	官网介绍：httplib — HTTP protocol client[https://docs.python.org/2/library/httplib.html?highlight=httplib#module-httplib]
			urllib2 — extensible library for opening URLs[https://docs.python.org/2/library/urllib2.html?highlight=urllib2]
			
'''


'''
	python 新浪微博客户端
	
	新浪：(改用cookie)
	http://open.weibo.com/wiki/SDK#Python_SDK
	http://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI
	http://open.weibo.com/wiki/2/statuses/friends_timeline
	http://open.weibo.com/wiki/%E6%96%B0%E6%89%8B%E6%8C%87%E5%8D%97
	教程：
	这么搜：https://www.google.com.hk/?gws_rd=cr,ssl#safe=strict&q=python+%E8%8E%B7%E5%8F%96%E5%BE%AE%E5%8D%9A
	http://www.cnblogs.com/wly923/archive/2013/04/28/3048700.html
	https://pypi.python.org/pypi/chinaapi/0.8.9
	好内容：
	https://www.zhihu.com/question/29666539
	http://www.douban.com/note/201767245/?start=100#comments
	http://www.jb51.net/article/44779.htm
	http://www.jikexueyuan.com/course/995.html

	带cookie尝试了一下，不好使啊！http://www.douban.com/note/264976536/
	这个，有点蛋疼，需要重新思考再做！2015-12-26

	使用cookie要比使用oauth2神马的好一些
	wap>m>pc
	javascript问题
'''