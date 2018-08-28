# -*- coding: utf-8 -*-


# def index():
# 	return dict(hi=T('hello'))
# def one():
# 	return dict(link=URL('two', hmac_key=KEY))
#
#
# def two():
# 	if not URL.verify(request, hmac_key=KEY):
# 		raise HTTP(403)
# 	# do something
# 	return locals()

def test():
    rows = db(db.test.id > 0).select()
    return dict(data=rows)
