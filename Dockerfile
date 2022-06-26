FROM python:3

RUN pip install numpy
RUN pip install tqdm
WORKDIR /home
