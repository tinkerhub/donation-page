from setuptools import setup, find_packages

requirements = [
    "pytest",
    "requests",
    "flask",
    "gunicorn",
    "razorpay",
    "uWSGI",
    "Werkzeug",
    "emoji"
]

setup(
    name="donation-page",
    version="0.0.1",
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements)
