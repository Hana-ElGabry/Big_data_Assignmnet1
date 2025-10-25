#!/bin/bash

echo "=========================================="
echo "SUMMARY: Extracting Results from Docker"
echo "=========================================="
echo ""

# Create results directory on host if it doesn't exist
mkdir -p results

# Container name
CONTAINER_NAME="analytics-container"

echo "Copying generated files from container to host..."
echo ""

# Copy all CSV files
echo "� Copying CSV files..."
docker cp ${CONTAINER_NAME}:/app/pipeline/data_preprocessed.csv ./results/

# Copy all text insight files
echo "� Copying insight files..."
docker cp ${CONTAINER_NAME}:/app/pipeline/insight1.txt ./results/
docker cp ${CONTAINER_NAME}:/app/pipeline/insight2.txt ./results/
docker cp ${CONTAINER_NAME}:/app/pipeline/insight3.txt ./results/

# Copy visualization
echo "� Copying visualization..."
docker cp ${CONTAINER_NAME}:/app/pipeline/summary_plot.png ./results/

# Copy clustering results
echo "� Copying clustering results..."
docker cp ${CONTAINER_NAME}:/app/pipeline/clusters.txt ./results/

echo ""
echo "✓ All files copied to ./results/"
echo ""

# List copied files
echo "Files in results directory:"
ls -lh results/
echo ""

# Stop and remove container
echo "Stopping and removing container..."
docker stop ${CONTAINER_NAME}
docker rm ${CONTAINER_NAME}

echo ""
echo "=========================================="
echo "✓ Summary Complete!"
echo "=========================================="
