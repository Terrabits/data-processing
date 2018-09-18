FROM python:3.7.0-slim-stretch

RUN pip install --upgrade pip setuptools wheel
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY    app.py requirements.txt ./
RUN     pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
