'''
https://www.cnblogs.com/Eva-J/articles/9676220.html
安装server端需要的命令
cmd下输命令
   -> net start mysql 开机自启动服务 -注配置了环境变量可以不用输绝对路径
    -> net stop mysql 关闭服务

启动client端 ->mysql.exe
在cmd下输命令
  启动
  -> mysql -u root -p -h192.168.1.1 加ip可以连网络服务器，本地可不加ip
  password 忽略回车5.6版本可以不输密码,5.7有初始密码（不好）有密码
  查看用户
    mysql-> select user(); 注结束加分号 root 是管理员账号 root@localhost

  创建新用户
    账号操作
        当前用户设密码：mysql->  set password =password('123")
        创建一个其他用户mysql->  create user 'guest' @ '192.168.1.% 'identified by '123'; 给一个网段访问，密码‘123’
        给一个用户授权
        grant 权限类型 on files.*    # *  to 'guest' @ '192.168.1.% '; ->表示对files文件夹下所有文件
            grant all 读写
            grant select 查
            grant insert 写

        flush privileges
    查看当前用户
        mysql> select user()
mysql 默认端口 3306，一般不改

数据库增删改查
    创建文件夹 create database 数据库名;

    查所有文件夹 show databases; 注结尾加分号
        切换到这个库下 use 数据库名;
            查文件 show tables; 先进入个库下
            创建文件 create table student(name char(12),age int);  -->表名(字段1，数据类型(长度)
            查看表结构
                desc student;
    操作数据
        插入数据 insert into student values('xiaomin',84);
        查询数据 select * from student;
        修改数据  update student set age=100 where name='xiaomin'; ->注 不加 where 就全改，高危操作
        删除数据 delete from student where name='xiaomin'; -> where后面是 条件










->

'''