# https://qiita.com/NAKA_G/items/f34738df364af8cbd58e

from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from PDF_maker import generater_status

app = Flask(__name__)
host='0.0.0.0'
# host = 'localhost'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# db = SQLAlchemy(app)

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(30), nullable=False)
#     detail = db.Column(db.String(100))
#     due = db.Column(db.DateTime, nullable=False)

pdf_status = generater_status()

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    # status_list = pdf_status.get_status_4Web()
    # print(status_list)
    return render_template('create.html')

@app.route('/status_list')
def status_list():
    status_list = pdf_status.get_status_4Web()
    return render_template('status_list.html',st_list=status_list)

@app.route('/result')
def result():
    # print('request.method',request.method)
    if request.method == 'GET':
        PDF_name = request.args.get('pdf')
        band_width = request.args.get('band_width')
        num_sample = request.args.get('num_sample')
        time_stamp = request.args.get('time_stamp')
        generation_time = request.args.get('generation_time')
        num_sample = request.args.get('num_sample')
        response_time = request.args.get('response_time')
        time_stamp_response = request.args.get('time_stamp_response')
        div = request.args.get('div')
        graph_range = request.args.get('graph_range')
        time_stamp_response = request.args.get('time_stamp_response')
        # print('title',title)
        # print(PDF_name,band_width,num_sample,time_stamp)
        st_list = [PDF_name,band_width,num_sample,time_stamp,generation_time,response_time,div,graph_range,time_stamp_response]
        pdf_status.change_status(PDF_name,band_width,num_sample,time_stamp,generation_time,response_time,div,graph_range,time_stamp_response)
    return render_template('result.html',st_list=st_list)

@app.route('/status')
def status():
    print('request.method',request.method)
    # st_flag, status_list = pdf_status.get_status()
    status_list = pdf_status.get_status()
    # return status_list
    status_txt = str(status_list)
    return status_txt# pdf_status.get_status()

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(debug=True, host=host, port=801)
    app.run()