'''
1.运行makepy.py生成的00020905-0000-0000-C000-000000000046x0x8x7.py记录了与win操作的py封装
    constants->对应win某一方法的 枚举 数据类型是int
    class XX ->对应获得win句柄后可操作的命令
        def 函数 -> 对应该命令下的自有方法，使用时xxx.xxx()
            _prop_map_get_ = {"XXX:xxxx...}-> 对应该命令下的引用的类-class, 使用时xxx.xxx

'''




#1.To use a COM object from Python
#C:\Program Files (x86)\Python38-32\Lib\site-packages
#Generating to C:\Users\wqlai\AppData\Local\Temp\gen_py\3.8\00020905-0000-0000-C000-000000000046x0x8x7.py
#https://docs.microsoft.com/zh-cn/office/vba/word/   --微软官方
#Word 2010 开发人员参考 --word帮助
# import win32com.client
# o = win32com.client.Dispatch("Object.Name")
# o.Method()
# o.property = "New Value"
# print (o.property)

# #----exmple1--
# import win32com.client
# # o = win32com.client.Dispatch("word.Application")
# o = win32com.client.gencache.EnsureDispatch("excel.Application")
# o.Visible = 1
# o.Workbooks.Add() # for office 97 – 95 a bit different!
# o.Cells(1,1).Value = "Hello"
#
# print(repr(o))



#------example2--更换页眉页脚-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
#
# # w=win32com.client.gencache.EnsureDispatch('Word.Application')
# w=gencache.EnsureDispatch('Word.Application')
# w.Visible=1 # 过程可见
# # print(w.WindowState)
# # print(type(w)) #<class 'win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x5._Application'>
# # w.WindowState = win32com.client.constants.wdWindowStateMinimize
# # doc = w.Documents.Add() #新建文档|Documents是一个类|Add()是一个函数 |在00020905-0000-0000-C000-000000000046x0x8x5
# doc=w.Documents.Open('1122.docx') # 打开文档
#
# a = doc.Sections(1)
# # a.Headers(win32com.client.constants.wdHeaderFooterPrimary).Range.Text = "Header text" # 新加页眉
# # a.Footers(win32com.client.constants.wdHeaderFooterPrimary).Range.Text =  "Footer text" # 新加页脚-文字
# # a.Footers(win32com.client.constants.wdHeaderFooterPrimary).PageNumbers.Add(PageNumberAlignment=win32com.client.constants.wdAlignPageNumberCenter)    # 新加页脚-页码|默认Left
# # a.Footers(win32com.client.constants.wdHeaderFooterPrimary).PageNumbers.Add()    # 新加页脚-页码|默认Left
# # doc.SaveAs2(FileName='2211.docx') #以兼容模式另存
#
# # a.Headers(constants.wdHeaderFooterPrimary).Range.Text="更改页眉1" # 页眉更新


# #------example3--查找替换-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
# from os.path import abspath, dirname
#
# current_path = abspath(dirname(__file__))
# w=gencache.EnsureDispatch('Word.Application')
# # doc=w.Documents.Add() # 新建文档
# doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个Document 对象
# b=doc.Range(Start=3,End=10) # 1.指定范围 --替换
# b.Text="abc"
# myrange=doc.Range() # Range-函数| ()默认全选 （Start=int ,End=int ）可选
# myrange.Find.Execute(FindText='abc', ReplaceWith='AAA',)


# #------example4--在最后插入分页符|分行-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
# from os.path import abspath, dirname
#
# current_path = abspath(dirname(__file__))
# w=gencache.EnsureDispatch('Word.Application')
# current_path = abspath(dirname(__file__))
#
# w=gencache.EnsureDispatch('Word.Application')
# # doc=w.Documents.Add() # 新建文档
# doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个Document 对象
#
# doc.Select() #Document->Select|Document类下的一个函数
# w.Selection.EndOf() #Selection是与Document同级的类
# w.Selection.InsertBreak()#默认插入分页符.可选其它符号(Type=XX)
# w.Selection.InsertBreak()


