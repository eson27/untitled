# django学习目录 https://www.cnblogs.com/clschao/articles/10526431.html
# django学习 --引子 --自已写一个完整web框架 从简到全 -9个版本
'''
https://www.cnblogs.com/clschao/articles/10391859.html
1.自已用py写一个简单的web简框
    1.1 写server  回复一个html文件
    1.2 http 协议介绍 --看博客 https://www.cnblogs.com/clschao/articles/9230431.html
        http默认访问的是 :80 端口 （ip地址不加端口号访问的是80端口）
        基本概念中的术语
            1.2.1客户端 -- 指用户
                客户端代理  user agent-- 浏览器 | 爬虫 | 其它网络工具
            1.2.2服务器 -- 指访问的网站
                源服务器 origin server--- 应答的服务器
                    访问过程中间还存在中间层- 代理服务器|网关|隧道tunnel...
            1.2.3请求应答的标准 ---tcp 协议 --主要用get | post 两样基本够用 ---html中用method 属性定义请求方法,不写默认为get
                1.请求 格式 完整分四部分 --  请求行|头部|一行空行|数据



                    get -- 发送用户名密码
                        请求行:GET / HTTP/1.1    -- 请求方法（get、post..）|请求路径(例：clschao/articles/10391859.html）|协议版本|回车符换行符（\r\n)
                            GET / --表示默认访问服务器根目录
                                https://www.cnblogs.com/clschao/articles/10391859.html --表示访问服务器的文件路径
                        头部的:格式为键值对 如 user-agent：XXXX   --- ua 中含浏览响信息--反爬机制需要用到
                        空行 ：\r\n\r\n
                        数据行  get 方法 数据行为空 ,请求的数据为文件路径信息，放在请求行
                                http://127.0.0.1:9001/?username=eson&pwd=123  --get方法本地浏览器可以看到请求数据--用？开产头&分隔
                    head -
                    post --添加数据
                    put --全局更新数据
                    delete --删除数据
                    patch --部分更新数据
                    track
                    option
                        .... 按规范不同方法对应不对的操作但一般get|post基本够用
                2.响应  格式 完整分四部分 --  响应行|头部|一行空行|数据
                        响应行--  HTTP/1.1 200 ok    协议|状态码|状态码解释
                        头部的-- 格式为键值对 如自已写一个 k1:v1 \r\n
                        空行 -- \r\n\r\n
                        数据行 ---如下py-server例中回复的页面数据
                                    with open('1. html回复v1.1.html','rb') as f:
                                        data=f.read()
                                    conn.send(data)
                                    conn.close()

                请求方式: get与post请求区别（通过form表单我们自己写写看）
                GET提交的数据会放在URL之后，也就是请求行里面，以?分割URL和传输数据，参数之间以&相连，如EditBook?name=test1&id=123456.（请求头里面那个content-type做的这种参数形式，后面讲） POST方法是把提交的数据放在HTTP包的请求体中.
                GET提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST方法提交的数据没有限制.
                GET与POST请求在服务端获取请求数据方式不同，就是我们自己在服务端取请求数据的时候的方式不同了，这句废话昂
                    get 请求 常用在-->浏览器输入网址 | a标签（href) | forms标签（method='get')
                    post 请求 常用在--> 数据提交 如 提交用户名密码

                3.响应数据中的-- 状态码
                    1xx消息——请求已被服务器接收，继续处理
                    2xx成功——请求已成功被服务器接收、理解、并接受
                    3xx重定向——需要后续操作才能完成这一请求
                    4xx请求错误——请求含有词法错误或者无法被执行
                    5xx服务器错误——服务器在处理某个正确请求时发生错误
        http协议特点
            基于请求-响应方式|无状态保存（每次访问都是一个新的访问--有缺陷：要解决用户登陆后一直访问问题）| 无连接（有两种模式-直接断开、在connection：keep-alive 声明保持几秒连接）

'''

#一.djanggo 学习第一天
'''
2.djanggo 学习
    2.1.自已写一个web框架 --共8个版本
        web框架分 服务器 | html
    2.2 　九、wsgiref模块版web框架 https://www.cnblogs.com/clschao/articles/10391859.html
        wsgiref模块其实就是将整个请求信息给封装了起来，就不需要你自己处理了，假如它将所有请求信息封装成了一个叫做request的对象，那么你直接request.path就能获取到用户这次请求的路径，request.method就能获取到本次用户请求的请求方式(get还是post)等，那这个模块用起来，我们再写web框架是不是就简单了好多啊
        WSGI（Web Server Gateway Interface）就是一种规范，它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦。

　　　　常用的WSGI服务器有uwsgi、Gunicorn。而Python标准库提供的独立WSGI服务器叫wsgiref，Django开发环境用的就是这个模块来做服务器。


3. djanggo --MVC 框架和 MTV 框架
    MVC 框架
        M--model模块 --程序和数据库接口
        V ---views ---用户自已的业务逻辑
        C -- controller ---控制器 ---服务器 收发操作
    MTV 框架--djanggo 使用的框架 由MVC演变而来
        Django的MTV模式本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django的MTV分别是值：
        M 代表模型（Model）： 负责业务对象和数据库的关系映射(ORM)。
        T 代表模板 (Template)：负责如何把页面展示给用户(html)。
        V 代表视图（View）：   负责业务逻辑，并在适当时候调用Model和Template。
        除了以上三层之外，还需要一个URL分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，View再调用相应的Model和Template
    下载djanggo
            pip3 install django==1.11.9  -->版本不同对有区别--以下有讲 大版本|中版本|小版本 2.X 版 与 1.11.X 版本语法和配置有变化，先学1.11.X版本
            官网：https://www.djangoproject.com/download/
4.创建第一个djanggo项目
        cmd》》 C:\djanggo_project>  django-admin startproject first_dproject 在C:\djanggo_project 下创建项目-》  first_dproject
            注：如果命令不执行 则配置下windows的环境变量
            文件夹结构 -- 一个主程序和一个文件夹包括四个py文件
                    manage.py
                    first_dproject ->__init__.py | settings.py --项目配置工具 | urls.py -urls控制器|wsgi.py--封装了sockect
              manage.py ----- Django项目里面的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管你将框架分了几个文件，必然有一个启动文件，其实他们本身就是一个文件。
                settings.py ---- 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
                urls.py ----- 负责把URL模式映射到应用程序。
                wsgi.py ---- runserver命令就使用wsgiref模块做简单的web server，后面会看到renserver命令，所有与socket相关的内容都在这个文件里面了，目前不需要关注它。
    启动django 项目--
        坑1. 版本不对 安装1.11.9版启动服务出错，更新到1.11.17版本ok ，注：出错就更新到最新的小版本
            报错：SyntaxError: Generator expression must be parenthesized
5.启动django项目
          cmd>>   c:\django_project\first_project>python manage.py runserver 127.0.0.1:8080
                    注：python manage.py runserver  运行默认 127.0.0.1：8000 端口
                     显示   Starting development server at http://127.0.0.1:8080/
                                Quit the server with CTRL-BREAK.
        什么都不写，项目也可以启动运行，浏览器访问返回一些自带的信息

6. 创建app --django项目通过应用 app 实现用户需求 --类似微信下面的应用小程序
    cdm 》》 c:\django_project\first_project>python manage.py startapp app01

        app01文件夹结构
                __init__.py |views.py|models.py|apps.py|admin.py|tests.py| migrations--文件夹内有个__init__.py

      我们现在只需要看其中两个文件

　　　　models.py ：之前我们写的那个名为model的文件就是创建表用的，这个文件就是存放与该app(应用)相关的表结构的

　　　　views.py    ：存放与该app相关的视图函数的
    配置app
        在setting.py  -->INSTALLED_APPS =[] ,将'app01' 字符串添加到列表最后
7. 在pycharm 创建 django项目 -- 以后主要使用pycharm建项目，app会自动进置
    newproject->django -> location 填入C:\django_project\porject_2
                        -> 解释器 选择py38 \  注意 解释器配选下面一项，上面项目虚拟环境应用，限制多不选
                        ->more setting  填写 创建的app 名称--例  app01
8.写一个例子 -- 访问 --> 返回一个模拟用户登陆页-login.html
    写法 : 注pycharm建的文件已默认引入了常用模块
      sep1 - 在templates文件夹下创建 login.html  注：在setting文件已引入的templates文件夹路径，使用用目录下文件都不再用前缀

        sep2 - 在 views 文件里写 用户函数 --本例写：通过render方法 返回login.html
            render方法 实际已包含读文件with open()-- f.read() --return 操作
                 return render(request,'login.html') # render 固定写法 方法 一句语就可以把页面回过去，注意 在setting已经写入了templates文件夹路径，不用再写
         sep3 -- 配置urls文件
            在urls 中 引用 views 再函数名作作url 被调用
             from app01 import views   # 引用view模块的各种函数
                urlpatterns = [url(r'^index/', views.index), ] # 尖括号 表示包含 正则 方法 开头匹配就是 true
        运行项目 --可在右上角配置 默认端口 本例配8080
        访问 http://127.0.0.1:8080/index/

9. 例子 在 pycharm 建 一个django - project_2 项目 模拟一个用户登陆页面


    使用到文件 setting.py | urls.py | views.py | 在templates文件夹-自建logion.html
    sep1: 浏览器器输入网址->得到一个web页面
        输入：http://127.0.0.1:8080/index/  回复 ：logion.html
       1. urls.py-先配置路径
            from app01 import views   # 引用view模块的各种函数
                urlpatterns = [ url(r'^index/', views.index),]  # 尖括号 表示包含 正则 方法 开头匹配就是 true
                    url(r'^index/', views.index)---第1个参数 正则字符串 ;第二个参数 视图函数

        2. views.py 视图函数  2.1 接收数据 get | post 方法  --2.2 回复数据 HttpResponse | render 方法
          函数输入形参 -request  --是一个对象
            获取请求方式  request.method  --> 返回字符串 如 'POST' | 'GET'
            2.1 get 请求的数据获取
                get_data= request.GET -->返回一个含字典的对象用.get方法取字典数据
                    #     username=get_data.get('username')
                        #     password=get_data.get('password')
                 post 请求的数据获取 --使用psot请求先 在setting.py 注释认证
                   post_data = request.POST
                    username=post_data.get('username')
                    password=post_data.get('password')
            2.2 数据返回
                引入方法：
                    from django.shortcuts import render,HttpResponse
                HttpResponse(参数1) 返回数据 --参数->字符串-语法：
                    return HttpResponse('登陆成功')
                render(参数1，参数2） --英文字面意思--渲染
                    return render(request,'login.html')  --参数1 request对象 参数2 - 文件相对路径 ，注意templates路径已引入不用写

'''

