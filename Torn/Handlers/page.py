#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from Conn import conn
import tornado.ioloop
import tornado.web
import re
import json
import os


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *arg, **kwargs):
        user = tornado.web.escape.xhtml_escape(self.current_user)
        path = os.getcwd() + "\static\img"
        files = []
        for file in os.walk(path):
            files.append(file)
        print files[0][2]
        if user+".jpg" not in files[0][2]:
            self.render("index.html", cur_user="default")
        else:
            self.render("index.html", cur_user=user)


    def post(self, *args, **kwargs):
        pass


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html")

    def post(self, *args, **kwargs):
        user = {}
        user["uname"] = self.get_argument("uname")
        print user["uname"]
        user["upass"] = self.get_argument("upass")
        conns = conn()

        for i in conns.get_list(m="test", l="user").find({"uname": user["uname"]}):
            if user["upass"] == i["upass"]:
               self.set_secure_cookie("user", user["uname"], expires_days=20, version=2.0)
               self.redirect("/")
            else:
               data = {"data": "Uknown User"}
               self.write(json.dumps(data))


class RegisterHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("register.html")

    def post(self, *args, **kwargs):
        uname = self.get_argument("uname")
        upass = self.get_argument("upass")
        sname = self.get_argument("sname")
        sex = self.get_argument("sex")
        id_card = self.get_argument("id_card")
        conns = conn()
        user = conns.get_list(m="test", l="user")
        auser = {"uname": uname, "upass": upass,
                 "sname": sname, "sex": sex,
                 "id_card": id_card}
        user.insert(auser)
        for i in user.find():
            print i
        self.redirect("login")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("user")
        self.redirect("/")


class PinfoHandler(BaseHandler):

     def get(self, *args, **kwargs):
         pass
     def post(self, *args, **kwargs):
         path = os.getcwd()+"\static\img"  #获取当前的路径
         upload_path = os.path.join(os.path.dirname(__file__), "../static/img")
         user=self.get_current_user()


         #获取上传路径
         file_metas = self.request.files["fi"]  #获取AJAX中的FORM数据或获取前端FILE文件名字为FI的
         for meta in file_metas:
             file_name = meta["filename"]
             file_path = os.path.join(upload_path, file_name) #得到的是文件的路径
             with open(file_path, 'wb') as up:
                 up.write(meta['body'])
             for file in os.walk(path):
                 if user+".jpg" in file[2]:
                    os.remove(path+"\\"+user+".jpg")
                    os.rename(path+"\\"+file_name, path+"\\"+user+".jpg") #切记要指定到绝对路径下
                 else:
                     os.rename(path + "\\" + file_name, path + "\\" + user + ".jpg")
         self.write(user)


