FROM python:3.11-slim

# Set the working directory

WORKDIR /app

COPY ./app .

# Install the required packages

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "process_images.py" ]
