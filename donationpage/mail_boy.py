import requests
from donationpage import app

class MailBoy(object):
    def __init__(self):
        self.subject = "Thank you for contributing to TinkerHub"
        self.text= "Hey\n Your valuable contribution to tinkerhub is recieved with love.\n Thank you."
        self.sender='Hakuna Matata<no-reply@community.tinkerhub.org>'
    
    def send(self, reciever):
        return requests.post(
            "https://api.mailgun.net/v3/community.tinkerhub.org/messages",
            auth=("api", app.config['MAILGUN_API_KEY']),
            data={"from": self.sender,
                "to": [reciever],
                "subject": self.subject,
                "text": self.text})

