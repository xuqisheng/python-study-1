#encoding:utf-8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import PSDraw
import sys
import random 

'''尝试PIL
PIL handbook：http://effbot.org/imagingbook/
pillow:http://pillow.readthedocs.org/en/3.0.x/handbook/tutorial.html 

1.基本概念：
	图像模式(mode)：L[灰度图片，只有一个值是灰度],RGB[255真彩图片，三个灰度值，分别是(R灰度，G灰度，B灰度)],RGBA-多一个alpha通道
	图像格式：使用Image操作图片，不需要特殊关注格式，只需要知道图片mode就可以了，不论png还是jpg，用RGB操作都一样的，但是保存和转换时会有不同
	通道(Band):L-单通道，RGB-三通道，RGBA-四通道 Image.split返回通道
1.常用Module与Function:
	Image,ImageDraw,ImageFont,ImageFilter
2.基础操作：split,merge,cut,paste
	Image = Image.open(filepath)#获取图片
	Image = Image.new(mode,(width,height),'white')#构造图像
	Image.save(fp, format=None, **params)#保持
	Image.show()#显示
	Image.split()#返回通道
	Image.size#(width,height)
	PIL.Image.merge(mode, bands)#合并，bands是通道
	Image.crop#剪切
	Image.paste(im, box=None, mask=None)#把im粘贴到Image中去，其中mask为255的地方粘贴im，mask为0的地方保持原样
	说明：mask就是个'L'图或者'RGBA'图，如果是'L',那么所有mask值为255对应的Image的点都会被替换为im对应的点,为0则不替换。mask是RGBA的时候，就会使用其alpha通道值，为255就替换,为0就不替换
	draw=ImageDraw.Draw(Image)#构造一个画笔
	ImageDraw.ink = 255+0*256+1*256*256#设置画笔颜色
	ImageDraw.rectangle([0,0,100,100],fill='black',outline='red')#画矩形
	ImageDraw.text((0,0),'Hello World',font = font)#画字
4.像素操作
	Image.load()返回像素对象，可以px = img.load()
	枚举像素：
		for h in xrange(height):
			for w in xrange(width):
				pix[w,h] = (0,0,0)
'''

def main():
	img = Image.open(sys.argv[1])
	#splitAndMerge(img)
	#cuttingAndPasting(img)
	#img.show()
	#out = img.point(lambda i: i * 1.2)#变亮变白～
	#out.show()
	#mask(img)
	maskWithPix(img)

def splitAndMerge(img):
	r, g, b = img.split()
	print(img)
	print(r)
	width,height = img.size
	pix = r.load()
	for h in xrange(height):
		for w in xrange(width):
			pix[w,h] = 255#很好玩哦～
	imgT = Image.merge("RGB", (r,g,b))
	imgT.show()

def cuttingAndPasting(img):
	'''
		只是使用crop，如cutImg1 = img.crop(box1)，并不会马上产生cutImg1，
		cutImg1所代表的图片会在第一次调用cutImg1的时候去img中截取，所以
	'''
	width,length = img.size
	box1 = (0,0,width/2,length)
	box2 = (width/2,0,width,length)
	cutImg1 = img.crop(box1)
	cutImg2 = img.crop(box2)
	if random.randint(0,1) == 0:#当输出了cutImg1的时候，就是左右交换，没输出的时候就是右赋值到左侧
		cutImg1.show()
	cutImg1.load()#	或者使用一下cutImg1，就一定会左右交换了
	img.paste(cutImg2,box1)
	img.paste(cutImg1,box2)
	img.show()

def drawImage(img):
	width,height = img.size
	im = Image.new('RGBA',(width,height),'white')#构造图像
	draw = ImageDraw.Draw(im)#构造画笔
	font = ImageFont.truetype("arial.ttf", 36)#构造字体
	draw.ink = 255+0*256+1*256*256#设置画笔颜色
	draw.rectangle([0,0,100,100],fill='black',outline='red')
	draw.text((0,0),'Hello World',font = font)
	#im.show()
	#alpha不是0.0~1.0吗？为什么不接受浮点数？
	pix = im.load()
	for h in xrange(height):
		for w in xrange(width):
			#pix[w,h]-(255,255,255,255)
			pix[w,h] = (pix[w,h][0],pix[w,h][1],pix[w,h][2],0)#这里不能写浮点数如0.5

#加一个HelloWorld mask
def mask(img):
	width,height = img.size
	im = Image.new('RGBA',(width,height),'white')#构造图像
	draw = ImageDraw.Draw(im)#构造画笔
	font = ImageFont.truetype("arial.ttf", 36)#构造字体
	draw.ink = 0+0*256+0*256*256#设置画笔颜色
	draw.text((0,0),'Hello World',font = font)#左上角在0,0写字
	pix = im.load()
	for h in xrange(height):
		for w in xrange(width):
			if pix[w,h][0]==0 and pix[w,h][1]==0 and pix[w,h][2]==0:
				pix[w,h] = (pix[w,h][0],pix[w,h][1],pix[w,h][2],255)
			else:
				pix[w,h] = (pix[w,h][0],pix[w,h][1],pix[w,h][2],0)
	img.paste(im,mask=im)
	img.show()

def maskWithPix(img,Wid=100,Hei=100):
	width,height = img.size
	mask = Image.new('L',(Wid,Hei),'white')
	pix = mask.load()#构造mask 是数组4
	for h in xrange(Hei):
		for w in xrange(Wid):
			if w==Wid/2 or h==Hei/2 or w+h==Hei/2:
				pix[w,h]=255
			else:
				pix[w,h]=0
	box=[0,0,Wid,Hei]
	#mask标识的地方用红色填充-构造一个红图就可以了
	img.paste(Image.new('RGB',(Wid,Hei),'Red'),box=box,mask=mask)
	img.show()

if __name__ == '__main__':
	main()




