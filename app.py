from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>欢迎来到 Flask 简易程序！</h1><p>这是首页。</p>'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'<h1>Hello, {name}!</h1>'
    else:
        return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
