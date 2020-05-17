import os
import redis
BASE_DIR = os.path.dirname(os.path.abspath('__file__'))

def get_db_uri(dbinfo):

    dbtype = dbinfo.get('DBTYPE') or 'sqlite'
    dbdriver = dbinfo.get('DBDRIVER') or 'sqlite'
    dbuser = dbinfo.get('DBUSER') or ''
    dbpwd = dbinfo.get('DBPWD') or ''
    dbhost = dbinfo.get('DBHOST') or ''
    dbport = dbinfo.get('DBPORT') or ''
    dbname = dbinfo.get('DBNAME') or ''
    
    return '{}+{}://{}:{}@{}:{}/{}'.format(dbtype, 
                                            dbdriver, 
                                            dbuser,
                                            dbpwd,
                                            dbhost,
                                            dbport,
                                            dbname)

class BaseConfig():

    BASE_DIR = BASE_DIR
    DEBUG = False
    TESTING = False

    # 禁止对象追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 使用flask_upload时需要设置一个SECRET_KEY
    # 使用Flask session技术时也需要设置它
    SECRET_KEY = 'something_secret'

    # 如果使用flask-session则需要设置SESSION_TYPE，它可以为null, redis,
    # memcached,filesystem,mongodb,sqlalchemy等
    # 不设置的话，SESSION_TYPE默认值为null
    SESSION_TYPE = 'redis' 

    # SESSION_PERMANENT值为True表示长期有效，False表示关闭浏览器session失效
    # SESSION_PERMANENT默认值为True
    SESSION_PERMANENT = False

    # 设置session有效期时间，单位为秒
    PERMANENT_SESSION_LIFETIME = 3600 
    
    # 是否对存储在cookie里的session值进行加密
    SESSION_USE_SIGNER = False

    # 设置session中保存值的前缀
    SESSION_KEY_PREFIX = 'flasksession:'

    # 设置redis地址
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379', db=2)
    
    # 下面3个参数仅在flask_upload拓展里使用
    print('settings.py BASE_DIR:', BASE_DIR)
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'App/static/upload')
    UPLOADED_FILES_DEST = os.path.join(BASE_DIR, 'App/static/upload')
    UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'App/static/upload')

    # 设置flask-debug-toolbar开关
    DEBUG_TB_ENABLED = False

    # 设置flask-debug-toolbar是否打开profiler性能分析开关
    DEBUG_TB_PROFILER_ENABLED = True

    # 设置flask-debug-toolbar是否拦截重定向请求开关
    DEBUG_TB_INTERCEPT_REDIRECTS = True

    # 以下设置flask_caching配置参数
    CACHE_DEFAULT_TIMEOUT = 60*5
    CACHE_TYPE = 'redis' # 使用redis作为缓存
    CACHE_KEY_PREFIX = 'flask_cache:'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_PASSWORD = 1234567
    CACHE_REDIS_DB = 2
    
    # 一键配置cache_redis_url
    CACHE_REDIS_URL = 'redis://jackson:1234567@localhost:6379/2'

    # flask_email配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'ben_0910@163.com'
    MAIL_PASSWORD = 'wy2020'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # 配置网易云信
    WYYX_APP_KEY = 'c2ddbc9a092c318f5e7f137c8bda5711'
    WYYX_APP_SECRET = 'b5df98f7dbd4'

    # 配置bootstrap加载本地资源
    BOOTSTRAP_SERVE_LOCAL = True

    # 获取docker-compose文件里的变量
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', '')
    POSTGRES_USER = os.getenv('POSTGRES_USER', '')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
    POSTGRES_DB = os.getenv('POSTGRES_DB', '')

class DevelopConfig(BaseConfig):

    DEBUG = True
    dbinfo = {
        'DBTYPE': 'mysql',
        'DBDRIVER': 'pymysql',
        'DBUSER': 'jackson',
        'DBPWD': 123456,
        'DBHOST': 'localhost',
        'DBPORT': '3306',
        'DBNAME': 'stockdata'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    
class TestConfig(BaseConfig):

    DEBUG = True
    dbinfo = {
        'DBTYPE': 'postgresql',
        'DBDRIVER': 'psycopg2',
        'DBUSER': 'jackson',
        'DBPWD': 123456,
        'DBHOST': 'localhost',
        'DBPORT': 5432,
        'DBNAME': 'stockdata'
    }
    if BaseConfig.POSTGRES_HOST != '' and BaseConfig.POSTGRES_DB != '':
        dbinfo = {
        'DBTYPE': 'postgresql',
        'DBDRIVER': 'psycopg2',
        'DBUSER': BaseConfig.POSTGRES_USER,
        'DBPWD': BaseConfig.POSTGRES_PASSWORD,
        'DBHOST': BaseConfig.POSTGRES_HOST,
        'DBPORT': 5432,
        'DBNAME': BaseConfig.POSTGRES_DB
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    print('settings.py SQLALCHEMY_DATABASE_URI:', SQLALCHEMY_DATABASE_URI)

class StagingConfig(BaseConfig):

    DEBUG = True
    dbinfo = {
        'DBTYPE': 'mysql',
        'DBDRIVER': 'pymysql',
        'DBUSER': 'jackson',
        'DBPWD': 123456,
        'DBHOST': 'localhost',
        'DBPORT': '3306',
        'DBNAME': 'flask_qfedu_views'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

class ProductConfig(BaseConfig):

    DEBUG = False
    dbinfo = {
        'DBTYPE': 'mysql',
        'DBDRIVER': 'pymysql',
        'DBUSER': 'jackson',
        'DBPWD': 123456,
        'DBHOST': 'localhost',
        'DBPORT': '3306',
        'DBNAME': 'flask_qfedu_views'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

config = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}