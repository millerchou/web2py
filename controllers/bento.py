# -*- coding: utf-8 -*-
import requests


def get_code():
    js_code = request.vars.code
    if js_code:
        data = Storage(appid=WX.appid, secret=WX.appsecret, js_code=js_code, grant_type=WX.grant_type)
        r = requests.post(url='https://api.weixin.qq.com/sns/jscode2session', data=data)
        print r.text