# #------example5--在指定位置插入分页符|分行-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
# from os.path import abspath, dirname
#
# current_path = abspath(dirname(__file__))
# w=gencache.EnsureDispatch('Word.Application')
# current_path = abspath(dirname(__file__))
#
# w=gencache.EnsureDispatch('Word.Application')
# # doc=w.Documents.Add() # 新建文档
# doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个代表Document 对象
#
# myrange=doc.Range() # Range-函数| ()默认全选 （Start=int ,End=int ）可选
# myrange.Find.Execute(FindText='图片在此新加页插入')#find后myrange更新,并返回Ture|Flase

# myrange.Select()
# w.Selection.EndOf()#Selection是直属Dispatch的类
# w.Selection.InsertNewPage()#在指定位置后面插入新页
# w.Selection.Text='在指定位置新建了一页' #在新增页上写字
# # s=doc.Sections.Count #返回 int 1--sectionx暂无法理解及应用，Selection貌似可以替代
# w.Selection.InsertBreak()
# w.Selection.InsertAfter(Text='加在EndOf最后') #Selection是与Document同级的类

# w.Selection.Delete(Count=-4)



# doc.SaveAs2(FileName=(current_path+r'/4433.docx'))
# doc=w.Documents("3344.docx") # 选中指定文档
# doc.Close() #关闭文档

# #------example6--全选|Words计算-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
# from os.path import abspath, dirname
#
# current_path = abspath(dirname(__file__))
# w=gencache.EnsureDispatch('Word.Application')
# current_path = abspath(dirname(__file__))
#
# w=gencache.EnsureDispatch('Word.Application')
# # doc=w.Documents.Add() # 新建文档
# doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个代表Document 对象
#
# myrange=doc.Range() # Range-函数| ()默认全选 （Start=int ,End=int ）可选
# # t=myrange.Find.Execute(FindText='^m')#find后myrange更新,并返回Ture|Flase
# # dd=doc.Sections(1).Footers(constants.wdHeaderFooterPrimary).PageNumbers(1) #<class 'win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x5.PageNumber'>| 此句中PageNumbers(1)返回PageNumber对象，参数只能是1，每页页码只有一个
#
# myrange.WholeStory()#全选包括特殊字符|不包括页眉页脚
# # myrange.Select()
# # h=w.Selection.Words.Count # selection.words 计数包括-特殊符号|对象|中文（词）|数字英文按空格分开。。
# h=myrange.Words.Count# Range.words
# print(h,type(h))

# #------example7--建一个文件名：index的字典-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
# from os.path import abspath, dirname
#
# current_path = abspath(dirname(__file__))
# w=gencache.EnsureDispatch('Word.Application')
# current_path = abspath(dirname(__file__))
#
# w=gencache.EnsureDispatch('Word.Application')
# # doc=w.Documents.Add() # 新建文档
# # doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个代表Document 对象
#
# # n=doc.__call__()
#
# # n=w.Documents(1).__call__()
# d_name='3344.docx'
# ds_dic={}
# w.Documents.Open(d_name)
# n=w.Documents.__iter__()
# ds_index=0
# for i in n:
#     ds_index+=1
#     # print(i,w.Documents(i).__call__())
#     ds_dic[i.__call__()] = ds_index
#     print(ds_dic)
# d_index=ds_dic[d_name]
# doc=w.Documents(d_index)
# print(doc.__call__())


