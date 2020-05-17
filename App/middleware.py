import time
from flask import request, g 
from flask import current_app
from App.exts import cache
from App.utils import add_ip_into_blacklist, check_ip_in_blacklist

# 设置每秒访问次数
REQUEST_TIME_LIMIT_SECOND = 2
    
def limit_ip_request():
    """Limit http request interval to specified parameter. Please note
    this function should be used within user login scenario. Or the user who
    view the browser will be occasionally stopped by 5 seconds.
    :param key: the key to set
    :param value: the value for the key
    :param timeout: the cache timeout for the key in seconds (if not
                    specified, it uses the default timeout). A timeout of
                    0 idicates that the cache never expires.
    :returns: ``True`` if key has been updated, ``False`` for backend
                errors. Pickling errors, however, will raise a subclass of
                ``pickle.PickleError``.
    :rtype: boolean
    """
    t0 = time.time()
    REQUEST_QUEUE = cache.get('REQUEST_QUEUE') or []
    print('REQUEST_QUEUE1:', REQUEST_QUEUE, type(REQUEST_QUEUE))

    if len(REQUEST_QUEUE) < REQUEST_TIME_LIMIT_SECOND:
        REQUEST_QUEUE.append(t0)
        cache.set('REQUEST_QUEUE', REQUEST_QUEUE)
    else:
        if (t0-REQUEST_QUEUE[0]) < 1:
            print('Visit too soon')
            time.sleep(5)
        REQUEST_QUEUE.append(t0)
        cache.set('REQUEST_QUEUE', REQUEST_QUEUE[1:])
    print('REQUEST_QUEUE2:', REQUEST_QUEUE, type(REQUEST_QUEUE))

def limit_ip_request_by_ip_address():

    IP_BLOCK_FLAG = check_ip_in_blacklist(request.remote_addr)
    if IP_BLOCK_FLAG:
        msg = f'{request.remote_addr} your ip was blocked'
        print(msg)
        return msg

    t0 = time.time()
    REQUEST_LIMIT_DICT = cache.get('REQUEST_LIMIT_DICT') or {}
    print('REQUEST_LIMIT_DICT1:', REQUEST_LIMIT_DICT, type(REQUEST_LIMIT_DICT))

    if request.remote_addr+request.path not in REQUEST_LIMIT_DICT.keys():
        REQUEST_LIMIT_DICT.update({request.remote_addr+request.path: t0})
        cache.set('REQUEST_LIMIT_DICT', REQUEST_LIMIT_DICT)
    else:
        delta = t0-float(REQUEST_LIMIT_DICT.get(request.remote_addr+request.path))
        REQUEST_LIMIT_DICT.update({request.remote_addr+request.path: t0})
        cache.set('REQUEST_LIMIT_DICT', REQUEST_LIMIT_DICT)

        if 0.5 <= delta < 1:
            msg = f'{request.remote_addr} visit too soon'
            print(msg)
            time.sleep(3)
            # return msg
        elif 0.1 <= delta < 0.5:
            msg = f'{request.remote_addr} visit really soon'
            print(msg)
            time.sleep(8)
            # return msg
        elif 0 < delta < 0.1:
            msg = f'{request.remote_addr} your ip would be blocked'
            print(msg)
            add_ip_into_blacklist()
            time.sleep(20)
        else:
            msg = f'{request.remote_addr} visit normally'
            print(msg)
            # return msg
            
    print('REQUEST_LIMIT_DICT2:', REQUEST_LIMIT_DICT, type(REQUEST_LIMIT_DICT))

def display_request_methods():
    print('dir request:', dir(request))
    # for i in dir(request):
    #     if not i.startswith('_'):
    #         print(i, ':', request.__getattr__(i))
    print('request.path:', request.path)
    print('request.referrer:', request.referrer)
    print('request.url:', request.url)
    # print('request.user_agent:', request.user_agent)

def display_current_app_methods():
    print('dir current_app:', dir(current_app))
    for i in dir(current_app):
        if not i.startswith('_'):
            print(i, ':', current_app.__getattr__(i))

def dislay_g_methods():
    print('dir current_app:', dir(g))
    for i in dir(g):
        if not i.startswith('_'):
            print(i, ':', g.__getattr__(i))

def load_middleware(app):
    @app.before_request
    def before():
        print('中间件before_request开始')

        # limit_ip_request()

        # display_request_methods()

        return limit_ip_request_by_ip_address()

        # dislay_g_methods()

        """
        统计
        反爬
        优先级
        用户认证
        用户权限
        """

    @app.after_request
    def after(resp):
        print('中间件after_request结束')
        return resp
        """
        界面里统一动态加载的内容，数据安全
        flask-debug-toolbar就是在after_request里处理
        """