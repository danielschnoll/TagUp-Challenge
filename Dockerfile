FROM python:3.8-alpine

WORKDIR /TagUp\ (2022)

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP="app.py"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p", "8080"]