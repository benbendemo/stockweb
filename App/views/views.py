from flask import (Blueprint, 
                    render_template, 
                    redirect, 
                    url_for, 
                    request, 
                    flash,
                    send_from_directory,
                    make_response,
                    Response,
                    abort,
                    session,
                    g,
                    current_app,
                    jsonify)
from sqlalchemy import and_, or_
from App.exts import db, cache, mail
from App.utils import send_sms, encode_content, _decorator
from flask_mail import Message
import os
import random
import time
import hashlib

basepath = os.path.dirname(__file__)
blue = Blueprint('blue', __name__)

@blue.route('/', methods=['GET', 'POST'])
@_decorator
def index():
    # print('index name:', index.__name__)
    current_app.logger.info('views.py run index function')
    return 'Hello Flask'
    # return render_template('index.html', msg='You need to go bed')

@blue.route('/stockdata/', methods=['GET', 'POST'])
def stockdata_index():
    current_app.logger.info('views.py run stockdata_index function')
    print('stockdata_index name:', stockdata_index.__name__)
    return render_template('/stockdata/index2.html')

@blue.route('/index2', methods=['GET', 'POST'])
def index2():
    current_app.logger.info('views.py run index2 function')
    return render_template('/stockdata/bootstrap_base.html')

@blue.route('/wx')
def wx():
    current_app.logger.info('views.py run wx function')
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    token = 'wechatwebapp20191215'

    compose_list = [token, timestamp, nonce]
    compose_list.sort()
    sha1 = hashlib.sha1()

    # should comment map function as it only works in py2
    # map(sha1.update, compose_list); should use below for py3 refer to below url
    # https://www.cnblogs.com/roadwide/p/10566946.html
    sha1.update(compose_list[0].encode('utf-8'))
    sha1.update(compose_list[1].encode('utf-8'))
    sha1.update(compose_list[2].encode('utf-8'))
    hashcode = sha1.hexdigest()

    if hashcode == signature:
        return echostr
    else:
        return 'wx signature check failed'

# 给蓝图添加一个before_request钩子函数，用于处理blue这个蓝图下所有app
# 接收到的request请求
@blue.before_request
def before():
    g.msg_begin = '蓝图before_request开始'
    print(g.msg_begin)
    print('before_request request.url:', request.url)

@blue.after_request
def after(resp):
    g.msg_end = '蓝图after_request开始'
    print(g.msg_end)
    config = current_app.config
    print('after_request config:', len(config))
    return resp

@blue.route('/getshow/')
def getshow():
    
    t = request.args.get('t', type=int)
    print('getshow t:', t)

    c = time.time() * 1000
    print('getshow c:', c)

    if c > t and (c - t < 1000):
        with open(os.path.join(basepath, 'static/js/security.js'), 'r') as fp:
            js_content = fp.read()
        return js_content
    else:
        return 'could not be show'
