from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
# flask_cache只能用在低于1.0.0版本里面
# from flask_cache import Cache   
from flask_caching import Cache
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
cache = Cache(config={
    # simple表示一级缓存，使用本地Python字典存储
    'CACHE_TYPE': 'simple',
    # 默认过期时间300秒
    'CACHE_DEFAULT_TIMEOUT': 60*5
})

cache1 = Cache(config={
    'CACHE_REDIS_URL': 'redis://jackson@localhost:6379/2'
    # 'CACHE_REDIS_URL': 'redis://jackson:1234567@localhost:6379/2'
})
mail = Mail()

def init_exts(app):
    db.init_app(app)
    # db.reflect(app=app)
    migrate.init_app(app, db)
    Bootstrap(app)
    # toolbar.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
    # with app.app_context():
    #    db.reflect()
    # all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    # print('models.py all_table:', all_table, type(all_table))
    # table_one = all_table.get('goods')
    # print('table_one:', type(table_one), dir(table_one), table_one.metadata)
    # Session(app)
