# https://qiita.com/NAKA_G/items/f34738df364af8cbd58e

from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
host='0.0.0.0'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# db = SQLAlchemy(app)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(30), nullable=False)
#     detail = db.Column(db.String(100))
#     due = db.Column(db.DateTime, nullable=False)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/result')
def result():
    print('request.method',request.method)
    if request.method == 'GET':
        title = request.args.get('band_width')
        print('title',title)
    return render_template('result.html')

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(debug=False, host='0.0.0.0', port=80)]
    app.run()