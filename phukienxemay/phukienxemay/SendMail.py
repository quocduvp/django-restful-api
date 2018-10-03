import sendgrid
from phukienxemay.settings import SEND_GRID_KEY
from sendgrid.helpers.mail import *

class SendMail():
    sg = sendgrid.SendGridAPIClient(api_key=SEND_GRID_KEY)
    send_to = ""
    send_from = ""
    content = ""
    subject = ""
    def send_mail(self):
        s_to = Email(self.send_to)
        s_from = Email(self.send_from)
        ct = Content("text/html", self.content)
        mail = Mail(s_from, self.subject, s_to, ct)
        response = self.sg.client.mail.send.post(request_body=mail.get())
        return response.status_code