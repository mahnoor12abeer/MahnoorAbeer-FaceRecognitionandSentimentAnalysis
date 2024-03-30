FROM python:3.8

WORKDIR /code

COPY ./app /code/app
COPY requirements.txt /code/

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install numpy
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]