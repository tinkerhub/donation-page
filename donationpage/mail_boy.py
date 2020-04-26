import emoji
import requests
from donationpage import app

class MailBoy(object):
    def __init__(self):
        self.subject = "Thank you for contributing to TinkerHub "+emoji.emojize(":folded_hands:")
        self.text= "Thank you!\n\nGiving is a superpower, and you're a superhero!"+ emoji.emojize(":smiling_face_with_heart-eyes:") +"\n\n\n\nYour contribution is helping us sustain our efforts towards making a difference. If you're interested in what TinkerHub does and would like to volunteer, feel free to reach us at hello@tinkerhub.org.\n \nlove,\nTeam TinkerHub"
        self.sender='Hakuna Matata<no-reply@community.tinkerhub.org>'
    
    def send(self, reciever):
        return requests.post(
            "https://api.mailgun.net/v3/community.tinkerhub.org/messages",
            auth=("api", app.config['MAILGUN_API_KEY']),
            data={"from": self.sender,
                "to": [reciever],
                "subject": self.subject,
                "text": self.text})

