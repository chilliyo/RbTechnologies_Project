from flask import Flask, render_template,request,json
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def demo():
	d = [{'name': 'sui','age': '6'}, {'name':'chen','age':10}, {'name':'xiaochen','age':100}]
	return render_template('data_display.html', lis = d)

if __name__ == '__main__':
    app.run()


