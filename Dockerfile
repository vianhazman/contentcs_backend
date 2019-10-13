FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
EXPOSE 8000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["bash","entrypoint.sh"]