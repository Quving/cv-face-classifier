FROM python:2.7

RUN apt-get update && apt-get install -y unzip

WORKDIR /workdir

COPY requirements.txt requirements.txt
COPY letsfaceit.py letsfaceit.py

RUN mkdir cnn
RUN wget -O class_indices.zip http://nextcloud.quving.com/s/GkdP5QoaPJpEs2d/download && unzip class_indices.zip -d cnn
RUN wget -O models.zip http://nextcloud.quving.com/s/ktXiwxgiAgxrA2L/download && unzip models.zip -d cnn

RUN pip install -r requirements.txt

CMD ["python", "letsfaceit.py"]
