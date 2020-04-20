# Donation Page
TinkerHub is helping 1000 of students learn technology. Here lies the code that enables you to commit small monthly contributions to our cause.
## How it Works ?
1. We use [RazorPay API](https://razorpay.com/docs/api/subscriptions/) for payment subscription.
2. Please visit the resources folder to find the design, workflow and helper docs.
## Languages and Libraries used
* HTML/CSS & JS
* Python
* Flask (Python) : for backend web app
## Configure and run
- Edit the configure.sh and add your razorpay key and secret.
- Run
```
bash ./configure.sh
```
- Go to the URL.

## Docker
```
docker build -t donations:latest .
```
```
docker run -d -p 5000:5000 donations:latest
```
## How to Test
Instructions for testing  
## Commit Guidelines
Commit to respective branches for the frontend,backend, and bug fixes.
## Contributors list
1. [Abid Aboobaker](https://github.com/ekuttan)
2. [Gopikrishnan Sasikumar](https://github.com/gopikrishnansasikumar)
3. [Abhijith Neil Abraham](https://github.com/abhijithneilabraham)
4. [Sudev Suresh Sreedevi](https://github.com/GameGodS3)
5. [Navaneeth KT](https://github.com/Navan0)
