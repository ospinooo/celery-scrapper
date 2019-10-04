FROM python:3-alpine

# Dependencies Libraries
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# App
ADD ./src ./src

# Run the stream
CMD ["python", "src/sub.py"]
