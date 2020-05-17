from flask import Flask
from App.views import init_views
from App.apis import init_restapi
from App.exts import init_exts
from App.settings import config
from App.middleware import load_middleware

def init_flask_app(env):

    app = Flask(__name__)
    # 加载settings配置
    app.config.from_object(config.get(env))
    # print("base_dir:", app.config.items())
    return app

def create_app(env):

    # 创建flask app
    app = init_flask_app(env)

    # 加载中间件
    load_middleware(app)
    
    # 加载拓展库
    init_exts(app)

    # 加载视图函数
    init_views(app)

    # 加载restful_api视图函数
    # 与路由相关的flask拓展都单独拎出来写成一个独立文件，不要放在exts.py模块里面
    init_restapi(app)

    return app
