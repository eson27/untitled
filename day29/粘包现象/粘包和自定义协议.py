#ret=njm.zfill(4)  第一个字节协议规定和填充字长
import struct #固定长度
num1=12314244
num2=24324
num3=21
ret1=struct.pack('i',num1)
print(ret1)

ret2=struct.pack('i',num2)
print(ret2)

ret3=struct.pack('i',num3)
print(ret3)