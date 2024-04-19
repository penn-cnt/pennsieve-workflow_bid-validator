FROM python:3.9.12

WORKDIR /service

RUN apt clean && apt-get update

COPY . .

RUN ls /service

RUN mkdir -p data

# Add additional dependencies below ...
RUN pip install -r /service/requirements.txt

ENTRYPOINT [ "python3.9", "/service/main.py" ]