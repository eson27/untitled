'''
说明文档
https://pyecharts.org/#/zh-cn/intro

'''
# #----------1.首先开始来绘制你的第一个图表
# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()

# #----------2.pyecharts 所有方法均支持链式调用
# from pyecharts.charts import Bar
#
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# bar.render()

# #----------3.使用 options 配置项，在 pyecharts 中，一切皆 Options。
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
# # V1 版本开始支持链式调用
# # 你所看到的格式其实是 `black` 格式化以后的效果
# # 可以执行 `pip install black` 下载使用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render()

# #----------4.渲染成图片文件，这部分内容请参考 进阶话题-渲染图片
# from pyecharts.charts import Bar
# from pyecharts.render import make_snapshot
#
# # 使用 snapshot-selenium 渲染图片
# from snapshot_selenium import snapshot
#
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# make_snapshot(snapshot, bar.render(), "bar.png")

# #----------5.使用主题
# #pyecharts 提供了 10+ 种内置主题，开发者也可以定制自己喜欢的主题，进阶话题-定制主题 有相关介绍。
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # 内置主题类型可查看 pyecharts.globals.ThemeType
# from pyecharts.globals import ThemeType
# x_list=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# y_dict={"商家A":[5, 20, 36, 10, 75, 90],"商家B": [15, 6, 45, 20, 35, 66]}
#
# bar = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.HALLOWEEN))
#     .add_xaxis(x_list)
#     .add_yaxis("商家A", y_dict["商家A"])
#     .add_yaxis("商家B", y_dict["商家B"])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# )
# bar.render()
import asyncio
async def main():
    await asyncio.sleep(1)
    print('hello')


asyncio.run(main())