FROM python:3

COPY . /cryptobot
WORKDIR /cryptobot

#COPY requirements.txt .

RUN pip install --no-cache-dir pipenv==2018.11.26
RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "flask", "run" ]
