FROM python:3.10-slim AS base

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM python:3.10 AS dev

COPY --from=base /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=base /usr/local/bin /usr/local/bin

ENV FLASK_APP=app