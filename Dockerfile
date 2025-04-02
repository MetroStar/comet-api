FROM python:3.12

WORKDIR /code

COPY . .

RUN pip install .

COPY ./app /code/app
COPY ./.env /code/.env

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
