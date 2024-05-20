FROM amd64/python:3.12.3-alpine
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]