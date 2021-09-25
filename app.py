# encoding:utf8

import os
import baidupan


from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# 有问题: ./js找不到路径; 
# @app.route('/index')
# def index():
#     return app.send_static_file("index.html")

@app.route('/key')
def key():
    return '0123456789ABCDEF'

@app.route("/videos/<dir_name>/<video_name>/<file_name>")
def video_file(dir_name, video_name,file_name):
    dir_name = str(dir_name)
    video_name = str(video_name)
    file_name = str(file_name)
    file_content = baidupan.get_file_bytes_2(dir_name, video_name,file_name)
    content_type = "application/octet-stream"
    headers = {
        "Content-Type": content_type
    }
    # (response, status, headers)
    return (file_content, 200, headers)
 

@app.route("/videos")
def videos():
    list = baidupan.get_dir_list()
    return jsonify(list)

@app.route("/dirs")
def dirs():
    list = baidupan.get_list()
    return jsonify(list)
    
@app.route("/dirs/<dir_name>")
def get_video_list(dir_name):
    dir_name = str(dir_name)
    list = baidupan.get_video_list(dir_name);
    return jsonify(list)






