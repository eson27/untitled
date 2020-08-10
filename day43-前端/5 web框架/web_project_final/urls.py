'''
web框架 --包括服务层函数  和 应用层函数
1.manage --主程序 完成服务器操作 --放服务层函数
2. views ---  放应用层函数 --用户自已写业务逻辑
3.urls --  存放 请求路径 对应的函数
    下次要使用时 1 不用动 配下2views的逻辑 和 3 的 对应关系 就可以了


'''

import views
# req = {'/':'10起飞版webpage.html',
#        '/04test.css':'./04test.css',
#        '/04test.js':'./04test.js',
#        '/1.jpg':'./1.jpg',
#        '/04web.ico':'./04web.ico',
#
#        }
urlpatterns  = {'/':views.html,
                '/04test.css':views.css,
                '/04test.js':views.js,
                '/1.jpg':views.jpg,
                '/04web.ico':views.icon}