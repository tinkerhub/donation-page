import requests
from donationpage import app
tinkerhub_subject = "Thank you for contributing to TinkerHub"
tinkerhub_text= "Payment recieved.\n Thank you."
tinkerhub_sender='Hakuna Matata<no-reply@community.tinkerhub.org>'
def send_mail(reciever, sender=tinkerhub_sender, subject=tinkerhub_subject, text=tinkerhub_text):
    return requests.post(
        "https://api.mailgun.net/v3/community.tinkerhub.org/messages",
        auth=("api", app.config['MAILGUN_API_KEY']),
        data={"from": sender,
              "to": [reciever],
              "subject": subject,
              "text": text})

