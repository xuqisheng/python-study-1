#encoding:utf-8
import urllib,urllib2,cookielib
from PIL import Image
import os

def createOpennerWithLogInHeader(cj):
    '''
    返回伪造了浏览器头的openner，防止被拒绝链接
    头抄自Chrome
    :param cj:CookieJar，用于初始化openner，自动管理cookie
    :return:urllib2.OpenerDirector 返回伪造了浏览器头的openner，防止被拒绝链接
    '''
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #浏览器header
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    opener.addheaders.append(('Accept','application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'))
    opener.addheaders.append(('Accept-Encoding','gzip,deflate,sdch'))
    opener.addheaders.append(('Accept-Language','en-US,en;q=0.8,ja;q=0.6'))
    opener.addheaders.append(('Cache-Control','max-age=0'))
    opener.addheaders.append(('Connection','keep-alive'))
    opener.addheaders.append(('DNT','1'))
    opener.addheaders.append(('Host','ids.hit.edu.cn'))
    opener.addheaders.append(('Refer','http://219.217.227.152:8080/hitgsmis/main.do'))
    opener.addheaders.append(('Upgrade-Insecure-Requests','1'))
    return opener

def login(site):
    '''
    用于哈工大统一身份认证登录
    返回登录后的openner
    :param site:统一身份认证登录网址
    :return:(CookieJar,OpenerDirector) - (cj,openner)
    '''
    #cookie自动管理
    cj = cookielib.CookieJar()
    urlopener = createOpennerWithLogInHeader(cj)
    urllib2.install_opener(urlopener)
    #解析Lt dllt execution _eventId rmShown
    #服务端发送的验证码和这五个字段对应，我猜实现是：
    #   1.浏览器Get，服务端返回一个带这些标记字段的页面
    #   2.下一个被请求的验证码，会和上一个标记字段对应
    #   3.页面Post表单，根据表单中的lt去找对应验证码，再看匹配不匹配
    #缺点是坏人一直刷新验证码，会导致映射错误；网络过慢会导致映射错误
    #print(cj)#查看cookie的变化
    re = urlopener.open(site)
    #print(cj)#查看cookie的变化
    content = re.read()
    features = ['input type="hidden" name="lt" value="',
                'input type="hidden" name="dllt" value="',
                'input type="hidden" name="execution" value="',
                'input type="hidden" name="_eventId" value="',
                'input type="hidden" name="rmShown" value="'
                ]
    label = ['lt','dllt','execution','_eventId','rmShown']
    label_map = {}
    for i in range(len(features)):
        start = content.find(features[i])+len(features[i])
        end = content.find('"',start)
        label_map[label[i]] = content[start:end]
    #验证码
    captchaURL = 'http://ids.hit.edu.cn/authserver/captcha.html'
    re = urlopener.open(captchaURL)
    #print(cj)#查看cookie的变化
    path = 'e:/TEMP/tmp.jpg'
    out = open(path,'wb')
    out.write(re.read())
    out.close()
    img = Image.open(path)
    img.show()
    user = raw_input("username:")
    pwd = raw_input('password:')
    captcha = raw_input("captcha:")
    #构造post values
    values = {
        'username':user,
        'password':pwd,
        'captchaResponse':captcha
    }
    for i in range(len(label)):
        values[label[i]] =  label_map[label[i]]
    #print(values)#输出Post表单信息
    actionURL='http://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2F219.217.227.152%3A8080%2Fhitgsmis%2FindexActionCAS.do'
    re = urlopener.open(actionURL,urllib.urlencode(values))
    #print(cj)#查看cookie的变化
    #print(re.read())
    return cj,urlopener



if __name__ == '__main__':
    #login url
    site = 'http://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2F219.217.227.152%3A8080%2Fhitgsmis%2FindexActionCAS.do'
    cj,urlopener = login(site)
    #试一下
    testURL = 'http://219.217.227.152:8080/WebReport/ReportServer?reportlet=/hit/xj_001.cpt&amp;xh=15S003086'
    testPath = 'e:/毕业图像采集不找证明.html'
    re = urlopener.open(testURL)
    content = re.read()
    print(content)
    out = open(testPath,'w')
    out.write(content)
    out.close()