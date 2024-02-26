FROM python:3.11-slim

# Set the working directory

WORKDIR /app

# install requirements

COPY ./app/requirements.txt .

# Install git, install dependencies from requirements.txt, then remove git to save space
RUN apt-get update && \
    apt-get install -y git && \
    pip install -r requirements.txt && \
    apt-get remove -y git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy rest of app

COPY ./app .

EXPOSE 8000

# Run api.py when the container launches
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
