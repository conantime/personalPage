#coding:utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from page import BaseHandler
from Conn import conn
import json
import base64image
import base64
import re
file_path = os.getcwd()+"\\static\\file"





class GetdesHandler(BaseHandler):
    def getDesign(self, type, curpage):
        conns = conn()
        design = conns.get_list(m="test", l="design")
        uname = self.get_current_user()
        designs = design.find({"type": type, "uname": uname}).skip(6*curpage-1).limit(6*curpage)
        print designs
        li = []
        for i in designs:
            print i
            text = ""
            path = i["src"]
            print path
            ppath = os.getcwd() + "\\static\\file\\" + uname + "\\" + path
            if type == "1":
                with open(ppath, "r+") as rd:
                    for i in range(0, 4):
                        text = text+rd.readline()
                        print "text="+text
                        data = {"data": text}
                li.append(data)
            elif type == "2":
                paths = ppath.split("file")
                li.append(paths[1])
            elif type == "3":
                pass
        datas = {"data": li}
        return datas

    def get(self, *args, **kwargs):
        self.post()

    def post(self, *args, **kwargs):
        type = self.get_body_argument("type")
        print type
        datas = self.getDesign(type=type)

        self.write(json.dumps(datas))


class UploadHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("upload.html")

    def post(self, *args, **kwargs):
        conns = conn()
        des = conns.get_list(m="test", l="design")
        files = []
        uname = self.get_current_user()
        length = int(self.get_body_argument("length"))#获取文件长度
        ftype  = self.get_body_argument("type1")
        print ftype
        for i in range(0, length):
                files.append(self.request.files["f"+str(i)])
        if not os.path.exists(file_path+"\\"+uname):
                os.mkdir(file_path+"\\"+uname)
        print files
        for j in range(0, files.__len__()):
            filep= os.path.join(file_path+"\\"+uname, files[j][0]["filename"])
            with open(filep, "wb") as op:
                op.write(files[j][0]["body"])
                des.insert({"type": ftype,
                            "uname": uname,
                            "src": files[j][0]["filename"],
                            "updatatime": time.asctime()})

        self.redirect("/")


class ImgDlHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        img = self.get_body_argument("data")
        imgs = re.split(",", img)

        print imgs
        img1 = base64.b64decode(imgs[1])
        with open(os.getcwd()+"/static/img/myInfo.png", "wb+") as op:
            op.write(img1)
            op.flush()
        self.write("good")



