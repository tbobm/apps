FROM python:3.12-slim AS release

WORKDIR /app

EXPOSE 8000
RUN pip install poetry
# NOTE: could implement healthcheck

# install dependencies
COPY . .

RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "dump.main:app", "--host", "0.0.0.0" ]
