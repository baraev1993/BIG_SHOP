FROM ubuntu

WORKDIR /

COPY . .

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt install python3-pip -y
RUN pip install --upgrade pip
RUN pip install wheel gunicorn
RUN pip install -r req.txt

ENV SECRET_KEY=django-insecure-(^-9$l#yj_ei#n$3ss3h*&_trya(=k+v6-4&9%=tq*x#kb%q$g
ENV DB_NAME=railway
ENV DB_USER=postgres 
ENV DB_PASSWORD=2kwPoq5OZxOPgVr24xDE
ENV DB_HOST=containers-us-west-102.railway.app
ENV DB_PORT=7496
ENV DEBUG=1
ENV ALLOWED_HOSTS=127.0.0.1,
ENV PORT=8000

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi:application
