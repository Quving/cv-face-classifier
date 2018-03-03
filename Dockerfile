FROM python:2.7

RUN apt-get update && apt-get install -y unzip

WORKDIR /workdir

COPY requirements.txt requirements.txt
COPY letsfaceit.py letsfaceit.py
COPY start.sh start.sh

RUN mkdir cnn
RUN wget -O class_indices.zip http://nextcloud.quving.com/s/GkdP5QoaPJpEs2d/download && unzip class_indices.zip -d cnn
RUN wget -O models.zip http://nextcloud.quving.com/s/ktXiwxgiAgxrA2L/download && unzip models.zip -d cnn

RUN pip install -r requirements.txt

RUN printf "import keras\nkeras.applications.VGG16(include_top=False, weights='imagenet')" >> dl_vgg16.py
RUN python dl_vgg16.py

CMD ["bash", "-c", "start.sh"]
