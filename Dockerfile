FROM python:3.10

RUN mkdir //job_searcher

WORKDIR /job_searcher

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /job_searcher

CMD gunicorn main:app --bind=0.0.0.0:8000