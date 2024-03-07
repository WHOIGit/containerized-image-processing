FROM python:3.11-slim

# Set the working directory

WORKDIR /app

# install requirements

COPY ./app/requirements.txt .

RUN pip install -r requirements.txt

# Copy rest of app

COPY ./app .

EXPOSE 8000

# Run api.py when the container launches
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
