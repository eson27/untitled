'''
https://www.cnblogs.com/Eva-J/articles/9772614.html
PyMySQL 模块
    1.配置 pymysql.connect 参数
    2.获取游标 cursor
    3.增删改查
    #---实际操作遇到的一个问题
        sql注入问题 用来设计用户登陆时
            -- 注释后面
                or 1=1 --
    4.涉及改 conn.commit 提交
    5.关闭游标
    6.关闭库 conn.close()

mysql 库 | 表 备份
    事务 开启后过程中等于执行了行级锁
        锁 -
        mysql> begin; #开启事务
             select pwd from userinfo where id=1 for update; 上锁至update完成
                update pwd set pwd=456 where id=1;
                    commit ;提交事务，还钥匙

    备份 使用bin文件夹内 mysqldump.exe
        在cmd 命令行输入 -先退出mysql
            单库备分
            mysqldump -u root - p123 h127.0.0.1 day41 >C:\Users\wqlai\PycharmProjects\untitled\day37\backtest.sql
            mysqldump -u root -p -h127.0.0.1 day41 >C:\Users\wqlai\PycharmProjects\untitled\day37\backtest.sql
            多库备份 mysqldump -u root -p --databases day37 day38 day41 >C:\Users\wqlai\PycharmProjects\untitled\day37\backtestm.sql
    恢复
        mysql> create database day42;
            mysql> use day42;
                单库恢复 --如果use day42 在当前库中生成原库的表 ---修改库名可用这个方法
                    mysql> source C:\Users\wqlai\PycharmProjects\untitled\day37\backtest.sql  注意结尾不用加分号
                多库恢复--会在根目录生恢复库覆盖原库 *注意安全
                    mysql> source C:\Users\wqlai\PycharmProjects\untitled\day37\backtestm.sql




'''
#
# import pymysql
# #sep1-建立连接,常用前面几个参数,port可不用，默认3306
# conn=pymysql.connect(host='127.0.0.1', user='root', password="",database='day40', port=3306,)
#
# #print(conn)
#
# #sep2--获取mysql的游标
# cur=conn.cursor() # 元组方式
# #cur=conn.cursor(cursor=pymysql.cursors.DictCursor) # ret 返回字典格式，注：数据清晰，效率低
#
# #se3--进行execute(mysql操作命令)
# #--------example for execute 和 .fetchXXX
# # try:                                   #操作文件名出错先try下
# #     cur.execute('select * from dep')
# #     #cur.execute('select * from depssss')
# #     #cur.execute('select * from dep order by id')
# #     ret_one=cur.fetchone() #获取一个值
# #     ret_many =cur.fetchmany(3) #获取多个值
# #     ret_all =cur.fetchall()#获取全部值,注意游标是向下走的，执行完上面两条all余下是空集
# #     print(ret_one,ret_many,ret_all)
# #
# # except pymysql.err.ProgrammingError as e_info:
# #     print(e_info)
#
# # #--------exmple for scroll
# # cur.execute('select * from dep')
# #
# # #cur.execute('select * from depssss')
# # #cur.execute('select * from dep order by id')
# # ret_one=cur.fetchone() #获取一个值
# # ret_many =cur.fetchmany(3) #获取多个值
# # cur.scroll(0,'absolute')
# # ret_all =cur.fetchall()#获取全部值,注意游标是向下走的，执行完上面两条all余下是空集
# # print(ret_one,ret_many,ret_all)
#
#
# # # #--------exmple for 表头查询desc
# # cur.execute('select * from dep')
# # cur.execute ('desc dep')
# # ret = cur.fetchall()
# # ret_key=[ i[0] for i in ret]
# # print(ret_key)

# #--------exmple for 表增insert into | 删 delete from where|改 update set where|查fetchXXX
# import pymysql
# conn=pymysql.connect(host='127.0.0.1', user='root', password="",database='day40', port=3306,)
# cur=conn.cursor()
# try: #一般防止出错用try 出错就回滚
#     cur.execute('delete from dep where id=6') #删除
#     cur.execute('insert into dep values (6,"py写入2")') # 表写入字符双引号，存入库要conn.commit
#     cur.execute('update dep set name="左外连接pym" where id=4')
#     conn.commit() # 提交后才真正写入
# except Exception as e: #捕捉异常
#     print('try异常:',e)
#     conn.rollback()
# cur.execute('select * from dep')
# ret_all =cur.fetchall()
# print(ret_all)

'''
-----example for sql的注释问题 -安全绕过
在dos mysql下操作
mysql> create datas day41;
mysql> use day41;
create table userinfo(id int, name char(18), pwd char(32));
insert into userinfo values(1, 'a', 123);
'''
#---sql 注释问题
import pymysql
conn=pymysql.connect(host='127.0.0.1', user='root', password="",database='day41', port=3306,)
cur=conn.cursor()

user=input('username:')
pwd = input('pwd:')

#cur.execute('select * from userinfo where name="%s" or 1=1 -- and pwd="%s"'%(user,pwd))  # 用这种方式拼接user pwd-注释问题
#   username -> * " or 1=1 --   pwd->* 绕过密码 --符后面mysql语句被注释不执行
cur.execute('select * from userinfo where name="%s" and pwd="%s"'%(user,pwd))  # 用这种方式拼接user pwd-注释问题
print(cur.fetchone())
conn.close()
# #---sql 注释问题处理
# import pymysql
# conn=pymysql.connect(host='127.0.0.1', user='root', password="",database='day41', port=3306,)
# cur=conn.cursor()
#
# user=input('username:')
# pwd = input('pwd:')
# sql='select * from userinfo where name=%s and pwd=%s'
# cur.execute(sql,(user,pwd))  # 用这种方式拼接user pwd可以避免注释问题
# print(cur.fetchone())
# conn.close()