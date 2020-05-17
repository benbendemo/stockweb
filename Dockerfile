FROM python:3.7-slim

# This is Dockerfile for stockweb
ARG AIRFLOW_USER_HOME=/usr/local/stockweb
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}

COPY ./apt-source.list /etc/apt/sources.list

RUN apt-get update -y && apt-get install -y \
        build-essential \
        libpq-dev \
        apt-utils \
        curl \
        netcat \
        locales \
        vim \
        lsof \
	procps \
        && useradd -m airflow -g sudo -s /bin/bash -d ${AIRFLOW_USER_HOME} \
	&& apt-get clean

COPY requirements.txt requirements.txt

# Use below to replace alpine pip mirror
RUN pip install pip -U && \
    pip config set global.index-url https://pypi.doubanio.com/simple && \
    pip install -r requirements.txt


USER airflow
WORKDIR ${AIRFLOW_USER_HOME}

COPY . /user/local/stockweb

# ENTRYPOINT ["entrypoint.sh"]
CMD python3 manage.py runserver -h 0.0.0.0 -r -d
