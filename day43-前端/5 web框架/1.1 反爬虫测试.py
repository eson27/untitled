'''
写一个爬虫测试京东'http://www.jd.com' 的反爬虫设置
    京东'http://www.jd.com'  ---没有反爬
       抽屉    https://dig.chouti.com/  --做了反爬

'''
# import requests
# res=requests.get('http://www.jd.com')
#
# # print(res.text)
# with open('jd.html','w',encoding='utf-8'  ) as f:
#     f.write(res.text)


# # 直接要求网页不是正常浏览器 返回警告网页---做了反爬
# import requests
# res=requests.get('https://dig.chouti.com')
#
# # print(res.text)
# with open('chouti.html','w',encoding='utf-8'  ) as f:
#     f.write(res.text)

# 做了反爬 --确解--伪装发送正常浏览器的网页申请的信息--这里放头部UA信息就可以
import requests
res=requests.get('https://dig.chouti.com',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})

# print(res.text)
with open('chouti-反反爬.html','w',encoding='utf-8'  ) as f:
    f.write(res.text)