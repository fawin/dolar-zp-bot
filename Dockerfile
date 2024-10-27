FROM python:3.12-alpine

COPY requirements.txt .
COPY dolarhoy.py .
COPY dolar.png .
COPY btc.png .

RUN python -m pip install -r requirements.txt

CMD ["python", "dolarhoy.py"]
