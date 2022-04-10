FROM python:3.9

ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN groupadd -r pyapp && useradd -r -s /bin/false -g pyapp pyapp \
      && chown -R pyapp:pyapp /app

USER pyapp

COPY requirements.txt .

RUN pip install -r requirements.txt -t .

COPY . .

CMD [ "python", "app.py"]
