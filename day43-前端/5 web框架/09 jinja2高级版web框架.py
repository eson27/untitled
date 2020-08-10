'''
实现 用户请求--从sql读数据--替换html数据 --响应请求
1.使用 py 标准库 - wsgiref 库 处理服务请求数据 -注：django 是基于wsgiref开发的web框架
2. 与 mysql 交换数据 https://www.cnblogs.com/clschao/articles/9907529.html
    mysql 配置自动root用户登陆方法
        在mysql安装文件夹根目录下\my.ini 添加语句
            user=root
            password=123
        cmd中输入mysql 回车进入 输入 select user() -> 查看已直接是 root
        本例中 新创建 一个库--webtest1
            mysql> create database webtest1
             mysql> use webtest1
        2.1使用pymsql 来操作表  --先用pymsql 创建一个空表  userinfo-->8.1 pymsql_for_web.py
            创建好后cmd ->查看表
                mysql> show tables;  看数据库包含表
                 mysql> desc userinfo; 查表头信息  本例表有三列 id|name|age
        2.2使用pymsql 操作表  添加一条数据 id|name|age  -> 1|小a|18  --8.2 pymsql_insertdata.py
            运行py文件 8.2 pymsql_insertdata.py
                查看表内行信息
                    mysql> select * from userinfo;
        2.3 使用pymsql 操作表  读取一条数据

3. html页面字符串替换--有封装好的模块 https://www.cnblogs.com/clschao/articles/10391859.html
    二 模板渲染JinJa2
　　  上面的代码实现了一个简单的动态页面(字符串替换)，
        我完全可以从数据库中查询数据，然后去替换我html中的对应内容（专业名词叫做模板渲染，你先渲染一下，再给浏览器进行渲染），
        然后再发送给浏览器完成渲染。 这个过程就相当于HTML模板渲染数据。
        本质上就是HTML内容中利用一些特殊的符号来替换要展示的数据。
        我这里用的特殊符号是我定义的，其实模板渲染有个现成的工具： jinja2　
    下载：pip install jinja2
    载入 ：







3.environ--请求数据字典
{
	'ALLUSERSPROFILE': 'C:\\ProgramData',
	'APPDATA': 'C:\\Users\\wqlai\\AppData\\Roaming',
	'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files',
	'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
	'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
	'COMPUTERNAME': 'DESKTOP-P2O8IQC',
	'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe',
	'CONFIGSETROOT': 'C:\\WINDOWS\\ConfigSetRoot',
	'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
	'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',
	'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
	'HOMEDRIVE': 'C:',
	'HOMEPATH': '\\Users\\wqlai',
	'LOCALAPPDATA': 'C:\\Users\\wqlai\\AppData\\Local',
	'LOGONSERVER': '\\\\DESKTOP-P2O8IQC',
	'NUMBER_OF_PROCESSORS': '4',
	'ONEDRIVE': 'C:\\Users\\wqlai\\OneDrive',
	'OS': 'Windows_NT',
	'PATH': 'C:\\Program Files (x86)\\Python38-32\\Scripts\\;C:\\Program Files (x86)\\Python38-32\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\mysql-5.6.47-winx64\\bin;C:\\Program Files\\Git\\cmd;C:\\Program Files\\dotnet\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Users\\wqlai\\Downloads\\swigwin-3.0.12\\;C:\\Users\\wqlai\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\JetBrains\\PyCharm 2019.3.4\\bin;',
	'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW',
	'PROCESSOR_ARCHITECTURE': 'x86',
	'PROCESSOR_ARCHITEW6432': 'AMD64',
	'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 78 Stepping 3, GenuineIntel',
	'PROCESSOR_LEVEL': '6',
	'PROCESSOR_REVISION': '4e03',
	'PROGRAMDATA': 'C:\\ProgramData',
	'PROGRAMFILES': 'C:\\Program Files (x86)',
	'PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
	'PROGRAMW6432': 'C:\\Program Files',
	'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules',
	'PUBLIC': 'C:\\Users\\Public',
	'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2019.3.4\\bin;',
	'PYCHARM_DISPLAY_PORT': '63966',
	'PYCHARM_HOSTED': '1',
	'PYTHONIOENCODING': 'UTF-8',
	'PYTHONPATH': 'C:\\Users\\wqlai\\PycharmProjects\\untitled;C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\helpers\\pycharm_matplotlib_backend;C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\helpers\\pycharm_display',
	'PYTHONUNBUFFERED': '1',
	'SESSIONNAME': 'Console',
	'SYSTEMDRIVE': 'C:',
	'SYSTEMROOT': 'C:\\WINDOWS',
	'TEMP': 'C:\\Users\\wqlai\\AppData\\Local\\Temp',
	'TMP': 'C:\\Users\\wqlai\\AppData\\Local\\Temp',
	'USERDOMAIN': 'DESKTOP-P2O8IQC',
	'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-P2O8IQC',
	'USERNAME': 'wqlai',
	'USERPROFILE': 'C:\\Users\\wqlai',
	'WINDIR': 'C:\\WINDOWS',
	'SERVER_NAME': 'DESKTOP-P2O8IQC',
	'GATEWAY_INTERFACE': 'CGI/1.1',
	'SERVER_PORT': '8080',
	'REMOTE_HOST': '',
	'CONTENT_LENGTH': '',
	'SCRIPT_NAME': '',
	'SERVER_PROTOCOL': 'HTTP/1.1',
	'SERVER_SOFTWARE': 'WSGIServer/0.2',
	'REQUEST_METHOD': 'GET',
	'PATH_INFO': '/',
	'QUERY_STRING': '',
	'REMOTE_ADDR': '127.0.0.1',
	'CONTENT_TYPE': 'text/plain',
	'HTTP_HOST': '127.0.0.1:8080',
	'HTTP_CONNECTION': 'keep-alive',
	'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
	'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
	'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'HTTP_SEC_FETCH_SITE': 'none',
	'HTTP_SEC_FETCH_MODE': 'navigate',
	'HTTP_SEC_FETCH_USER': '?1',
	'HTTP_SEC_FETCH_DEST': 'document',
	'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br',
	'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9',
	'wsgi.input': < _io.BufferedReader name = 764 > ,
	'wsgi.errors': < _io.TextIOWrapper name = '<stderr>'
	mode = 'w'
	encoding = 'utf-8' > ,
	'wsgi.version': (1, 0),
	'wsgi.run_once': False,
	'wsgi.url_scheme': 'http',
	'wsgi.multithread': False,
	'wsgi.multiprocess': False,
	'wsgi.file_wrapper': < class 'wsgiref.util.FileWrapper' >
}


'''
# # 1.原版 copy from https://www.cnblogs.com/clschao/articles/10391859.html
# from wsgiref.simple_server import make_server
# # wsgiref本身就是个web框架，提供了一些固定的功能（请求和响应信息的封装，不需要我们自己写原生的socket了也不需要咱们自己来完成请求信息的提取了，提取起来很方便）
# #函数名字随便起
# def application(environ, start_response):
#     '''
#     :param environ: 是全部加工好的请求信息，加工成了一个字典，通过字典取值的方式就能拿到很多你想要拿到的信息
#     :param start_response: 帮你封装响应信息的（响应行和响应头），注意下面的参数
#     :return:
#     '''
#     start_response('200 OK', [('k1','v1'),]) #响应的 响应行和响应头
#     print(environ)
#     print(environ['PATH_INFO'])  #输入地址127.0.0.1:8000，这个打印的是'/',输入的是127.0.0.1:8000/index，打印结果是'/index'
#     return [b'<h1>Hello, web!</h1>'] # 响应的数据
#
# #和咱们学的socketserver那个模块很像啊
# httpd = make_server('127.0.0.1',9000,application)
#
# print('Serving HTTP on port 8001...')
# # 开始监听HTTP请求:
# httpd.serve_forever()