#二、urls | views | 模板 -- 响应的对应路径 -请求和对应响应的视图函数关系
'''
二、urls | views | 模板
1. urls
https://www.cnblogs.com/clschao/articles/10403619.html  Django基础二之URL路由系统
    1.1 无名分组
        # url(r'^books/(\d{4})/)', views.books), # 路径- 无名分组--(\d{4}) 正则出2001四位数字- 用户输入http://127.0.0.1:8080/books/2001 ,在views用形参2接收
        url(r'^books/(\d{4})/(\d{1,2})', views.books),#多个无名分组写法用斜杠分隔 ,views用增加形参3接收-例用户输入 http://127.0.0.1:8080/books/2001/12

    1.2 有名分组
         url(r'^books/(?P<year>\d{4})/(?P<month>\d{1,2})', views.books) #路径- 有名分组,views必须用同名参数接收，位置可以不限
    注意事项
        urlpatterns中的元素按照书写顺序从上往下逐一匹配正则表达式，一旦匹配成功则不再继续。
        若要从URL中捕获一个值，只需要在它周围放置一对圆括号（分组匹配）。
        不需要添加一个前导的反斜杠（也就是写在正则最前面的那个/），因为每个URL 都有。例如，应该是^articles 而不是 ^/articles。
        每个正则表达式前面的'r' 是可选的但是建议加上。
        ^articles&  以什么结尾，以什么开头，严格限制路径


    1.3视图函数中指定默认值
    1.4 urls 路由分发 之 include() --示例 project3_urltest
        手动创建app02 ---app01 可以在新建项目时由pycharm创建
          cmd>>  c:\django_project\project2>python manage.py startapp app02
        在setting 配置app02
            pycharm 提供简便方法-- 菜单-> 工具 -> run manage task 后在下方窗口出现manage命令窗口，只要输命令即可不用再找路径
        在项目主文件夹 project3_urltest->urls.py 
            from

'''

#views 视图函数 --djiang 视图函数 -响应请求的方法
'''
三、views 视图  --project4_viewstest
    https://www.cnblogs.com/clschao/articles/10409764.html
    1.请求相关的方法 --方法很多，讲以下一些
        print(a.method) #GET
        print(a.POST)
        print(a.GET)  #<QueryDict: {'username': ['eson'], 'password': ['123']}>
        print(a.body) # b'' 获取 路径后面 get方法是空值，post方法是数据信息
        print(a.path) # /index/
        print(a.path_info) #/index/
        print(a.get_full_path()) #/index/?username=eson&password=123
        print(a.META)  # {xxxx} 请求信息的字典
    2.响应方法 主要讲三个 HttpResponse -回复字符串| render -回复文件| redirect--重定向
        return redirect('/index/') # 重定向后，用户自动按新路径再申请一次页面,浏览器地址栏显示新地址
    
四.CBV和FBV
    BV（function base views） 就是在视图里使用函数处理请求。之前都是FBV模式写的代码，所以就不写例子了。
　　CBV（class base views） 就是在视图里使用类处理请求。
　　Python是一个面向对象的编程语言，如果只用函数来开发，有很多面向对象的优点就错失了（继承、封装、多态）。所以Django在后来加入了  Class-Based-View。可以让我们用类写View。这样做的优点主要下面两种：
            提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
            可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性
            
五 view视图 加 函数装馈器 --project4_viewstest
    CBV和FBV 的 dispatch 方法 --> 在响应路径前加插任务
    FBV本身就是一个函数，所以和给普通的函数加装饰器无差
    使用装饰器装饰CBV 有三种方法 看示例
'''

# 三、模板 template --django的模板语法
'''
三、模板 template --- 例：项目 templatetest
 内容包括 一 语法|二 变量|三 过滤器|四 标签Tags|五 模板继承|六 组件|七 自定义标签和过滤器|八 静态文件相关
https://www.cnblogs.com/clschao/articles/10409764.html


一 语法
# # 1.example1 for test djanggo 模板系统 处理 数据
# def index(request):
#     num = 100
#     name= 'teststrname'
#     name_list = ['nl1','nl2','nl3']  #<p>{{name_list_html.2  }}</p>-html模板语言-数列取值 通过.index语法
#     name_dict ={'nd1':'nd1_val','nd2':'nd1_va2','nd3':'nd1_va3'}#<<p>{{ name_dict_html.nd1}}</p>-html模板语言-数列取值 通过.key语法
#
#     #类-返回
#     class a:  # html语 <p>{{ c_html }}</p>-> 访问返回 <app01.views.index.<locals>.a object at 0x04297430>
#         def __init__(self):
#             self.kind='dog' # html语 <p>{{ c_html.kind }}</p>--> 访问返回  dog
#         def eat(self):
#             return '狗吃狗粮' # html语 <p>{{ c_html.eat}}</p>--> 访问返回狗吃狗粮 注：方法后不加括号，也不能传参，函数功能有限制
#
#
#     return render(request,'index.html',{'num_html':num,'name_html':name,'name_list_html':name_list,'name_dict_html':name_dict,'c_html':a}) # 坑：不能有空格
二 变量
三 过滤器--Django的模板语言中提供了大约六十个内置过滤器。
    过滤器的语法： {{ value|filter_name:参数 }}
    default --设置变量默认值|length-测量变量长度|filesizeformat--数值转换成MB等|slice-切片|date-转换成日期|safe
认证机制csrf 介绍 在setting.py 中MIDDLEWARE = [   'django.middleware.csrf.CsrfViewMiddleware', ] 设置中间件
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:# post方法直接提交数据提示 Forbidden (403) CSRF verification failed. Request aborted.
        print(request.POST)#<QueryDict: {'csrfmiddlewaretoken': ['GduARb3adLanEkdtJFqBVeB74AWXQZgZD8rDSLEpoXHbmA92RpDRHPueSUrK4RLT'], 'username': ['eson'], 'password': ['323']}>
        return HttpResponse('登陆成功')#要通过验证写在form标签内-{% csrf_token %}
    #csrf认证过程 --请求->发送前生成% csrf_token %}生成一个戳 返回login->post请求时带{'csrfmiddlewaretoken': ['GduARb3adLanEkdtJFqBVeB74AWXQZgZD8rDSLEpoXHbmA92RpDRHPueSUrK4RLT']返回数据

四 标签Tags--这里指模板语法的函数名
        for| if | with -复杂变量起个别名
    
五 模板继承 --如一些后台管理网站，有些站分如导航栏和菜单一直不变，只有操作窗口变化，不变的部分就可做成母板，再继承过来
    Django模版引擎中最强大也是最复杂的部分就是模版继承了。模版继承可以让您创建一个基本的“骨架”模版，它包含您站点中的全部元素，并且可以定义能够被子模版覆盖的 blocks 。
    sep1--做好母板 一般base.html命名 
        sep2-在活动区域设置block函数--content：是形参
                 {% block content %}  
                    <div> 这是母板活动页</div>
                {% endblock %}
        sep3-引用母板和函数
            {% extends 'muban.html' %}
                {% block content %} 
                        {{ block.super }}  # 同时-继承母函数内的内容，不写就不继承          
                         <div>这是mnue1页</div>            
                {% endblock %}  #  也可写成{% endblock content%}
                     
     一般在html 三个部分都预留空位   
六 组件--　　可以将常用的页面内容如导航条，页尾信息等组件保存在单独的文件中，然后在需要使用的地方，文件的任意位置按如下语法导入即可。
    {% include 'navbar.html' %}
    　　组件和插件的简单区别
            组件是提供某一完整功能的模块，如：编辑器组件，QQ空间提供的关注组件 等。           
               而插件更倾向封闭某一功能方法的函数。
                这两者的区别在 Javascript 里区别很小，组件这个名词用得不多，一般统称插件。
七 自定义标签和过滤器  示例 templatetest\app01\templatetags\xx.py
    sep1-在app文件夹下建一个 templatetags 文件夹 必须这个名字
        setp2-在目录下建py文件例- xx.py
            引用django自定义标签的方法
                使用django 内置方法自定义标签
            1.自定义过滤器 --- 一般只需传入参数最多2个时时使用自定义filter方法 ，传多参数时使用 自定义标签方法
              py语法
                   from django import template                   
                    register = template.Library() #register是固定的名字必须这样命名进行注册                   
                    @register.filter
                    def oo(v1):  #一个参数
                        s=v1+'from_templatetags'
                        return s
                    
                    @register.filter
                    def dd(v1,v2):#两个参数
                        s=v1+v2 +'from_templatetags'
                        return s
                html语法  
                     #1.不加自定义过滤器效果#}
                        <p>
                        {{ s1 }}
                        </p>
                        {#2.只有自身作为参数情况#}
                        <p>
                        {% load xx %} #  在使用views.py文件中的变量时在前面加 {% load xx %} --xx是自已写的xx.py文件
                            {{ s1|oo }}
                        </p>
                        {#3.除了自身还多一个参数共2个参数情况#}
                        <p>
                        {% load xx %}
                            {{ s1|dd:'》》连自身两个参数的方法' }}  
             2.自定义标签方法 @register.simple_tag
                 py语法   
                    @register.simple_tag#注：后面不用加括号
                    def mytag(v1,v2,v3):
                        return v1+v2+v3+'这是传多个参数方法：@register.simple_tag.'   
                html语法
                    {% load xx %} # 引入自定义标签方法同自定义过滤器--模板语法使用{%--函数方式
                        {% mytag '》》自定义标签方法--可传多个参数@register.simple_tag+参数1' '+参数2' '+参数3' %} }}
                    </p>         
             3.自定义html组件--@register.inclusion_tag方法--自已写一个xxxx.html,用py函数传到页面
                py语法
                    @register.inclusion_tag('data.html')
                    def func(v1,v2,v3):
                        # data=[11,22,33] # 不带参数方式 html 写法{% load xx %}  {% func %}
                        data =[v1,v2,v3]  # 带参数方式 html 写法{% load xx %} {% func 44 55 66 %} 函数与参数间用空格分隔                   
                        return {'data':data} # 给data.html传参用字典形式
                        
                html语法
                    @register.inclusion_tag('data.html')
                    def func(v1,v2,v3):
                        data1=[11,22,33] # 不带参数方式 html 写法{% load xx %}  {% func %}
                        data =data1+[v1,v2,v3]  # 带参数方式 html 写法{% load xx %} {% func 44 55 66 %} 函数与参数间用空格分隔                 
                        return {'data':data} # 给data.html传参用字典形式                              
                片段页面data.html 写法
                    {% for i in data %}  # 参数名data与py文件传进来的一致
                        <li>{{ i }}</li>
                    {% endfor %}            
           
        八 静态文件相关 --示例项目 statictest --静态文件包括图片|视频|css|js。。
            在django中配置静态文件方法
                sep1 - 根目录中创建 静态文件夹如：’jingtiwenjian‘
                sep2-在setting.py中加上
                    STATICFILES_DIRS =[ os.path.join(BASE_DIR,'jingtaiwenjian'),]
                        -->即 ['C:\\django_project\\statictest\\jingtiwenjian']
                sep3 在html中引入有如下方法
                {# href="/jingtaiwenjian/css1.css"不能生效 -->在setting中作了配置静态路径 static替代了jingtaiwenjian  #}
                {#    <link href="/jingtaiwenjian/css1.css" rel="stylesheet">#}
                {#        引入方式一  setting 中 STATIC_URL = '/static/' 的路径参数 href中/static/ 在 中文件名前加上#}
                {#        <link href="/static/css1.css" rel="stylesheet">#}
                {#        引入方式二 如果不想写成路径可用在文件头加上{% load static %} 配合link中的href='{% static "css1.css" %}'语句的方法引用,这时static是一个变量href中/static/ 在 中文件名前加上,这时static=STATIC_URL#}
                {#            <link href='{% static "css1.css" %}' rel="stylesheet">#}
                {#            引入方式三 用{% load static %} 配合link中的href='{% get_static_prefix %}"css1.css" '语句的方法引用，与方法二其实一样g\#}
                
                            <link href='{% get_static_prefix %}"css1.css" ' rel="stylesheet">
                
            
                                             
                    
                
'''

