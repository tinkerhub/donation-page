FROM ubuntu:16.04

ENV RAZORPAY_KEY_TESTING $1
ENV RAZORPAY_SECRET_TESTING $2
ENV APP_SETTINGS backend.config.TestingConfig

# Installing base packages
RUN apt-get -y update && apt-get install wget unzip gcc tar -y && \
        apt-get install -y python-pip python-dev

# Copy files to container
COPY . /app

# Set working directory
WORKDIR /app

# Upgrade PIP
RUN pip install --upgrade pip

# Install the project and dependencies
RUN pip install -e .

ENTRYPOINT [ "python" ]

CMD [ "backend/run.py" ]

