FROM python:3.11.3-slim-buster

ENV PYTHONPATH "/app"

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "inventory/app.py" ]
ENTRYPOINT [ "python3" ]