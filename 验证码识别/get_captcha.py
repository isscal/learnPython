import time

import requests

for i in range(1, 10):
    with open('img\\{}.png'.format(i), 'wb') as f:
        time.sleep(0.1)
        # f.write(requests.get('http://my.hlju.edu.cn/captchaGenerate.portal').content)
        f.write(requests.get('http://192.168.1.139/IISP//identiryCode/getIdentiryCode').content)
        
        print('成功获取一张验证码')
