#encoding:utf-8
import Image
import sys

color = 'MNHQ$OC?7>!:-;.'
size = 200,200


def main():
	if len(sys.argv)<=2:
		print('Need <input img path> <output html path>')
		return
	img = Image.open(sys.argv[1])#获取图片
	size = img.size
	img = img.resize(size)#修改大小
	img = img.convert('L')#转化成黑白图片
	pix = img.load()#加载，获取像素
	#构造字符画
	width,height = img.size
	result = ''
	for j in xrange(height):
		for i in xrange(width):
			#加两次，图片宽一点
			result += color[int(pix[i, j]) * 14 / 255]+color[int(pix[i, j]) * 14 / 255]
		result+='<br />'	
	html_head = '''
    <html>
		<head>
			<style type="text/css">
			 body {font-family:Monospace; font-size:5px;}
			</style>
		</head>
		<body>
	'''
	html_tail = '</body></html>'
	file = open(sys.argv[2],'w')
	file.write(html_head+result+html_tail)
	file.close()
	img.show()

if __name__ == '__main__':
	main()