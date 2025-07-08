FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Install Python dependencies
RUN pip install flask opencv-python requests numpy

# Run the app
CMD ["python", "app.py"]