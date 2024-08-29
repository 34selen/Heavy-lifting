# Dockerfile

# Python 3.9 기본 이미지 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치 (MySQL client 라이브러리 포함)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc pkg-config

# 애플리케이션의 모든 파일 복사
COPY . .

# Python 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# Flask 애플리케이션을 실행하기 위한 환경 변수 설정
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 컨테이너가 8000 포트를 사용할 수 있도록 설정
EXPOSE 8000

# Flask 애플리케이션 실행
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
