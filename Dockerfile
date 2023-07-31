# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container's working directory
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install uvicorn

# Copy the entire application directory into the container's working directory
COPY . .

# Expose the port on which the FastAPI application will run (change it to your FastAPI app's port)
EXPOSE 8000

# Command to run the FastAPI application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
