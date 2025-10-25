
# Use Python 3.11 slim base image
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Install required Python packages
RUN pip install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    scipy \
    requests \
    kagglehub

# Create working directory inside container
WORKDIR /app/pipeline/

# Copy all project scripts into the container
COPY ingest.py .
COPY preprocess.py .
COPY analytics.py .
COPY visualize.py .
COPY cluster.py .

# Copy Data folder if it exists
# COPY Data/ ./Data/
COPY Data /app/pipeline/data
# Set working directory
WORKDIR /app/pipeline/

# Start interactive bash shell when container runs
CMD ["/bin/bash"]