# 四、ORM-- 数据库操作
'''
演示项目--ormtest
https://www.cnblogs.com/clschao/articles/10427807.html
四、ORM-- 数据库操作 ---ORM为了前端开发降低对sql语言的依赖，也就是说会sql开发可以完成数据操作,会ORM在不会SQL也可以用py的类方法操作数据
4.1 创建表和相关配置
        ORM是“对象-关系-映射”的简称。（Object Relational Mapping，简称ORM）(将来会学一个sqlalchemy，是和他很像的，但是django的orm没有独立出来让别人去使用，虽然功能比sqlalchemy更强大，但是别人用不了)
        在app01\models.py 是专门用业写前于ORM的内容的py文件
        from django.db import models
        # Create your models here.       
        class userinfo(models.Model):# sep1.定义一个类，并继承django 中的models.Model类
            # sep2 定义表的首行表头
            id =models.AutoField(primary_key=True)
            name = models.CharField(max_length=16)
            age =models.IntegerField()
            current_date =models.DateField()
        
            # 翻译成mysql语句 create table userinfo(id int primary key auto_increment,name varchar(16),age int,current_date date)
            # sep3 在Terminal输入py命令生成记录 C:\django_project\ormtest> python manage.py makemigrations
        
            #sep4 在Terminal输入py命令翻译命令成生成数据 C:\django_project\ormtest>python  manage.py migrate
        
            #此时在 ormtest文件夹下生成 db.sqlite3 --注：这是一个django自带小型文件数据库，在生产环境中基本不用这个，只是在调试时用
            #查看数据库--将左边  的db.sqlite3 拖到右边的Database窗口 注：坑--没装数据库驱动不能展开数据库--解决- database窗口菜单Datasource properties 下选中SQLite在右边窗口 drive file中看到未安装就安装下驱动
            # sep5 在database窗口双击app01_userinfo 就可以连上表，进行可视化操作，手动增加数据
            #sep6 以上使用的是默认的sqlite3数据库，需更换为mysql
                # 在 setting -->DATABASES 进行配置，转看setting.py文件
            #sep7 在ormtest->__init__.py 写入import pymysql
                         #写入 pymysql.install_as_MySQLdb()
            #sep8 重复sep3\4
            #sep9 查看表 用mysql时 在cmd命令下 show tables 查看表会看到已生成
            注：C:\Program Files (x86)\Python38-32\Lib\site-packages\django\db\backends\mysql\base.py
                    _data_types ={}字典是orm和mysql语句对应关系，其它数据库同理

4.2 ORM对mysql表的增删改查 --示例项目-ormtest2
    from django.shortcuts import render
    from app01 import models
    
    # Create your views here.
    # def index(request):
    #     #1.1增--ORM插入行 方式一 .save()
    #     student_obj = models.Students(name='学生1',age=18)#类：实例化对象--sql：插入行
    #     student_obj.save()# 类save方法 --sql数据写入
    #
    #     return  render(request,'index.html')
    
        #1.2增--ORM插入行 方式二 .create
        # new_object= models.Students.objects.create(name='学生3',age=6)#类：实例化对象--sql：插入行--习惯称为model对象或表对象
        #
        # # 1.3 增 --ORM插入行 方式三 批量创建方法
        # obj_list=[]
        # for i in range(20):
        #     obj=models.Students(name='批量创建'+str(i),age=i)
        #     obj_list.append(obj)
        # models.Students.objects.bulk_create(obj_list)
    
        # # 2.1 查---ORM-查 --查询方法--查所有数据
        # all_objs = models.Students.objects.all()
        # print('new_object:',new_object,'name:',new_object.name,'age:',new_object.age)#打印结果：new_object: Students object name: 学生3 age: 6
        # print('all_objs',all_objs)#all_objs 是一个ORM定义的object类型,和list相似但有不同--><QuerySet [<Students: Students object>, <Students: Students object>, <Students: Students object>, <Students: Students object>]> 注：要在QuerySet中的元素显示对象的信息要在models.py写返回信息函数def __str__(self)方法
        # #加了__str__方法打印显示 all_objs < QuerySet[ < Students: 学生1 >, < Students: 学生1 >, < Students: 学生2 >, < Students: 学生3 >, < Students: 学生3 >] >
        # # model对象和QuerySet对象对应方法不一样要注意会经常遇到这两个对象
        # # for i in all_objs:
        # #     print(i.name)
    
        # # 2.2 查---ORM-查 --查询方法--条件查询filter方法---返回的queryset集合
        #     注：filter方法有多条结果时返回queryset集合，没有结果返回空集，不会报错
        # objs = models.Students.objects.filter(id=2)
        # print(objs) # 结果--><QuerySet [<Students: 学生1>]>
    
        # # 2.3 查---ORM-查 --查询方法--条件查询get 方法--返回的是models对象
        #     注：get方法如果结果不是唯一|结果不存在都会报错
        # obj = models.Students.objects.get(name='不存在报错')
    
        # obj = models.Students.objects.get(id=1)
        # print(type(obj),obj) # 结果 obj是一个models对象 <class 'app01.models.Students'>    学生1
    
        # #3 删 --ORM删除行方法 -- models对象和queryset集合后都可跟.delete（）方法删除查到的行
        #     # 3.1 删除用get方法获取到的models对象行
        # models.Students.objects.get(id=4).delete()
        # # 3.2 删除用filter方法获取到的queryset 集合-多行
        # models.Students.objects.filter(name='学生2').delete()
        # # # 3.3 删除所有
        # # models.Students.objects.all().delete()
    
        # 4.1 改- ORM更新数据 .update()方法 --注:get方法返回的models对象不能使用update方法，只有filter方法返回的queryset集合可以
        # models.Students.objects.filter(name='学生3').update(age=22)
        # 4.2 改- ORM更新数据 .update_or_create()方法 --有就改没有就创建
        # models.Students.objects.update_or_create(name='有就更就没有就创建',defaults={'age':88})
        return  render(request,'index.html')
        
4.3 ORM对mysql表的查询接口
        <1> all():                  查询所有结果，结果是queryset类型
          
        <2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象，结果也是queryset类型 Book.objects.filter(title='linux',price=100) #里面的多个条件用逗号分开，并且这几个条件必须都成立，是and的关系，or关系的我们后面再学，直接在这里写是搞不定or的
          
        <3> get(**kwargs):          返回与所给筛选条件相匹配的对象，不是queryset类型，是行记录对象，返回结果有且只有一个，
                                    如果符合筛选条件的对象超过一个或者没有都会抛出错误。捕获异常try。  Book.objects.get(id=1)
          
        <4> exclude(**kwargs):      排除的意思，它包含了与所给筛选条件不匹配的对象，没有不等于的操作昂，用这个exclude，返回值是queryset类型 Book.objects.exclude(id=6)，返回id不等于6的所有的对象，或者在queryset基础上调用，Book.objects.all().exclude(id=6)
            作用于 object and queryset 对象-->返回的是queryset对象 -->可以写链式
            Book.objects.exclude(id=6).exclude(id=5)
                　　　　　　　　　　　　　　　　
        <5> order_by(*field):       queryset类型的数据来调用，对查询结果排序,默认是按照id来升序排列的，返回值还是queryset类型
        　　　　　　　　　　　　　　　　  models.Book.objects.all().order_by('price','id') #直接写price，默认是按照price升序排列，按照字段降序排列，就写个负号就行了order_by('-price'),order_by('price','id')是多条件排序，按照price进行升序，price相同的数据，按照id进行升序
                
        <6> reverse():              queryset类型的数据来调用，对查询结果反向排序，返回值还是queryset类型
                排序之后反转 models.Book.objects.all().order_by('id').reverse()
                    
          
        <7> count():                queryset类型的数据来调用，返回数据库中匹配查询(QuerySet)的对象数量。
          
        <8> first():                queryset类型的数据来调用，返回第一条记录 Book.objects.all()[0] = Book.objects.all().first()，得到的都是model对象，不是queryset
          
        <9> last():                queryset类型的数据来调用，返回最后一条记录
          
        <10> exists():              queryset类型的数据来调用，如果QuerySet包含数据，就返回True，否则返回False
        　　　　　　　　　　　　　　     空的queryset类型数据也有布尔值True和False，但是一般不用它来判断数据库里面是不是有数据，如果有大量的数据，你用它来判断，那么就需要查询出所有的数据，效率太差了，用count或者exits
        　　　　　　　　　　　　　　　　 例：all_books = models.Book.objects.all().exists() #翻译成的sql是SELECT (1) AS `a` FROM `app01_book` LIMIT 1，就是通过limit 1，取一条来看看是不是有数据
        
        <11> values(*field):        用的比较多，queryset类型的数据来调用，返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
                                    model的实例化对象，而是一个可迭代的字典序列,只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。
                                    models.Book.objects.filter(age=18).values('id','age')
        <12> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
                     models.Book.objects.filter(age=18).values_list('name','age')
         
        <13> distinct():            values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复纪录--去重,返回queryset
        
        <14>     基于双下划线的模糊查询
                Book.objects.filter(price__in=[100,200,300]) #price值等于这三个里面的任意一个的对象
                Book.objects.filter(price__gt=100)  #大于，大于等于是price__gte=100，别写price>100，这种参数不支持
                Book.objects.filter(price__lt=100)
                Book.objects.filter(price__range=[100,200])  #sql的between and，大于等于100，小于等于200
                Book.objects.filter(title__contains="python")  #title值中包含python的
                Book.objects.filter(title__icontains="python") #不区分大小写
                Book.objects.filter(title__startswith="py") #以什么开头，istartswith  不区分大小写
                Book.objects.filter(pub_date__year=2012)

5.djiango外部文件py文件引入 --示例项目singletablehw\外部py文件操作django示例.py
示例
    # sep1. 配置django项目环境
    import os
    if __name__ == "__main__":#这条语句在manage.py 首句copy过来
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singletablehw.settings")
    # sep2 安装 运行环境
        import django
        django.setup()
    
    #  sep3 写自已需要在项目中使用的函数
        from app01 import models
        obj_list=[ ]
        for i in range(1,9):
            object=models.Book(
                title='葵花宝典第%s式'%i,
                price=20+i,
                pub_date='198%s-11-11'%i,
                publish= '出版社1' if i <5 else '出版社2',
            )
            obj_list.append(object)
    
        models.Book.objects.bulk_create(obj_list)
    

6.urls 别名和反向解释
  6.1 写别名 url(r'^index',views.index,name='别名XX')
  6.2 别名反向解释 ：
   from django.urls import reverse
   reverse('别名XX') --不加参数
   reverse('别名XX','参数') -- 带参数
   6.3 模板写法
   {% url '别名XX' %}  --不加参数
   {% url '别名XX' id %}  --带参数
   
'''

