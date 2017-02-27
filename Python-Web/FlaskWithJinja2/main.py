#encoding:utf-8
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

#这是一个通用的匹配,和ip匹配一样有最长原则,即/signin会匹配/signin而不是/<name>.
@app.route('/<name>')
def homeWithName(name):
    return render_template('home.html',name=name)

#GET显示带参的要怎么获取参数呢?比如'localhost:5000/?name=belan'


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/bootstrap-3.3.5-dist/css/test.css')
def css():
    return render_template('./bootstrap-3.3.5-dist/css/test.css')

#xss注入测试-结果：使用jinja2模板会自动转移<，>为&lt和&gt
@app.route('/xss')
def xss_get():
    return render_template('xss.html')
@app.route('/xssPost', methods=['POST'])
def xss_post():
    username = request.form['user']
    #return render_template('signin-ok.html', username=username)
    return '<html>'+username+'</html>'

if __name__ == '__main__':
    app.run()
