FROM python:3.8-slim as release

WORKDIR /app

EXPOSE 5000
# NOTE: could implement healthcheck

# install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# install application
COPY . .

RUN pip install -e .

ENTRYPOINT [ "gunicorn", "-c", "/app/gunicorn.py", "webserver.app:app" ]
