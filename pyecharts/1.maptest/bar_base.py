from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    .render("bar_base.html")
)
set password for 'wqlai'@host= password('123');
set password for wqlai@'localhost'= password('123');
grant all privileges on *.* to wqlai@'localhost' identified by '123';
show grants for wqlai@localhost;