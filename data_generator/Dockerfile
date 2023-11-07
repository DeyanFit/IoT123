FROM python:3.8 as stage-a

WORKDIR /app

FROM python:3.8-alpine

WORKDIR /app

COPY data_generator.py ./

CMD ["python", "data_generator.py"]
