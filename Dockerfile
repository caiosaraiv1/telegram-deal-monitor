# 1. Official Python base image (slim version = lighter)
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the dependencies file first (good practice for Docker caching)
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code into the container
COPY . .

# 6. Command executed when the container starts
CMD ["python", "-u", "main.py"]