#五. ORM-- 多表操作
'''
https://www.cnblogs.com/clschao/articles/10439958.html
 mysql 三种表关系-- 一对一| 一对多| 多对多
 多表操作 -- 演示项目 --  manytable
 建立多关系表
    sep1:在models.py 创建 表和表关系--写class
    sep2: 配置mysql连接 --settings.py -->DATABASES = {..}
    sep3 . 配置mysql连接 --__init__.py 写入
        import  pymysql
        pymysql.install_as_MySQLdb()
    
    sep4: 创建表--- 用manage程序执行 makemigrateion --> migrate
        4.1 一对一关系表 创建 models.OneToOneField
         authorDetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)
            #ORM创建的authorDetail 属性 对应生成mysql表后 在表后插入authorDetail_id字段--含UNIQUE--唯一属性
    
        4.2 一对多关系表 创建 models.ForeignKey
            publishs=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
            #ORM创建的publishes 属性 对应生成mysql表后 在表后插入publish_id字段--不包含UNIQUE--唯一属性
        4.3 多对多关系表   models.ManyToManyField
            authors=models.ManyToManyField(to='Author',)
            #ORM创建的authors 属性 对应生成mysql表后 生成一张记录两表关系的新表 app01_book_authors
        具体打右边看mysql可视化窗口查看表的结构
    
    sep5. pycharm 配置mysql 可视化窗口 --方便调试
        右边Database菜单窗口 左上角 + 号->data source -->输入相关信息
        坑：连接mysql时没有设置时区报错[08001] Could not create connection to database server
            在url后拼接  ?useSSL=false&serverTimezone=UTC
                python时间对象时区的判断 https://www.cnblogs.com/clschao/articles/10757374.html
    
    sep6 在表中插入数据 --新方式 django提供的后台管理系统 admin.py
        数据插入已经学过的方式 cmd操作原生mysql命令| pycharm的可视化窗口操作|django外部引入py程序用pymysql批量创建| django提供的后台管理系统admin.py创建
         django提供的后台管理系统admin.py---django专门用来管理数据库的表
         使用方法
         6.1 配置urls --pycharm生成的项目已默认配置urlpatterns = [url(r'^admin/', admin.site.urls),]
         6.2 首先要配置一个超级用户账号密码--用manage.py 创建 --createsuperuser
            manage.py@manytable > createsuperuser ---按提示输入用户密码
                这里设用户名 ：wqlai  密码 :wqlai123  --会提示不能小于8位，不能全为数字
          6.3 进入后台管理系统 http://127.0.0.1:8080/admin
                这时只可看到用户管理的信息看不到表，还需在amdin.py注册表
          6.4 在admin.py 注册表
                from django.contrib import admin
                from app01 import models
                admin.site.register(models.Author)
                admin.site.register(models.AuthorDetail)
                admin.site.register(models.Publish)
                admin.site.register(models.Book)
        6.5 进入网址 点击操作增删改查---后台操作
            坑1 -- 增加一条数据 查显示 -Publish object 解决__str__方法显示当前object
    
    sep7 演示前台操作关系表的增删改查
        7.1 设置 urls--> url(r'^query/', views.query),
        7.2 写views逻辑 -> def query(request) ...--> 转看views
 




'''

