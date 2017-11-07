import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
from Handlers.page import IndexHandler, LoginHandler, RegisterHandler, LogoutHandler,PinfoHandler
from Handlers.design import GetdesHandler, UploadHandler, ImgDlHandler
from Handlers.send import SendMsgHandler

url = [
            (r"/", IndexHandler),
            (r"/login", LoginHandler),
            (r"/register", RegisterHandler),
            (r"/logout", LogoutHandler),
            (r"/personal_info", PinfoHandler),
            (r"/get_design", GetdesHandler),
            (r"/upload", UploadHandler),
            (r"/imgdl", ImgDlHandler),
            (r"/send_msg", SendMsgHandler)
]