# 2. 自已写项目

from wsgiref.simple_server import make_server
import time
import pymysql
from pymsql_showdata import showdata
from jinja2 import Template

# wsgiref本身就是个web框架，提供了一些固定的功能（请求和响应信息的封装，不需要我们自己写原生的socket了也不需要咱们自己来完成请求信息的提取了，提取起来很方便）
#函数名字随便起
# 自已写的用户操作内容

req = {'/':'./09 jinja2版web页面.html',
       '/04test.css':'./04test.css',
       '/04test.js':'./04test.js',
       '/1.jpg':'./1.jpg',
       '/04web.ico':'./04web.ico',

       }

# print(time.time())

#使用函数-方程单个请求动作控制


def html(path):
    # with open(path,'rb') as f:
    #     data=f.read()
    # conn.send(data)
    # conn.close()

    # 加入动态控制效果
    # timp_tag=str(time.time())
    # time_show=time.strftime('%Y-%m-%d %H:%M:%S')
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

def css(path):
    with open(path,'rb') as f:
        data=f.read()
    return data
r2=css
def js(path):
    with open(path,'rb') as f:
        data=f.read()
    return data

def jpg(path):
    with open(path,'rb') as f:
        data=f.read()
    return data


def icon(path):
    with open(path,'rb') as f:
        data=f.read()
    return data

func_use = {'/':html,'/04test.css':css,'/04test.js':js,'/1.jpg':jpg,'/04web.ico':icon}
# wsgiref 部分
def application(environ, start_response):
    '''
    :param environ: 是全部加工好的请求信息，加工成了一个字典，通过字典取值的方式就能拿到很多你想要拿到的信息
    :param start_response: 帮你封装响应信息的（响应行和响应头），注意下面的参数
    :return:
    '''
    start_response('200 OK', [('k1','v1'),]) #响应的 响应行和响应头
    # print(environ)
    print(environ['PATH_INFO'])  #输入地址127.0.0.1:8000，这个打印的是'/',输入的是127.0.0.1:8000/index，打印结果是'/index'
    p_info=environ['PATH_INFO']
    if p_info in func_use:
        data=func_use[p_info](req[p_info])
        return [data] # 响应的数据 --list形式
    else:
        return [b'404 data not found']

#和咱们学的socketserver那个模块很像啊
httpd = make_server('127.0.0.1',8000, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
