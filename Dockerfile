
FROM python:3.9





RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc pkg-config


COPY . .


RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

RUN pip install --no-cache-dir -r requirements.txt



ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


EXPOSE 8000


CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