#六. ORM-- 跨表查询
'''
六. ORM-- 跨表查询
from   app01 import models

# Create your views here.


def query(request):
    #多关系表--增删改查
    # 1.多表关系--增
    # 1.1 一对一表
    # 添加方式一：用类操作关系表 直接uthorDetail=new_ad, -- 两个表数据同时创建
    # new_ad=models.AuthorDetail.objects.create(
    #     birthday='1999-2-1',
    #     telephone='222',
    #     addr='views北京1'
    # )
    #
    # new_author=models.Author.objects.create(
    #     name='views作者1',
    #     age='21',
    #     authorDetail=new_ad,

    # # 添加方式二：用mysql字段操作 ---已有AuthorDetail的数据 再创建Author数据 --常用
    # obj =models.AuthorDetail.objects.filter(addr='views北京2').first()
    # new_author=models.Author.objects.create(
    # name='views作者2',
    # age='21',
    # authorDetail_id=obj.nid
    # )

    # 1.2 增 一对多关系表 --和一对一表方法一样
    # 添加方式一：用类操作关系表 直接将类的属性=一个object -- publishs=new_ad
    # obj=models.Publish.objects.get(nid=1)
    # models.Book.objects.create(
    #     title='views一对多书籍1',
    #     publishDate='2000-2-2',
    #     price='11',
    #     publishs=obj
    # )

    # # # 添加方式二：用mysql字段操作 ---表Book ->字段 publishs_id --常用
    # models.Book.objects.create(
    #     title='views一对多书籍2',
    #     publishDate='2002-2-2',
    #     price='22',
    #     publishs_id=2
    # )

    #1. 3.增-- 多对多关系表--Book表和Author表多对多关系  --object对象 使用 manytomany方法在Book表创建的属性 authors=models.ManyToManyField(to='Author',)
    # #方法一 通过类属性操作object -- 直接在*arg参数中放入外键值---常用
    # obj = models.Book.objects.get(nid=10) #对应MySQL已有数据’views一对多书籍2‘
    # obj.authors.add(*(1,2,3)) # obj对象 Author表中添加外键值为 1、2、3的三个作者

    # # 方法一 通过类属性操作object --在*arg参数中放入对象-- 较麻烦
    # author1= models.Author.objects.get(nid=1)
    # author2 = models.Author.objects.get(nid=2)
    # obj = models.Book.objects.get(nid=9) #对应MySQL已有数据’views一对多书籍1‘
    # obj.authors.add(*(author1,author2)) # obj对象 Author表中添加外键值为 1、2的三个作者

# 2.多表关系-删
#     2.1 一对一|一对多的删除都和单表删一样
#     2.1.1  删除  一对一中 在author类中创建onetoone方法，增时先建authordetail 再调用author一对一方法关联表，删除时删authordetail同时删除author，删除author不影响authordetail
#     models.AuthorDetail.objects.get(nid=7).delete()
    # models.Author.objects.get(nid=7).delete()
#     2.1.2 删除--一对多 Publish 是一| Book -有外键- 是多 --删除publish会同时删除book，反这不会
#     models.Publish.objects.get(nid=4).delete()
#     models.Book.objects.get(nid=12).delete()

#     2.2 多对多删除 -- Book （含manytomany方法)| Author 两表互为一对多关系，删除除用manytomany方法定义的类属性（本例为authors）
    #.2.2.1 多对多删除 --指定删除 remove
#     models.Book.objects.get(nid=10).authors.remove(2) # 单个删除mysql第三张表（关系表）中Author id=2的关系
#     models.Book.objects.get(nid=10).authors.remove(*[3,4])  # 多个删除mysql第三张表（关系表）中Author id=2的关系

    # .2.2.2 多对多删除 --全部关系删除(清空) clear
    # models.Book.objects.get(nid=9).authors.clear()
    # .2.2.3 多对多删除 --set命令-全部关系删除同时重新添加 等于先 clear 再add两个命令组合
    # models.Book.objects.get(nid=10).authors.set('1')  # 清空重新加1个-- 传参输入为字符串格式
    # models.Book.objects.get(nid=10).authors.set(['2','3','4']) # 清空重新加多个--将原来关系全删再加上2，3，4，注 参数前不用加星号

# 3.多表关系 --更新 --和单表操作一样--利用queryset 对象 update命令更新
#     3.1 一对一关系表-更新
#     models.Author.objects.filter(nid=8).update(
#         name='已更新作者1',
#         age=22,
#         # authorDetail= models.AuthorDetail.objects.get(nid=10) # 方法一：这个参数使用类属性 要给一个model对象
#         authorDetail_id = 9  # 方法二 这个参数使用mysql 字段 直接给值
#     )
#     3.2 一对多关系表--更新 和 一对一关系更新方法一样，小了关联字段的唯一限制
#     models.Book.objects.filter(pk=13).update(  # 注：内置pk关键字= 主键字段
#         title='一对多update1',
#         # publishs=models.Publish.objects.get(pk=2)#方法一：这个参数使用类属性 要给一个model对象
#         publishs_id=1,
#     )

# 4. 查 --ORM-- 跨表查询
6.1 基于对象的跨表查询 - --类似于 - -子表查询
#     正向查询和反向查询 - -正向 - -从含有关系属性的表查不含有关系属性的表 | 反向 - -从不含有关系属性的表去查

#     6.1.1 一对一
#         6.1.1.1 正向查询 示例作作者1的电话号码
    # author_obj=models.Author.objects.filter(name='作者1').first()
    # print(author_obj.authorDetail,type(author_obj.authorDetail)) # 返回副表的object--> 广州1 <class 'app01.models.AuthorDetail'>
    # print(author_obj.authorDetail.telephone) #返回副表object 下属性的值 -->1234
    # #         6.1.1.2 反向查询 示例 电话号码 查 作者
    # authordetail_obj = models.AuthorDetail.objects.filter(telephone='1234').first() #sep1-先选择副表对象
    # print(authordetail_obj.author,type(authordetail_obj.author)) #sep2--副表对象.主表类名小写--返回主表对象 -作者1 <class 'app01.models.Author'> 注 作用于model对象 对queryset没有这种方法
    # print(authordetail_obj.author.name) # sep3-获取主表对象的属性值 -->返回--作者1
    
                一对一 正向查询 Authorobj.authorDetail , 对象，关联属性名称    
        author------------------------------------------------------------->authorDetail
              <------------------------------------------------------------
                一对一 反向查询 authorDetailobj.author , 对象，小写类名    
    

#     6.1.2 一对多
#         6.1.2.1 正向查询 示例 查  书籍1的 出版社 和一对一相同
#     book_obj = models.Book.objects.get(title='书籍1')
#     print(book_obj.publishs,type(book_obj.publishs)) # 返回 一个model的对象-》 出版社1 <class 'app01.models.Publish'>
#     print(book_obj.publishs.name) #返回 对象的属性值 -》出版社1
    #         6.1.2.2 反向查询 示例 查  出版社1的 所有书籍
    # publish_obj = models.Publish.objects.filter(name='出版社1').first() #sep1 先选中一个publish对象
    # print(publish_obj.book_set,type(publish_obj.book_set)) # sep2 用内置的方法 主表名_set方法获得一个类 返回值： app01.Book.None <class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
    # print(publish_obj.book_set.all()) # sep2 用内置的方法 主表名小写_set 类的.all()方法获得一个queryset 的查询结果：<QuerySet [<Book: 书籍1>, <Book: 书籍7>, <Book: views一对多书籍1>, <Book: 一对多update1>]>
       
                一对多 正向查询 Bookobj.publishs , 对象，关联属性名称    
        book------------------------------------------------------------->publish
              <------------------------------------------------------------
                一对多 反向查询 Publish_obj.book__set.all() , 对象，小写类名__set (小写表名加双下划线set）   
    

#     6.1.3 多对多
#         6.1.3.1 正向查询 示例 查  书籍 nid=2 的 多作者
#     book_obj = models.Book.objects.get(nid=2) # sep1 获取主表book的一个对象
#     print(book_obj.authors,type(book_obj.authors)) # sep2 用主表的关联属性获取副表的类 结果：app01.Author.None <class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
    # print(book_obj.authors.all()) #sep3 获取 多值 -- queryset ，结果：<QuerySet [<Author: 作者2>, <Author: 作者3>]>


#         6.1.3.2 反向查询 示例 查  作者 nid=2 的 多籍 -- 方法同一对多反向 副表对象.主表名小写_set.all()
#     author_obj = models.Author.objects.get(nid=2)
#     print(author_obj.book_set,type(author_obj.book_set))# 返回 app01.Book.None <class 'django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager'>
#     print(author_obj.book_set.all()) # 返回：<QuerySet [<Book: 书籍2>, <Book: 书籍3>, <Book: 书籍5>, <Book: 书籍6>, <Book: 书籍7>]>

                多对多 正向查询 Bookobj.authors.all(), 对象，关联属性名称    
        book------------------------------------------------------------->author
              <------------------------------------------------------------
                多对多 反向查询 Author_obj.book__set.all() , 对象，小写类名__set (小写表名加双下划线set） 
#-===========================================================================================================

6.2  基于双下划线的跨表查询 ---- 连表 join --基于对象的方法需两条语句，这里只要一条语句
#     6.2.1  一对一表 基于双下划线的跨表查询：
    #     方式一：正向查询--主表在前写法-->主表queryset.value(副表__属性）
    # print(models.Author.objects.filter(name='作者1').values('authorDetail__telephone'))#用filter产生一个queryset再用.values 同样返回<QuerySet [{'authorDetail__telephone': '1234'}]>
    # 翻译mysql语句：SELECT `app01_authordetail`.`telephone` FROM `app01_author` INNER JOIN `app01_authordetail` ON (`app01_author`.`authorDetail_id` = `app01_authordetail`.`nid`) WHERE `app01_author`.`name` = '作者1' LIMIT 21; args=('作者1',)
#
# #     方式二：反向查询---副表在前写法-->副表 在 filter内进行连表，再.values 就有两表所有属性
# #     print(models.AuthorDetail.objects.filter(author__name='作者1').values('telephone'))
#
#     print(models.AuthorDetail.objects.filter(author__name='作者1').values())#返回副表全部值<QuerySet [{'nid': 2, 'birthday': datetime.date(2020, 7, 1), 'telephone': '1234', 'addr': '广州1'}]>
#
#     print(models.AuthorDetail.objects.filter(author__name='作者1').values('telephone','author__age'))# 连表后跨表 用 --表名小写__属性 查 返回：<QuerySet [{'telephone': '1234', 'author__age': 22}]>
#     #翻译mysql语句：SELECT `app01_authordetail`.`telephone` FROM `app01_authordetail` INNER JOIN `app01_author` ON (`app01_authordetail`.`nid` = `app01_author`.`authorDetail_id`) WHERE `app01_author`.`name` = '作者1' LIMIT 21; args=('作者1',)


#     6.2.2 一对多表 基于双下划线的跨表查询：
#     6.2.2.1 正向查询 示例-查书籍1的出版社
#     print(models.Book.objects.filter(title='书籍1').values('publishs__name'))# 返回<QuerySet [{'publishs__name': '出版社1'}]>

#     6.2.2.1 反向查询 示例-查出版社1 对应的 书
#     print(models.Publish.objects.filter(name='出版社1').values('book__title')) #返回<QuerySet [{'book__title': '书籍1'}, {'book__title': '书籍7'}, {'book__title': 'views一对多书籍1'}, {'book__title': '一对多update1'}]>

#     6.2.3 多对多表 基于双下划线的跨表查询：
#     6.2.3.1 正向查询 示例-作者1的 多本书
#     print(models.Author.objects.filter(name='作者1').values('book__title'))#结果：<QuerySet [{'book__title': '书籍1'}, {'book__title': '书籍3'}, {'book__title': '书籍7'}, {'book__title': '书籍8'}, {'book__title': 'views一对多书籍2'}]>

#    6.2.4 进阶查询 --三表连表查
#     示例 查 出版社1 出版的书 及作者
#     方式一  中间关系表写在前 --   book主表-publish副表 一对多 | book和author多对多关系
#     print(models.Book.objects.filter(publishs__name='出版社1').values('title','authors__name'))
    #mysql 语句 SELECT `app01_book`.`title`, `app01_author`.`name` FROM `app01_book` INNER JOIN `app01_publish` ON (`app01_book`.`publishs_id` = `app01_publish`.`nid`) LEFT OUTER JOIN `app01_book_authors` ON (`app01_book`.`nid` = `app01_book_authors`.`book_id`) LEFT OUTER JOIN `app01_author` ON (`app01_book_authors`.`author_id` = `app01_author`.`nid`) WHERE `app01_publish`.`name` = '出版社1' LIMIT 21; args=('出版社1',)
    #结果返回：<QuerySet [{'title': '书籍1', 'authors__name': '作者1'}, {'title': '书籍7', 'authors__name': '作者1'}, {'title': '书籍7', 'authors__name': '作者2'}, {'title': 'views一对多书籍1', 'authors__name': None}, {'title': '一对多update1', 'authors__name': None}]>

    # 方式二 有选择条件表publish写在前
    # print(models.Publish.objects.filter(name='出版社1').values('book__title','book__authors__name'))
    #mysql语句 ：SELECT `app01_book`.`title`, `app01_author`.`name` FROM `app01_publish` LEFT OUTER JOIN `app01_book` ON (`app01_publish`.`nid` = `app01_book`.`publishs_id`) LEFT OUTER JOIN `app01_book_authors` ON (`app01_book`.`nid` = `app01_book_authors`.`book_id`) LEFT OUTER JOIN `app01_author` ON (`app01_book_authors`.`author_id` = `app01_author`.`nid`) WHERE `app01_publish`.`name` = '出版社1' LIMIT 21; args=('出版社1',)
    # 方式三 author表写在前
    # print(models.Author.objects.filter(book__publishs__name='出版社1').values('name','book__title'))

    # 6.2.4进阶查询 - -四表连表查 --例查 电话为3开头的作者 的书名和出版社
    # print(models.AuthorDetail.objects.filter(telephone__startswith='3').values('author__book__title','author__book__publishs__name'))#<QuerySet [{'author__book__title': '书籍2', 'author__book__publishs__name': '出版社2'}, {'author__book__title': '书籍3', 'author__book__publishs__name': '出版社3'}]>


# 7.聚合 -- 查出数据同时做统计 Avg 平均| Max 最大| Min 最小| Sum 求和|Count 记数 。。。
    from django.db.models import Avg,Max,Min,Sum,Count

    ret = models.Book.objects.aggregate(Avg('price'),Max('price'),Sum('price')) # .aggregate分组聚合方法--># 结果返回一个字典 {'price__avg': 46.181818}
    ret = models.Book.objects.aggregate(a=Avg('price'), b=Max('price'), c=Sum('price'))#a\b\c 为字典的key -->{'a': 46.181818, 'b': Decimal('123.00'), 'c': Decimal('508.00')}
    print(ret)

# 8 mysql可视化工具navcat介绍
#     8.1 查询窗口 -- 输入mysql原生指令 -- 美化--生成排版后可读性强的指令
#     8.2 表的增删改 -- 可视化操作
#     8.3 数据库备份功能-- 将数据从一个库 全部复制到另一个库
#           原生写法：https: // www.cnblogs.com / clschao / articles / 10263425.html
#     8.4 数据导入|导出 --- 如excel等格式导入导出
#     8.5 建模 : sep1 建表的模块-->sep在表写外键建立连接表-->sep3 导出sql语句生成sql命令文件保存在一个路径->sep4 创建库如 在 右边菜单在选中新建的库右键菜单选--运行mysql文件-找到刚生成的文件运成--sep5 查看库可见已生成新表


# 9 分组查询
#     原生mysql语句--GROUP BY ：---SELECT avg(price) FROM app01_book GROUP BY publishs_id;
#     示例 查 每个出版社 的平均价格
#     from django.db.models import Avg,Max,Min,Sum,Count
    # ret1 = models.Book.objects.values('publishs_id').annotate(a=Avg('price')) #单条件分组
         # ret1 返回结果<QuerySet [{'publishs_id': 1, 'a': 58.25}, {'publishs_id': 2, 'a': 30.8}, {'publishs_id': 3, 'a': 60.5}]>
    # ret2=models.Book.objects.values('publishs_id','nid').annotate(a=Avg('price'))# 多条件分组取值
        #ret2=  返回结果<QuerySet [{'publishs_id': 1, 'a': 58.25}, .>
    # ret3=models.Publish.objects.values(a=Avg('book__price')) # 使用跨表查询
        # ret3 返回结果< QuerySet[{'a': 58.25}, {'a': 30.8}, {'a': 60.5}] >
    # ret4 =models.Publish.objects.annotate(a=Avg('book__price')).values('name','a') # 使用分组+跨表查询
        # ret4返回结果 < <QuerySet [{'name': '出版社1', 'a': 58.25}, {'name': '出版社2', 'a': 30.8}, {'name': '出版社3', 'a': 60.5}]> 注ret4 是用published的id分组其实和ret3一样没实际使用意义

    # print(ret4)

# #10 F查询和Q查询
#     # F查询主要用于单表查询 中 两个字段的比较输出
#     # 示例 在 Book类中加入两个字段good 点赞数| comment 评论数 ，查找点赞数大于评论数的 行object数据
#     from django.db.models import Avg, Max, Min, Sum, Count,F,Q
#
#     # ret = models.Book.objects.filter(good__gt=F('comment')) #返回：<QuerySet [<Book: 书籍1>]>
#     # ret = models.Book.objects.filter(good__gt=F('comment')-10) #F字段支持四则运算
#
#     # F 查询---查找good点赞字段，让点赞数全部加5
#     # ret = models.Book.objects.all().update(good=F('good')+5)
#     # 普通查询 - good 和comment同时大于10的行 --与关系 注：不支持或关系，Q查询支持或关系
#     # ret = models.Book.objects.filter(good__gt=10,comment__gt=10) #<QuerySet [<Book: 书籍6>]>
#
#     # Q查询 支持逻辑运算  支持运算符 | 管道符、& 与关系 、 ~ 取反 并且可以嵌套（不示例）
#     # Q查询 good 大于10 或 comment大于10的行
#     # ret = models.Book.objects.filter(Q(good__gt=10)|Q(comment__gt=10)) # 结果<QuerySet [<Book: 书籍1>, <Book: 书籍6>]>
#     # Q查询 good 小于10 并且 comment小于10的行
#     # ret = models.Book.objects.filter( ~Q(good__gt=10)& ~Q(comment__gt=10))
#     #Q查询 --嵌套 --注：Q查询中&运算符优先级高于| ，要按自已逻辑用Q（）包起来
#     ret = models.Book.objects.filter(Q(Q(good__gt=10)|Q(comment__gt=10))&Q(price__gt=50))#返回结果：<QuerySet [<Book: 书籍1>, <Book: 书籍6>]>

# 11 ORM 中使用原生mysql语句
#     # 方式一obj.raw（'mysql语句'）
#     ret =models.Publish.objects.raw('select * from app01_publish;') #返回一个对象集<RawQuerySet: select * from app01_publish;>  注：可用for循环出所有object
#     print(ret) #返回一个对象<RawQuerySet: select * from app01_publish;>
#     print(ret[0],type(ret[0])) # 结果：出版社1 <class 'app01.models.Publish'>
#     print(ret[0].name)# 结果：出版社1
    # 方式二 引用pymsql管道https://www.cnblogs.com/clschao/articles/10439958.html
    #注：在__init__.py 建立了pymsql的管道，通过下面方式引入，再获取mysql游标，执行指令
    # from django.db import connection, connections
    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
    # cursor.execute("""SELECT * from app01_publish where id = %s""", [1])
    # ret = cursor.fetchone()
    
    --展示在django中的mysql翻译  
     # ret = models.Book.objects.all().update(good=F('good')+5)
       # from django.db import connection
        print(connection.queries)
     
     
    

'''

