import requests

def get_data():
    # 启动flask web服务器之后，执行这个程序测试http请求头里的UA-header

    # 向服务器端发送request请求，服务器端restful api里的reqparse.RequestParser类
    # 能够判断得出该request请求对应的User-Agent是爬虫而不是浏览器
    url = 'http://127.0.0.1:5000/goods/?g_name=110'
    resp = requests.get(url)
    print('resp.content:', resp.json())

if __name__ == '__main__':
    get_data()