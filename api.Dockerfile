# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY setup.py setup.py
RUN pip3 install --upgrade pip
RUN pip3 install -e .
COPY . .
