#encoding:utf-8
import urllib2
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8') 


def main(): 
	headerFromBrowser = '''cookie:PREF=ID=1111111111111111:FF=2:LD=zh-CN:TM=1445776741:LM=1449717466:GM=1:V=1:S=mITv5Q0PDfwmZkR6; SID=DQAAABMBAAAqwRTgTlnqeFrBwAJVTGQzcglHg_t1e2VMfAR0T9enapNhhDvxAsqdursupD0usV9tax8MQpFrq8hWyfzarwIFffpcRZR6axqt0INPlsVO7sIPII8dVDi2zrYrPP6f3YDddfj8jfoWdezKKpIcfCDujkl14SEBby1-hdlraMhKvbM9Ab4ZQatDz2CKzNRpZ3kqK1baqXFEBMwLMZB68fjl6LDKjKYf_vx-a6fvsisUMNpNV13cfwBRo5mV77QPU9vlWaoOZP3P0RbB_CGp4bwB1K_hddAVcrgF3dSUEy48cVOQYdyRDWwOwSr-uEQvnGWTYBvdxvF55oR9Ld4ZBrtOQjAXYf1rJ6mRn1XS5WN60sZNkQNywWnOxcH4dHaUaVM; HSID=ANguIJ7HWEZ6PWkz3; SSID=AXd337NyqcWWw8HFg; APISID=I8G2xfo4RWbRYrY5/AxmVt_OTEUPB5bDZN; SAPISID=56PIxvY_oayixZwt/AqnXdaQ15Fup-lwAh; NID=74=m4TanFq8XiiNlzZTFjvCcyeFJ60Ffz_bCvB_9O0BnlSfWgOWlcOn82BZn9Az0hKneigNjl19xJU7-agxehPDsmqGtfuM78crtbssK-o3QDXi-gyy9cahTJelGmYDw1M8nvrny4935ODM1aEG1I3tPS78BlngkmAnvxwI2dacP2FF-EtGNmgLTD8yQzuICY_4E_mT8wsshjyf4kcRc-LcnxkNVrG0--DlTnSsLxdxD577Oz3Ps4iHCkfAEu7bCEIsDtS9_1Ry7BGmclgfHB3mTzqPJU8lYPRGpNpLU7qVfWQ'''
	url = 'http://jwc.hit.edu.cn'
	headers = {}
	for s in headerFromBrowser.split('\n'):
		ss = s.split(':')
		headers[''+ss[0]] = ss[1]
	req = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(req)
	content = response.read()
	print(content)



if __name__ == '__main__':
	main()



