from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


c = (
    Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
        .render("map_base.html")
)
# a= [list(z) for z in zip(Faker.provinces, Faker.values())]
# print(a)
create user 'wqlai'@'%' identified by '123';
show grants for 'wqlaid'@'%'


GRANT ALL PRIVILEGES ON *.* TO 'wqlai'@'%' IDENTIFIED BY '123';