# 七. ORM--事务和锁
'''https://www.cnblogs.com/clschao/articles/10463267.html
mysql 锁相关知识  https://www.cnblogs.com/clschao/articles/10065275.html
7.1 锁　　
7.1.1行级锁  select_for_update
select_for_update(nowait=False, skip_locked=False) #注意必须用在事务里面，至于如何开启事务，我们看下面的事务一节。
返回一个锁住行直到事务结束的查询集，如果数据库支持，它将生成一个 SELECT ... FOR UPDATE 语句。
entries = Entry.objects.select_for_update().filter(author=request.user)  #加互斥锁，由于mysql在查询时自动加的是共享锁，所以我们可以手动加上互斥锁。
create、update、delete操作时，mysql自动加行级互斥锁
目前，postgresql，oracle和mysql数据库后端支持select_for_update()。 但是，MySQL不支持nowait和skip_locked参数。使用不支持这些选项的数据库后端（如MySQL）将nowait=True或skip_locked=True转换为select_for_update()将导致抛出DatabaseError异常，这可以防止代码意外终止。

7.1.2 　表锁 --了解即可

7.2 事务 -- 使用场景 银行转账 两账号同时减钱和加钱，执行过程错误语句同时不生效
   7.2.1 mysql 开启事务  start transatction 开启事务——> commit 提交事务
   
   7.2.2 　　1 全局开启 --- 注：全局开启一般不常用
   DATABASES = {
    'default': {
        。。。
        "ATOMIC_REQUESTS": True, #全局开启事务，绑定的是http请求响应整个过程
        "AUTOCOMMIT":False, #全局取消自动提交，慎用
    }，
    7.2.3  2 局部开启的三种方法
    7.2.3.1 　用法1：给函数做装饰器来使用　
        from django.db import transaction
        @transaction.atomic
        def viewfunc(request): --含mysql语句的函数
         。。。
    7.2.3.2 　用法2：作为上下文管理器来使用，其实就是设置事务的保存点
    from django.db import transaction
    def viewfunc(request): --含mysql语句的函数
        # This code executes in autocommit mode (Django's default). -- 部分1：常规语句
        do_stuff() 
    
        with transaction.atomic():   #保存点 -- 部分2：事务捆绑语句
            # This code executes inside a transaction.
            do_more_stuff()
    
        do_other_stuff()----部分3：常规语句
            
    7.2.3.2 　用法3：还可以嵌套使用，函数的事务嵌套上下文管理器的事务，上下文管理器的事务嵌套上下文管理器的事务等。（转看博客）
'''

