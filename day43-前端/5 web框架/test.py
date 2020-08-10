from jinja2 import Template
a={'a':1,'b':2}
data=str()
with open('./test1.html','r',encoding='utf-8') as f:
    data = f.read()
    usedata = a
    print('html', usedata)
    # data=data.replace('页面动态效果--此处每次访问更新为时间戳',a['name']+'我来了')
    tem = Template(data)
    print(type(tem))
    data = tem.render({'userinfo':usedata,})
    print(type(data))
    data = data.encode('utf-8')
    print(type(data))
with open ('test.html','wb') as f:
    f.write(data)