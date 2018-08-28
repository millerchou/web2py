# -*- coding: utf-8 -*-
from gluon.storage import Storage
from gluon.custom_import import track_changes

track_changes(True)
WX = Storage(
    appid='wx4835e96f55b2a3ec', appsecret='890d0dcec1b3c0df5b94d45c45dcb454', grant_type='authorization_code'
)
