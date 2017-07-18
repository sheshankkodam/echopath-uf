FROM python:2.7.12

COPY ./ /etc/opt/echopath-uf

WORKDIR /etc/opt/echopath-uf

EXPOSE 5000

RUN pip install -r requirements.txt