# 八 django -- Ajax --异步请求|局部刷新 --示例项目: ajaxtest
'''https://www.cnblogs.com/clschao/articles/10463267.html
两个特性：异步请求|局部刷新
    写法
        <script>
            $('#btn').click(function () {
                $.ajax({
                    url:'/login/', # 请求路径
                    type:'post', #请求方式
                    data:{       #发送数据
                        uname:$('#username').val(),
                        pwd:$('#password').val(),
                        {#post 请求需要csrf认证，在js中使用方法如下--类似爬虫的例子#}
                        csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
                    },
                    success:function (res) {    # 返回数据及处理方法
                        console.log(res,typeof res);
                        {# 本例中响应回来res的是一个josn格式字符串化的字典，通过反序列化拿到字典 #}
                        var res_str =JSON.parse(res);
                        {# Ajax 不能直接执行响应中的 redirect 命令，只能接收数据，通过数据处理识别响应结果自已用js的location命令重新申请页面#}
                        console.log(res_str,typeof res_str);
                        {#如果密码正确，跳转到index页面#}
                        if (res_str['code'] ===0 ){
                            location.href = res_str['msg']
                        }
                        {#如果用输入错误页面不刷新，在form后加一个span标签提示#}
                        else if (res_str['code'] ===3){
                            {#在jquery操作dom对象创建标签#}
                            var spanEle = document.createElement('span');
                            {#用jquery对象写入文本信息--注：$(dom对象）-->转变为jquery对象#}
                            $(spanEle).text(res_str['msg']);
                            {#用jquery对象把标签加在form标签后面#}
                            $('form').append(spanEle);
                        }
                    },
                })
                })
        </script>

        
# 演示 django Ajax 局部刷新|异步请求（请求后页面只有部分更新，不刷新页面）
https://www.cnblogs.com/clschao/articles/10463267.html
https://www.cnblogs.com/clschao/articles/10468335.html   --专题Ajax
https://www.cnblogs.com/clschao/articles/10409764.html  ---参考视图view 中的 JsonResponse
Ajax -- 通过 ajax 请求 响应一个数据(主要告诉它下一步干什么）给ajax 再 通过数据处理判断下一步动作 - 再操作dom对象实现需求
1. example for 没有用Ajax 新求后页面更新，前端页面的用户密码清空

2.example for 使用Ajax 新求后页面不刷新，前端页面的用户密码保留
    sep1 引用jQuery ---Ajax是基于jQuery 的 封闭后的方法 所以要先引用jQuery
        在项目根目录新建statics文件夹->copy jQuery -> 配置setting.py --> login.html 的script标签引入jQuery-> form 标签的提交按钮改成普通按钮，注（form|a| 提交都会刷新网页，为了不刷就不提交请求，改成点击事件交Ajax处理）--> 在script标签写Ajax语句：转向login.html

注1：script的一个坑：
    用js文件引入时，模板语言不生效如{% static 'login' %}，只能写在html文件，所以可以看到别人的网站在html还有script语句
注2：在前端查看方法 F12-->network -> all 全部请求| XHR就是筛选出ajax前求

注3 : django 十大组件 之 --解释器
        根据请求头 的 Content-Type: 声明的格式处理 数据 --实质是根据数据格式 切割 取值 放进字典
         Content-Type：三大数据格式 1 application/x-www-form-urlencoded| 2.multipart/form-data（将文件切割成片段发送）|3.application/json
        django 解释器只认识 浏览器 默认数据格式 Content-Type：-urlencoded和 multipart/form-data（用于上传文件）----不认识application/json,所以要自已处理，request.body(注：post方式时）直接取到b数，再转成字符串再反序列化
        ajax 默认 Content-Type：urlencode 但传数据常用application/json（django不认识）
补充：JSON 知识 --。。。


https://www.cnblogs.com/clschao/articles/10468335.html 
django 上传文件 普通form表单提交和 ajax 异步请求两种
    sep1 urls.py 配置响应路径：普通写法无特别 url(r'^upload/',views.upload,name='upload'),
    -> sep2 views写响应逻辑 相当于FTP，参看响应views函数  def upload(request):
        用 request.FILES方法获取文件对象 
        file_obj.chunks()方法按默认64k读写数据
        普通方法form表单提交和ajax 上传方法传到后端的数据和格式是一样的views函数没有不同之处，return同样内容，一个刷新页面一个不刷新只在后台处理
     -->sep3 写html文件 
            普通提交数据方法与ajax异步请求方法区别
            
            3.1普通方法 ： <form>标签内的<input type='submit'> 或button按钮提交，同时url请求刷新页面，默认form数据在请求头键值对传数据，要上传大文件数据在form标签中写入参数 enctype="multipart/form-data"，改在请求身 放数据
            
            3.2 ajax 方法 ： 不用form标签或不使用form标签的提交功能
                 通过 创建一个普通按钮绑定click事件，在响应事件方法中使用ajax,其中用到FormData()封闭要上传的数据（注：包括crsf认证），$.ajax({})写入上需要的必须的参数与数据。下面是html前端写法
                    <script>
                        $('#btn2').click(function () {
                             {#ajax传文件数据需要先用FormData()类的封闭数据#}
                            var formdata = new FormData();
                            formdata.append('uname',$('#username').val());
                            {#语句说明$('#file')[0].files[0]语句中$('#file')[0]是将jquery对象转为dom对象.files[0]是将.files返回的list取index=0的值，列表晨可存多个文件对象，本例只传一个，取值取第一个#}
                            formdata.append('head_pic',$('#file')[0].files[0]);
                            formdata.append('csrfmiddlewaretoken',$('[name="csrfmiddlewaretoken"]').val());
                
                            $.ajax({
                                url:'/upload/',
                                type:'post',
                                data:formdata,
                                processData: false, //不处理数据，传文件数据必须加上这两条processData: false，processData: false
                                contentType: false,// 不设置内容类型
                
                                success:function (res) {
                                    console.log(res)
                                }
                            })
                        })                
                      </script>






# 参看views文件：后端写法
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.views import View
#1. example for 没有用Ajax 新求后页面更新，前端页面的用户密码清空
class LoginView(View):

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):
        name=request.POST.get('uname')
        pwd =request.POST.get('pwd')
        if name =='eson' and pwd =='123':#{# Ajax 不能直接执行响应中的 redirect 命令，只能接收数据，通过数据处理识别响应结果自已用js的location命令重新申请页面#}
            # res = '{"code":0,"msg":"/index/"}' # 回复数据方式一 按json格式的字符串
            # return  redirect(request,'index.html')# ajax 不能直接执行redirect
            # return HttpResponse(res)

            # #回复json数据方式二 ： 用json模块
            # d1 ={"code":0,"msg":"/index/"}
            # import json
            # d1_json = json.dumps(d1)
            # return  HttpResponse(d1_json,content_type='application/json')# 参数 content_type 在响行头加了一个键值对，ajax收到后自动进行反序列化操作--  学名 ：ajax内部的 解释器

            # 回复json数据方式三：使用JsonRespone模块
            from django.http import JsonResponse # JsonResponse方法打包了方式二的方法
            d1 = {"code": 0, "msg": "/index/"}
            return JsonResponse(d1)
            # 补充： JsonResponse 回复list数据（非字典数据要加safe=False 参数）
            # d2=[11,22,33]
            # return JsonResponse(d1,safe=False )
        else:
            res = '{"code":3,"msg":"用户名或者密码错误！！！"}'
            return  HttpResponse(res)

def index(request):

    return render(request,'index.html')

#3. example for 用Ajax 上传文件
# # 3.1 普通方式上传--没有使用ajax
# def upload(request):
#     if request.method=='GET':
#
#         return render(request,'upload.html')
#     else:
#         print(request.POST) # request.POST拿到post请求的数据--只是文件名及用户名，不包含文件数据<QueryDict: {'csrfmiddlewaretoken': ['xHsHBVXqgOElUEUQoxp5qinok1NrAEnqtY9oqWdsadedCiZ7PICpa30qGhJLEPAE'], 'username': ['aa']}>
#         print(request.FILES) # 文件上传的保存在.FILES里 <MultiValueDict: {'head-pic': [<InMemoryUploadedFile: 1.png (image/png)>]}>
#
#         file_obj=request.FILES.get('head-pic') # 拿到文件数据，相当于文件句柄（ with open(XX,rb) as f)
#         file_name=request.FILES.get('head-pic').name
#         # 写入指定路径
#         import os
#         from ajaxtest.settings import BASE_DIR
#         path = os.path.join(BASE_DIR,'statics','img',file_name)
#         print(path)
#         with open(path,'wb') as f:
#             # for i in file_obj: # 方法一：按行读取---这种方法按行读取，但对于图片视频数据连续不适用，按固定大小读取方法.chunks(),它是一个生成器
#             #     f.write(i)
#         # 方法二 ： 按大小读取
#             for chunk in file_obj.chunks(): #chunk默认一次读64k
#                 f.write(chunk)
#
#         return HttpResponse('ok')


# 3.2 ajax方式上传--使用ajax  注：和普通方式写法一样不用改
def upload(request):
    if request.method=='GET':

        return render(request,'upload.html')
    else:
        #传过来的和上面数据一样
        print(request.POST) # request.POST拿到post请求的数据--只是文件名及用户名，不包含文件数据<QueryDict: {'uname': ['aa'], 'csrfmiddlewaretoken': ['May1r0tsHSOaO3XyU1Ekl5xXHqQVH5QkIrfIg1JuBho2wH2PlcRE5QaZ3GMfLg3y']}>
        print(request.FILES) # 文件上传的保存在.FILES里 <MultiValueDict: {'head_pic': [<InMemoryUploadedFile: 1.png (image/png)>]}>

        file_obj=request.FILES.get('head_pic') # 拿到文件数据，相当于文件句柄（ with open(XX,rb) as f)
        file_name=request.FILES.get('head_pic').name
        # 写入指定路径
        import os
        from ajaxtest.settings import BASE_DIR
        path = os.path.join(BASE_DIR,'statics','img',file_name)
        print(path)
        with open(path,'wb') as f:
            # for i in file_obj: # 方法一：按行读取---这种方法按行读取，但对于图片视频数据连续不适用，按固定大小读取方法.chunks(),它是一个生成器
            #     f.write(i)
        # 方法二 ： 按大小读取
            for chunk in file_obj.chunks(): #chunk默认一次读64k
                f.write(chunk)

        return HttpResponse('ok')

Ajax 发送 post 请求时要求csrf认证，请求-响应后接收到原码信息
    <input type="hidden" name="csrfmiddlewaretoken" value="fxTjVJApjmZXR9Uso9TKsDkkycbupjNgbOA0KKQrdLzPzNZJPk64coXmUs7Otu0u">
在 ajax 中 data：{ } 加入csrf信息  data：{'csrfmiddlewaretoken':$('[name="csrfmiddlewaretoken"]').val()}


'''

# 九 JsonRespone 响应方法 -- render | HttpResponse|redirect 方法后新学方法
''' 数据按json格式回复的方法，注非字典数据如list 需加 safe=false 
https://www.cnblogs.com/clschao/articles/10468335.html#part_4
注1： django 提供 JsonRespone回复json数据
注2 ： ajax 内置解释器 在 收到 content-type:'application/json'

发送数据请求：
浏览器或ajax 在content-type 没有指定时默认是 urlencoded 格式 如： ?a=1&b=2...
    对应django 后台views处理 如：request.POST.get('a') -->1 

django 没有json解释器，配合使用 djangorestframework 第三方库 解决json数据解释


'''

