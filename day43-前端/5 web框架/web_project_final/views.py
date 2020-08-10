

from pymsql_showdata import showdata
from jinja2 import Template

def html():
    # with open(path,'rb') as f:
    #     data=f.read()
    # conn.send(data)
    # conn.close()

    # 加入动态控制效果
    # timp_tag=str(time.time())
    # time_show=time.strftime('%Y-%m-%d %H:%M:%S')
    path ='10起飞版webpage.html'
    with open(path,'r',encoding='utf-8') as f:

        data=f.read()
        userinfo_data=showdata()
        print('html',userinfo_data)
        # data=data.replace('页面动态效果--此处每次访问更新为时间戳',a['name']+'我来了')
        tem =Template(data) # jinja2-坑1 --注释的内容有语法字符会出错，模板内小心注释内容包含语法
        data = tem.render({'userinfo':userinfo_data})#jinja2 坑2 （%  xxxx %） 特殊字符--语法字符如{%-不能有空格
        data=data.encode('utf-8')
        print(type(data))
        return data

def css():
    path='./static/css/04test.css'
    with open(path,'rb') as f:
        data=f.read()
    return data
r2=css
def js():
    path = './static/js/04test.js'
    with open(path,'rb') as f:
        data=f.read()
    return data

def jpg():
    path ='./static/img/1.jpg'
    with open(path,'rb') as f:
        data=f.read()
    return data


def icon():
    path = './static/img/04web.ico'
    with open(path,'rb') as f:
        data=f.read()
    return data