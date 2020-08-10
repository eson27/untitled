'''
mysql 支持很多种存储引擎
1.Innodb 存储引擎
    数据和索引存储在一起 2个文件->数据索引|表结构-->数据持久化
        支持事务  为了保证数据的完整性，将多个操作变成原子性操作
        支持行级锁 ： 修改小量行时，防止多个用户同时操作数据
            表级锁 ：批量修改多行时
        支持外键 ：约束两表中的关联字段不能随意 添加|删除

2.Myisam 存储引擎
    数据和索引 不存储在一起  3个文件->数据|索引|表结构-->数据持久化

3.Memory 存储引擎
    数据存储在内存中 1个文件->表结构-->数据断电消失

查看当前使用引擎相关信息
->show variables like '%engine%'; # 基本都是innodb

创建库
-> create database day38;  创建库
    --> use day38 ;      进入|切换到指定库
     —> select database(); 查看当前所在库
创建文件
-> create table student(id int,name char(18)); （字段名 类型[(宽度).。。]约束条件
->show create table student;  >查看表创建时的信息，注最后行
            ENGINE=InnoDB DEFAULT CHARSET=latin1 | -》CHARSET=latin1 要改成utf-8 按方法，在安装目录更换my.int


插入行
    mysql> insert into t1 values (2,'大臣n'),(3,'eva');  一次写入多条数据
    mysql> insert into t1 (name) values ('eva'); 单独输入一个列的数据
    mysql> insert into t1 (id) values (5); 单独输入一个列的数据
查看表的数据
     ->select * from t1;
查看表的结构
    ->desc t1; #方法一：只显示字段
    ->show create table t1;#方法二：显示表的所有信息

mysql数据类型
    1.数字
        整数-> 一般不约束长度,最大10位第一位4**
        create table t1(id int,age tinyint unsigned); 默认是有符号的 ，如果需要定义无符号的用unsigned声明
        小数 -> 约束长度如(5.2) 总长，小数长
        create table t2(f1 float(5,2),f2 float,f3 double(5,2),f4 double);
            insert into t1 values (5.233335);

    2.字符串
        char（18）  0-255 默认 1 定长 不够后面补空格 效率高节省时间
        varchar（18）  0-65535 默认 1  变长  节省空间 效率低
        其它不常用，大文件可选
    3.时间
        date 20200606
        time 121958
        datetime 20200606121958
        year 不常用 max 2155年
        timestamp 不常用 max 2038年
        create table t5(dt datetime,d date,t time,y year,ts timestamp );
            insert into t5 values(now(),now(),now(),now(),now());#插入当前时间
            update t5 set dt=('2017-7-8 12:30:12'); 更改时间可以用习惯样式
             insert into t5 (y) values(2019); 注操作单个或多个key，不输时间戳值默认为当前值
             select * from t5;
        create table t6 (id int,dt datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP); 设datetime 和时间戳一样
             ->NOT NULL  不为空
             ->DEFAULT CURRENT_TIMESTAMP 默认当前时间
             ->ON UPDATE CURRENT_TIMESTAMP 操作时默认自动真写当前时间


    4.enum|set
        enum 单选

            create

        set 多选

表的完整性约束
    约束某一字段不能为空
        not null
    约束某一字段无符号
        只和数字类型有关 int unsigned

    约束某一字段的默认值
       -> default 'male'

    约束某一字段不能重复
      --> unique(ip,port)  值不能重复但null可重复
            联合唯一
     第一个被设置为非空+不能重复的键 自动定义这主键 PRI -> primary key 一张表只有一个主键，但可设联合主键
        手动设置 id primary key
    自增  一般用在设置ID的约束
        auto increament
            对数字有效
                自带非空约束
                    必须在 unique后+auto_increament
                        常写成 id int primary auto_increament;
                            创建表时可加 auto increament=3约束从3开始
    主键
        一张表只有一个主键
        如果不指定 默认 第一个被设置为非空+不能重复

    外键
        班级表
            create table  class(cid int primary key auto_increment,cname char(12) not null);
                insert into class values (1,'py21') ,(2,'py22');  ->被关联后不能删除delete
        学生表
            create table student( id int primary key auto_increment,name char(12) not null,class_id int);
                foreign key (class_id) references class(cid);    先建班级表才能关联，cid必须唯一unique
                insert into student values(1,'小明',2),(2,'小q',2),(3,'小e',1);
        级联更新cascade ->两表联动，一般只用级联更新 update cascade 不用删除
修改表结构
    alter
    项目前建表定好，后期一般不常用修改

删除表
    drop table t1,t2;

多表结构的创建和分析
    多对1 多个学生是1个班级 forergn key
        学生表 对应 班级表 | 书籍表 对应 作者表 | 书籍 出版社 | 商品 订单

    多对多
        多个学生 参加 多个班级 -> 学生表 foreign key  班级表foreign key
            ->必须有第三张表 记录 学生ID unique 班ID unique 两个ID为外键

    一对一
        客户表 unique - 学生表 foreign key

数据的操作
    增
    删
        delete from t1  where id=3;删除,注自增偏移量没清空
        truncate table t1; 清空表

    改
        update t1 set id=101 , hobby ='上课,考试' where id=1;

    查
        (navicat 第三方可视化工具，只能看)

    表查询 select 字段 from table  - where | group by| having|order by
                create table t1(
                    id int primary key auto_increment,
                    username char(12) not null,
                    sex enum('male','female') default 'male',
                    hobby set('上课','写作业','考试') not null
                 );
                    insert into t1 values(1,'小a','male','上课,写作业',18),
                                         (2,'小b','male','上课,写作业,考试',18),
                                         (3,'小c','female','上课',22),
                                         (4,'小d','female','写作业,考试',22),
                                          (5,'小e','male','上课,写作业,考试',22),
                                         (6,'小f','female','上课,写作业',28),
                                         (7,'小g','female','考试',22);

                create table t2(id int,name char(12)); # 从t1母表得到一张子表
                    insert into t2 (id,name) select id,username from t1;
            select * from t1; 查所有
            select id,username from t1; 查指定列
            select id newid,username newname from t1; 查出来的显示列重命名
            select distinct sex, hobby from t1; 去重复

            select 使用 四则运算 + - * / |
                concat 拼接
                   concat_ws('/','a','a')
                 使用判断 相当于if
                    case
                        when XXX then XXX
                        when XXX then XXX
                        else
                        end

                where筛选
                    比较运算符 > < >= <= !=
                    比较运算 between  and | in(数组）->等于数组内的值
                    模糊匹配
                        like  'XX%" ,%为通配符 %匹配任意长度
                            select * from t1 where id like 'XX_" ,_为通配符 一个_仅匹配一个字符

                        regexp 正则匹配
                            regexp ('正则表达式‘)
                    逻辑运算 not|and | or
                        Null 判断 用 is null | is not null

                group by 分组 总与聚合一起用
                    count聚合 ---统计
                    max
                    min
                    sum
                    avg
                    select * from t1 group by hobby; 分组 结果只是显示这组第一个值
                    select hobby ,count(id) from t1 group by hobby; 分组聚合
                        ->注:统计的值只与分组字段对应，不与其它对应（如查年纪分组最小年纪的name，永远只显示年纪分组第一个人）
                        有个group concat 只能显示值不能取出值，对编程用处不大
                         use day39
                            select hobby ,group_concat(username) from t1 group by hobby;

                having 过滤  分组专用语句，总与分组聚合一起用 跟在语句后，注这个语句不能用于where后
                    select hobby ,avg(age) from t1 group by hobby;  按hobby 分组各组平均年龄
                        select hobby ,avg(age) from t1 group by hobby having avg(age)<22; 年龄小于22的分组

                order by 字段 -升序| order by 字段 desc  降序    ->字段可以多个，每个字段设升序与降序
                    select * from t1 order  by age desc,id ;  年龄降 id 升
                    select * from t1 order  by age desc,id desc;年龄降 id 降

                limit m,n  m开始数默认0，n相当于offset的数取数数量 常与order 排序 组合用
                    select * from t1 order  by age desc,id desc limit 1;最年最大的第一个
                        select * from t1 order  by age desc,id desc limit 3;最年最大的前3个

             拓展
                   where 不能使用 select username as name 的 重命名，其它可以
                                      ;
            多表查询
                多表查询
                    create database day40;
                    use day40;
                    create table dep(id int ,name char(20));
                        insert into dep values(1,'销售'),
                                         (2,'工程'),
                                         (3,'物业')
                                         (4,'左外连接')
                                         ;

                    create table staff(id int primary key auto_increment,name char(20),age int,dep_id int,foreign key (dep_id) references dep(id) );
                        insert into staff values(1,'小a',18,3),
                                         (2,'小b',18,1),
                                         (3,'小c',22,1),
                                         (4,'小d',22,2),
                                          (5,'小e',22,3),
                                         (6,'小f',28,1),
                                         (7,'小g',22,2);
                    所谓连表：连表查比子查询效率高，优选连表查
                        方式1.select  * from 表1，表2 where 条件
                             select * from dep,staff;连表 是用笛卡尔积组合成一张大表
                            select * from dep,staff where dep.id = dep_id;要得出想要的唯一连接用where 加条件筛选得出
                        方式2  内连接 select * from 表1 inner join 表2 on 条件 -> 常用方式2 注 两表不合条件筛选掉 后可再加where条件
                            select * from dep inner join staff on dep.id = staff.dep_id;
                                select * from dep as t1 inner join staff as t2 on t1.id = t2.dep_id; 支持重命名（即先join后重命名)
                                    select * from dep as t1 inner join staff as t2 on t1.id = t2.dep_id where age>20 and t1.name='工程'; 多条件


                        方式3 外连接
                            左外连接 --左表没有匹配到的项也会出现在现中
                                ----->insert into staff values(8,'左外连接',18,11);  注：这条不能生效，因dep没有11
                                insert into dep values(4,'左外连接');
                                select * from dep as t1 left join staff as t2 on t1.id = t2.dep_id;
                                    select t1.name,count(t2.id) as c from dep as t1 left join staff as t2 on t1.id = t2.dep_id group by t1.name order by c; 统计零值部门,null统计为0
                            右外连接 select XX from XX right join XX on


                子查询 -- 主要 用in | > < ...!=   注 子查询结果只能有一列 |inner join（子查询出来的表)

                    查平均年龄 >20 的部门
                    select name from dep where id in ( select dep_id from staff group by dep_id having avg(age)>20);
                    查 ‘工程’ 部门 人名
                    select name from staff where dep_id =( select id from dep where  name like '%工%'); # 只有一列的一个结果可用算符

                    inner join













'''