# 十 cookies 和 sessions  --示例 项目 cookiessession
'''Django基础八之cookie和session https://www.cnblogs.com/clschao/articles/10480206.html
 前言 http 协议两个特性 无连接 无状态  --- 不能持续对话 ，每次访问都要重新表明身份
    一个用户 -->  一个浏览器 --> 一个服务端
    
cookies: 设置和返回的都是明文的键值对，保存在客户端，不安全 注：数据传输经过网络，转为字符串
    过程 用户第一次请求： 带个空篮子过来--> 响应：在响应对象里加入cookies
        用户再次请求 带上cookies（F12 选中任一请求如有cookies则有cookies这个查看选项
        cookies写 ret.set_cookie('is_login',is_login)
        cookies读 is_login= request.COOKIES.get('k1')
        其它属性设置 看博客
session：为了解决安全问题，将cookies要返回的键值对保存在服务端，在cookies返回一个session的键值对,内容是一串加密的字符session_id，相当于一把密钥
    session方法使用方法：
        sep1 django连接数据库 。 注：通过makemigration -> migrate 命令django默认生在一张session的表(session_key|session_data|expire_date)，记录session，本例用sqlite3数据库为示例
        sep2 写session 与字典操作一样
            request.session['is_login'] = True

        sep3 读session
            is_login= request.session['is_login']
        其它属性设置 看博客

补充
CSRF Token相关装饰器在CBV只能加到dispatch方法上，或者加在视图类上然后name参数指定为dispatch方法。

　　　　　　备注：

　　　　　　　　csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。

　　　　　　　　csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。
    
'''

#十一 中间件 示例 项目 cookiessession
'''
二.django 的中间件
    django请求响应全过程 0.请求-->1.wsgi（socket)-->2.中间件（全局应用的类-方法）-->3. urls 路径分发系统 -->4.views 视图函数 -->models操作数据库和 html模板语言
    请求响应的全过程 ---学完中间件就全部学完
2.1 django 内置中间件
https://www.cnblogs.com/clschao/articles/10480419.html
       setting.py-->  MIDDLEWARE =【路径1，路径2.。。】
    中间件可以定义五个方法，分别是：（主要的是process_request和process_response）
            process_request(self,request)
            process_view(self, request, view_func, view_args, view_kwargs)
            process_template_response(self,request,response)
            process_exception(self, request, exception)
            process_response(self, request, response)
2.2 自定义中间件方法
    sep1 建一个自定义中间件文件夹 --注可在根目录也可在其它目录
        示例：在根目录建mymiddleware 文件件
    sep2 新建py文件-midtest.py  写中间件的类-方法
        from django.utils.deprecation import MiddlewareMixin
        class md1(MiddlewareMixin):
            def process_request(self,request):
                print('md1-请求来了')
                return None # 请求处理完默认回复None，标识已正确完成，交下一中间件顺序执行
            def process_response(self,request,response):
                print('md1-响应来了')
                return response # 响应要将 在本方法处理完的响应对象接力交给下一个中间件
 中间件应用：
    1.访问频率限制
        参看https://www.cnblogs.com/clschao/articles/10732867.html
    2.白名单


'''

# 十二 forms --三大功能  生成html页面标签|验证功能|保留用户输入的数据在返回页面上
'''https://www.cnblogs.com/clschao/articles/10486468.html
    form 用于用户验证 如输入用户名长度、大小写等规则
 form组件介绍
django 的form组件 --用于更方便写用户登陆输入验证、校验
https://www.cnblogs.com/clschao/articles/10486468.html
12.1 forms组件的三大功能
    功能1：生成html页面标签
    功能2：验证功能
        内置校验方法
        自定义校验：
                自定义校验器validators--正则校验、函数
                局部钩子、全局钩子
    功能3：保存用户输入的数据

12.2 写法
    12.2.1 views.py 写法
        首先导入模块 from django import forms
        sep1 定义类 --
                写入 类的属性-字段 如name|passowrd
                    定义属性 ---包括：功能1 的定义 标签及标签样式等| 功能2 定义校验规则，如name（。。。）

        sep2 写响应视图函数
            实例化类  form_obj = loginForm() # 实例化类
            使用类方法 ：
                    html生成标签 ：return render(request, 'register.html',{'form_obj':form_obj,}) # return实例化后的对象，在html中使用模板语言调用类对象的属性|方法
                    在views运行校验规则 form_obj.is_valid() # 运行规则 并返回状态True|False
                    在views调用类方法：print(form_obj.cleaned_data)|print(form_obj.errors).....

    12.2.2 html写法
         <div>
            <lable >{{ form_obj.name.label }}</lable>  #-- 属性值是一个字符串
                    {{ form_obj.name }}                 #-- 属性值是一个字典对象
            <span>{{ form_obj.name.help_text }}</span>
            <span style="color:red">{{ form_obj.name.errors.0 }}</span> # 调用类的errors方法返回的list，取index=0的值
        </div>
补充：
1 forms的两种方法forms.Form | forms.ModelForm
    froms的三大功能 1. 自动生成html标签 2.数据校验 3.数据库操作
    forms.Form | forms.ModelForm区别 ：forms.Form的类和models数据库的类分别操作，没有关联，ModelForm是model和forms的终极结合，在ModelForm类中就把models的类用class Meta 子类关联进来，ModelForm的类中有forms类的属性也有models类的属性。两者写法不同，类的方法也有不同。


1.1 forms.Form 的写法
sep1 复制 mbooks项目的内容过来，调试好
sep2 引用forms模块 ，用forms操作写类：增加字段属性-写标签 定校验规则
    from django import forms
    from   app01 import models
    class bookForm(forms.Form): 1.forms.Form类的写法与ModelForm不同 --ModelForm写class Meta 子类引用models
        title = forms.CharField(   # 1.1写字段及其属性
#         label='书名',
#         max_length=16,
#         # widget= forms.widgets.TextInput(attrs={'class':'form-control'})
#     )
       .....

        def clean_title(self): #在类中写局部钩子 -- 写入指定字段的特定的校验逻辑
          .......
        def clean(self): #在类中写全局钩子 -- 写入全局字段的特定的校验逻辑
            ............
        def __init__(self,*args,**kwargs): #批量操作函数 -- 写入批量操作逻辑
                ............
sep3 写views的响应函数
    def add_book(request):
    ......
        form_obj= bookForm(request.POST)# 2.forms.Form类的实例化对象写法与ModelForm不同
        ......
        if form_obj.is_valid()==True: # 3. 校验方法forms.Form|ModelForm两者相同
            newbook=models.Book.objects.create(**form_obj.cleaned_data) # 4.forms.Form|ModelForm操作数据方式均可通知models对象操作，ModelForm对象多了一个更简便的.save()方法
         ......
sep4 写html模板
    模板语言调用 {{ 对象.属性.元素}}
    {{ form_obj.price}} --- 生成含在forms类中写好样式对应input标签

1.2 forms.ModelForm 的写法
sep1 复制 mbooks项目的内容过来，调试好
sep2 引用forms模块 ，用forms操作写类：增加字段属性-写标签 定校验规则
    from django import forms
    from   app01 import models
    class bookForm(forms.ModelForm):# ModelForm类写法，1.单独字段用普通form写法先继承类forms.ModelForm
        title = forms.CharField(   #  1.ModelForm类内容：单独字段用普通Form写法，单独写可写在Meta字类前或后都可以，写后覆盖Meta类的相同字段内容
#         label='书名',
#         max_length=16,
#         # widget= forms.widgets.TextInput(attrs={'class':'form-control'})
#     )
       .....
          class Meta:  #2. ModelForm 固定定法，表单类中需要加model=UserInfo 指向那个models类，及类中的那些字段。注：Form与ModelForm区别：Form保存数据时用 models.Book.object.create()方法， ModelForme 用save(）方法，但要加Meta类。注 Meta类可以批量设置标签可看博客 class Meta下常用参数：model|fields|exclude|labels|help_texts|widgets|error_messages
        model = models.Book
        fields = ('__all__') # 引用数据库Book表的所有字段
        exclude = None   # 剔除数据库Book表的所有字段
        labels=None # 字典{'字段名':'标签字符串',...} 写法看博客
        help_texts=None# 字典{'字段名':'标签字符串',...}
        widgets=None # Meta类中widgets属性与ModelForm类的widgets方法重名，直接引用前面没有前缀用这个方法需要改名
        error_messages=None #字典 例：error_messages = {'name':{'required':"用户名不能为空",},。。}
        ......
        # 同样的，如果想做一些特殊的验证定制，那么和form一昂，也是那两个钩子（全局和局部），写法也是form那个的写法，直接在咱们的类里面写：

        def clean_title(self): # 3. 局部钩子：--与form一样 # 注：处理完要返回值，不能最后报错判断为空值
             value = self.cleaned_data.get("title")
             pass
            return value

        def clean(self): # 4.全局钩子--与form一样
            ......

        def __init__(self,*args,**kwargs): #批量操作函数 -- 写入批量操作逻辑
                ............

sep3 写views的响应函数
    def edit_book(request):
        edit_book_objs = models.Book.objects.get(id=book_id) # models数据库的对象，注：这里是models对象不是queryset
    ......
        form_obj = bookForm(request.POST,instance=edit_book_objs)# 2.实例化对象写法与ModelForm 有instance参数放入models数据库的对象
        ......
        if form_obj.is_valid()==True: # 3. 校验方法forms.Form|ModelForm两者相同
            form_obj.save()   # 4.forms.Form|ModelForm操作数据方式均可通知models对象操作，ModelForm对象多了一个更简便的.save()方法
         ......
sep4 写html模板 # 两者相同
    模板语言调用 {{ 对象.属性.元素}}
    {{ form_obj.price}} --- 生成含在forms类中写好样式对应input标签

坑1 编辑书籍需要显示原有数据：forms.Form 不能用 object(instance= XX)，form.ModelForm可以用，

'''
#十三  csrf 介绍 1.csrf安全机制补充|2.浏览器同源安全机制|跨站请求|跨源--简单请求、复杂请求

'''
1.csrf安全机制补充 -- html body中的crsf--csrfmiddlewaretoken--在ajax中data{}写入|  html headers中的cookies中的crsf--csrf-token-在ajax的headersv{}写入   
https://www.cnblogs.com/clschao/articles/10468335.html#part_3

2.浏览器同源安全机制|跨站请求|跨源--简单请求、复杂请求
https://www.cnblogs.com/clschao/articles/10745966.html





'''


