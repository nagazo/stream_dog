FROM python:3.9-slim

WORKDIR /code

COPY src/stream_dog /code/

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./code/requirements.txt

RUN pip install -r ./code/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app_esther.py", "--server.port=8501", "--server.address=0.0.0.0", "--reload"]
