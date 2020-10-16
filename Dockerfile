FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY demo .

COPY main.py .

CMD ["python3", "main.py"]