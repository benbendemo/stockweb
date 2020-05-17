import requests
import time

def get_data():
    # 启动flask web服务器之后，执行这个程序测试http请求头里的UA-header

    # 向服务器端发送request请求，服务器端restful api里的reqparse.RequestParser类
    # 能够判断得出该request请求对应的User-Agent是爬虫而不是浏览器
    url = 'http://127.0.0.1:5000/'
    resp = requests.get(url)
    print('resp.content:', resp.content.decode('UTF-8'))

def loop_get_data():
    for i in range(10):
        t0 = time.time()
        get_data()
        t1 = time.time()
        print(f'It take {t1-t0} time')

if __name__ == '__main__':
    # get_data()
    loop_get_data()