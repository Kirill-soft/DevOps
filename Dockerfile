FROM ubuntu:24.10

RUN apt-get update && apt-get install -y python3.12

COPY . /laba

WORKDIR /laba

CMD ["python3.12", "LB_1.py"]