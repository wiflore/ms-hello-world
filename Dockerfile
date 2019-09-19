FROM python:3.7

COPY . project/
WORKDIR project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python -u server.py