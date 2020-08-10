#生成一个随机字符串
# import os
# ret = os.urandom(16)
# print(ret)

# import hashlib
# sha = hashlib.sha1(密钥)
# sha.update(随机字符串)
# 结果=sha.hexdigest()

#新模块 替代hashlib
import os
import hmac
h = hmac.new(b'alex_sb',os.urandom(32),'md5') # digestmod='md5' / 'sha1'

ret=h.digest()
print(ret)
