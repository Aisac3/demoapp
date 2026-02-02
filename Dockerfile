# 1. Use official Python image (Linux + Python)
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy app code into container
COPY app/doesnotexist.py .


# 4. Run the application
CMD ["python", "app.py"]
