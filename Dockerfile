FROM python:3.8.5-buster

COPY app /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python","chatbot.py" ] 