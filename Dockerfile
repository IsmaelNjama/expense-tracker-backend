# Stage 1: Build and test
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies including test dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the application code
COPY . .

# Run tests
RUN pytest --maxfail=1 --disable-warnings -q

# Stage 2: Production image
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy only application code (not tests or dev files)
COPY app ./app


# Expose the application port
EXPOSE 8000
# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
