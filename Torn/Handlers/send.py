from page import BaseHandler
import smtplib

class SendMsgHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        name = self.get_body_argument("name")
        email = self.get_body_argument("email")
        message = self.get_body_argument("message")

