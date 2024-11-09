FROM python:alpine

LABEL maintainer="MaximumPigs - https://github.com/maximumpigs/discord_github_bot"
LABEL org.opencontainers.image.authors="MaximumPigs"
LABEL org.opencontainers.image.source="https://github.com/maximumpigs/discord_github_bot"

WORKDIR /usr/src/app

COPY discord_github.py .
COPY requirements.txt .

ENV DISCORD_TOKEN = "" \
    GITHUB_TOKEN = ""

RUN pip install --upgrade setuptools \
    && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./discord_github.py" ]