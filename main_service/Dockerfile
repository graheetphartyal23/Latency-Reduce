FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (OpenCV & general tools)
RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy app files into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask opencv-python numpy requests

# Expose the port (optional but good for clarity)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
