'''
mysql> create user 'wqlai'@'%' identified by '123'; -->创建远程用户
mysql> create user 'wqlai'@'loctalhost' identified by '123';-->创建本机用户

mysql> GRANT ALL PRIVILEGES ON *.* TO 'wqlai'@'loctalhost' IDENTIFIED BY '123'; -->授权用户
mysql> show grants for 'wqlaid'@'loctalhost' -->查看权限

mysql> SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user; -->查看所有用户



'''