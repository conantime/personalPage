#coding:utf-8

from url import url

import tornado.web
import os

setting = dict(

	template_path=os.path.join(os.path.dirname(__file__),"render"),
	static_path=os.path.join(os.path.dirname(__file__),"static")
)

application = tornado.web.Application(
	handlers=url,
	debug=False,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    xsrf_cookie = True,
    login_url = "/login",
    **setting
    )