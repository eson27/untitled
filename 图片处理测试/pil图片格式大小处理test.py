''' --------
   sep1.获取文件路径filename_dir-- 输入pics_path 输出 f_res=[]
        将要处理的图片放在同目录文件夹testpics
            图片按顺序编号
    sep2.获取图片转成BMP格式-- 输入pics_path 输出 bmp_res=[]
        注：在这里做缩放图片会不清晰，不做缩放

'''

from os import walk,mkdir,remove
import shutil
from PIL import Image


def filename_dir(pics_path):
    # for root ,dirs ,files in walk(pics_path):
     #     print('root:',root,'dirs:',dirs,'files:',files)
    f_res_0=list(walk(pics_path))[0] #('testpics', [], ['1.jpg', '2.jpg', '3.jpg'])
    f_res=[(f_res_0[0]+'\\'+i) for i in f_res_0[2]]
    # print(f_res)#['testpics\r1.jpg', 'testpics\r2.jpg', 'testpics\r3.jpg']
    return(f_res)

def bmp_tr(pics_path,f_res):
    bmp_path = pics_path + "_bmp"
    shutil.rmtree(bmp_path, True) #先删除原有bmp文件夹再建一个新的
    bmp_path=mkdir(bmp_path)
    pic_list=f_res
    for i in pic_list:
        im = Image.open(i)
        # im=im.resize((200, 200),Image.ANTIALIAS)

        name_0=i.split('\\')
        name_1=name_0[0]+"_bmp\\"+name_0[1].split('.')[0]+".bmp"
        im.save(name_1,'bmp', quality = 100)
        # im2=Image.open(name_1)
        # im3=im2.resize((300, 400),Image.ANTIALIAS)
        # im3.save(name_1, 'bmp', quality=100)



def main():
    pics_path='testpics'
    f_res=filename_dir(pics_path)
    bmp_tr(pics_path, f_res)

if __name__=="__main__":
    main()
