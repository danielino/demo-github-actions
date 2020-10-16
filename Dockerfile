FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY demo .

COPY app.py .

CMD ["python3", "app.py"]