# # ------example8--在指定位置插入图片-
# import win32com.client
# import win32com.client.gencache
# from win32com.client import constants,gencache
# import os
# from PIL import Image
#
#
# p_list=[]
#
# current_path = os.path.abspath(os.path.dirname(__file__))
# p_dir = current_path+'\\'+'win32com_BMPs'
# # print(p_dir)
# for i in os.listdir(p_dir):
#     p_list.append(p_dir+'\\'+i)
# p_list.sort()
# # print(p_list)
#
# w=gencache.EnsureDispatch('Word.Application')
# doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个代表Document 对象
#
# myrange=doc.Range() # Range-函数| ()默认全选 （Start=int ,End=int ）可选
# myrange.Find.Execute(FindText='图片在此新加页插入')#find后myrange更新,并返回Ture|Flase
# myrange.EndOf()
# myrange.InsertBreak()  # 在指定位置后面插入新页
# myrange.EndOf()
# myrange.Select()
#
#
# # myrange.Select()
# # w.Selection.EndOf()
#
# # w.Selection.InsertNewPage()
# #
# # #----图片尺寸大小获取|判断用A3|A4
# # p_s = Image.open(p_list[0])
# # p_w=p_s.size[0] #size结果单位是px A3=1552*1060 - 像素 对应 297mm×420mm
# # p_h=p_s.size[1] #A4=1190*776 - 像素 对应 210mm×297mm
# # p_dpi = p_s.info['dpi'] # info结果单位是px/inchi 1英寸=2.54cm
# # p_ws=p_w/p_dpi[0]*25.4 #单位mm
# # p_hs=p_h/p_dpi[1]*25.4
# # p_s.close()
#
# # print(p_ws,p_hs)
# # s=w.Selection.InlineShapes.AddPicture(FileName=p_list[0])
# # # w.Selection.InsertAfter(Text='adddd')
# # w.Selection.InsertBreak(Type=6)
# # s=w.Selection.InlineShapes.AddPicture(FileName=p_list[1])
# # s=w.Selection.InlineShapes.AddPicture(FileName=p_list[1])
# # w.Selection.InsertNewPage()
#
#
# psize_a34={0:7,1:6} #PaperSize 枚举 wdPaperA4=7|wdPaperA3=6
#
# for i in p_list:
#     # ----图片尺寸大小获取|判断用A3|A4-假设viso图按A3|A4别存为BMP图纸尺寸=像素px/分辨率dpi
#     p_s = Image.open(i)
#     p_w = p_s.size[0]  # size结果单位是px A3=1552*1060 - 像素 对应 297mm×420mm
#     p_h = p_s.size[1]  # A4=1190*776 - 像素 对应 210mm×297mm
#     print(p_s.size,p_s.info)
#     p_dpi = p_s.info['dpi']  # info结果单位是px/inchi 1英寸=2.54cm--JPG没有DPI信息
#     p_ws = p_w / p_dpi[0] * 25.4  # 单位mm
#     p_hs = p_h / p_dpi[1] * 25.4
#     p_s.close()
#
#     if (p_ws//297 + p_hs//297)==0:  # 判断A3|A4 选择参数
#         p_a34=0
#     else:p_a34=1
#
#     p_or = p_ws//p_hs #.Orientation 页面参数 0-纵排| 1 -横排
#
#     w.Selection.EndOf()
#     w.Selection.InsertBreak(Type=2)  # 分节符在下一页wdSectionBreakNextPage=2
#     w.Selection.EndOf()
#     # w.Selection.Text="123"
#
#     w.Selection.PageSetup.PaperSize=psize_a34[p_a34]
#     w.Selection.PageSetup.Orientation = p_or  # 根据图纸设置页面
#     s=w.Selection.InlineShapes.AddPicture(FileName=i)#插入图纸 - 大图纸必会在其后产生空白页
#     #     print(s.Height, s.Width)#A4=523.2999877929688 766.2000122070312
#     s.Select()
# w.Selection.EndOf()
# w.Selection.Delete()#删除产生的最后一页多余的空白页


# ------example9--全局查找替换关键字-
import win32com.client
import win32com.client.gencache
from win32com.client import constants,gencache
import os

oldword='Win32comtest'
newword='hellowindows'

w=gencache.EnsureDispatch('Word.Application')
doc=w.Documents.Open('3344.docx') # 打开指定文档-返回一个代表Document 对象
myrange=doc.Range() # Range-函数| ()默认全选 （Start=int ,End=int ）可选
myrange.Find.Execute(FindText='Win32comtest',ReplaceWith='hellowindows',Replace=constants.wdReplaceAll)#find后全部替换

s=myrange.Sections.__len__() #查看Sections的数量即count结果
print(s)

for i in range(1,s+1):
    h=doc.Sections(i).Headers(Index=constants.wdHeaderFooterPrimary)#wdHeaderFooterPrimary=1
    h.Range.Find.Execute(FindText='Win32comtest',ReplaceWith='hellowindows',Replace=constants.wdReplaceAll)#find后全部替换
    print(h)





















