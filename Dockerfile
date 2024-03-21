FROM tiangolo/uvicorn-gunicorn:python3.10-slim

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
ENV MODULE_NAME=app
ADD requirements.txt .
RUN pip install -r requirements.txt \
    && rm -rf /root/.cache
COPY . .
CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "8080"]
