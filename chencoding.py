#encoding:utf-8
import sys
import os

def main(decode='gbk',encode='utf-8'):
	'''
	编码转换
	case file:
		inputpath指定的文件进行编码转换，对应写到outputpath路径下
	case dir:
		inputpath路径下的所有文件(递归路径)进行编码转换，对应写到outputpath路径下

	usage:
		python gbk2utf8.py <inputpath> <outputpath> [decode]? [encode]?
	example:
		usr@pc:~/Desktop$ python gbk2utf8.py '/home/ljl/Desktop/out' '/home/ljl/Desktop/gbk' 'utf-8' 'gbk'	
	'''
	inputpath = sys.argv[1]
	outputpath = sys.argv[2]
	if len(sys.argv)>3:
		decode=sys.argv[3]
	if len(sys.argv)>4:
		encode=sys.argv[4]
	if os.path.isfile(inputpath):
		dealFile(inputpath,outputpath,encode,decode)
	elif os.path.exists(inputpath):
		dealDir(inputpath,outputpath,encode,decode)

def dealFile(inputpath,outputpath,encode,decode):
	if not os.path.exists(outputpath):
		os.makedirs(outputpath)
	inobj = open(inputpath,'r')
	outobj = open(os.path.join(outputpath,os.path.split(inputpath)[1]),'w')
	all_text = inobj.read().decode(decode).encode(encode)
	outobj.write(all_text)
	outobj.close()
	inobj.close()

def dealDir(inputpath,outputpath,encode,decode):
	for root, dirs, files in os.walk(inputpath,True):
		subdir=root[len(inputpath):]
		for name in files:
			if not os.path.exists(outputpath+subdir):
				os.makedirs(outputpath+subdir)
			inobj = open(os.path.join(root,name),'r')
			outobj = open(os.path.join(outputpath+subdir+'/',name),'w')
			all_text = inobj.read().decode(decode).encode(encode)
			outobj.write(all_text)
			outobj.close()
			inobj.close()

if __name__=='__main__':
	main()