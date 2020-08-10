
# class Payment:
#     def pay(self,name):
#         raise NotImplementedError('请在子类中使用同名pay')

# class Apple:
#     def __init__(self,name):
#
#         self.name=name
#     def fuqian(self,money):
#         dic={'name':self.name,'number':money}
#         print('%s 通过苹果支 %s 钱成功 '%(self.name,money))

# #
# # def pay(name,price,kind):
# #     if kind=='wechat'
# #         obj=WeChat(name)
# #     elif kind == 'alipay':
# #         obj=alipay(name)
# #      obj.pay(price)
# #     pass
#
# # pay('alex',400,'wechat')
# # pay('alex',400,'Apple')
#
# obj=Apple('alex')
# obj.fuqian(200)
#


# #print(obj.__dic__)
# import re
#
# st = 'www.baidu.com www.taobao.com'
# result = re.findall(r'www\.(\w*)\.(com)', st)
# print(result)

import time
c=time.time()
a=time.localtime()

b=time.strftime('%Y-%m-%d %H:%M:%S')
print(type(b))