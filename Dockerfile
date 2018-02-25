FROM python:2.7

WORKDIR /workdir
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "letsfaceit.py"]
