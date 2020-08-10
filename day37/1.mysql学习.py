'''
https://www.cnblogs.com/clschao/articles/10065275.html
注：本机mysql 登陆cmd命令  mysql -uroot -p123
了解数据库在程序中的作用
    数据库服务器-->提供数据服务的服务器
        数据库管理系统
            库-->文件夹
                表->文件
                    记录->一行数据
    关系型数据库
        mysql|sqllite|db2|oracle|Access|sql|
    非关系型数据库 key-value方式 快 {'a':[1,32,], } 用途举例 快递-> 快递单号 小视频 -> 视频ID
        mongodb|redis|memcache

    mysql
        版本 8.0 最新 5.7兼容不好
        分社区版和商业版

初始数据库
    配置
        必须在pycharm添加 my.ini （必须这个名）
            ->配置用课堂推荐配置（修改文件夹路夹-mysql 解压路径）
        添加环境变量
            在windows下-> 这台计算机->属性->高级系统设置->环境变量->新增
                C:\mysql-5.6.47-winx64\bin
        在cmd 安装mysql --以管理员身份运行cmd
           -> installd mysql    提示安装成功
            -> net start mysql  提示启动成功
基本操作



'''