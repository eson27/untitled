#已有表 database='webtest1' 表table userinfo 表头 id|name|age 往表insert 数据
import pymysql

conn=pymysql.connect(host='127.0.0.1', user='root', password="123",database='webtest1', port=3306,charset='utf8')#sep1 建立库连接

# cur=conn.cursor() # 元组方式
# #cur=conn.cursor(cursor=pymysql.cursors.DictCursor) # ret 返回字典格式，注：数据清晰，效率低
cursor =conn.cursor(cursor=pymysql.cursors.DictCursor) # sep2 获取游标

sql= 'insert into userinfo(name,age) value ("小b",29);' # sep3 插入数据 --写sql语句   注：id 外键为 auto_increment 是自动添加

cursor.execute(sql) #sep4 执行语句
conn.commit() #sep5 提交数据
cursor.close() #sep6 关闭游标
conn.close() #sep7 关闭数据库