FROM python:3.9

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip3 install pipenv
RUN pipenv install
COPY . .

CMD [ "python", "__main__.py"]