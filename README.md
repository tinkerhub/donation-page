# Donation Page
TinkerHub is helping 1000 of students learn technology. Here lies the code that enables you to commit small monthly contributions to our cause.
## How it Works ?
1. We use [RazorPay API](https://razorpay.com/docs/api/subscriptions/) for payment subscription.
2. Please visit the resources folder to find the design, workflow and helper docs.
## Languages and Libraries used
* HTML/CSS & JS
* Python
* Flask (Python) : for backend web app
* [Razorpay-Python](https://github.com/razorpay/razorpay-python) : for payment integration
* [MailGun](https://documentation.mailgun.com/en/latest/quickstart-sending.html#how-to-start-sending-email) : for sending mails 
## Configure and run
Edit the configure.sh and update your razorpay key and secret, mailgun private key and app settings.
Run
```
bash ./configure.sh
```
Go to the URL.

## Docker
Create a file env.dev.sh in ops directory and add the following,
```
RAZORPAY_KEY_TESTING=<KEY>
RAZORPAY_SECRET_TESTING=<SECRET>
APP_SETTINGS=donationpage.config.TestingConfig
RAZORPAY_KEY=<KEY>
RAZORPAY_SECRET=<SECRET>
MAILGUN_API_KEY=<PRIVATE_KEY>
```
Then run 
```
docker-compose build
```
```
docker-compose up -d
```
## How to Test
The current env.dev.sh configuration is set for testing mode.
For production edit the APP_SETTINGS in env.dev.sh as
```
APP_SETTINGS=donationpage.config.ProductionConfig
```
## Commit Guidelines
Commit to respective branches for the frontend,backend, and bug fixes.
## Contributors list
1. [Abid Aboobaker](https://github.com/ekuttan)
2. [Gopikrishnan Sasikumar](https://github.com/gopikrishnansasikumar)
3. [Abhijith Neil Abraham](https://github.com/abhijithneilabraham)
4. [Sudev Suresh Sreedevi](https://github.com/GameGodS3)
5. [Navaneeth KT](https://github.com/Navan0)
6. [Rahul](https://github.com/monkeyscript)

Made with :heart: by Team TinkerHub
