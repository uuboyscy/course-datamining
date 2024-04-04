FROM python:3.11-slim-bullseye

ENV TZ=Asia/Taipei

COPY Pipfile .

RUN apt-get update && \
    apt-get install git zsh vim curl procps gcc python3-dev -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    echo "Y" | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv lock --dev && \
    pipenv requirements --dev > requirements.txt && \
    pip install -r requirements.txt
