if [ -z "$1" ]; then
  echo "Usage: $0 <container_name>"
  exit 1
fi

CONTAINER=$1
HOST_RESULTS_DIR="$(pwd)/results"

echo "Copying outputs from container '$CONTAINER'..."
mkdir -p "$HOST_RESULTS_DIR"

# Copy CSV, TXT, PNG from container's working dir
docker cp "${CONTAINER}":/app/pipeline/data_raw.csv "${HOST_RESULTS_DIR}/" || true
docker cp "${CONTAINER}":/app/pipeline/data_preprocessed.csv "${HOST_RESULTS_DIR}/" || true
docker cp "${CONTAINER}":/app/pipeline/insight1.txt "${HOST_RESULTS_DIR}/" || true
docker cp "${CONTAINER}":/app/pipeline/insight2.txt "${HOST_RESULTS_DIR}/" || true
docker cp "${CONTAINER}":/app/pipeline/insight3.txt "${HOST_RESULTS_DIR}/" || true
docker cp "${CONTAINER}":/app/pipeline/clusters.txt "${HOST_RESULTS_DIR}/" || true
docker cp "${CONTAINER}":/app/pipeline/summary_plot.png "${HOST_RESULTS_DIR}/" || true

echo "Files copied to ${HOST_RESULTS_DIR} (if exist)."

echo "Stopping container ${CONTAINER}..."
docker stop "${CONTAINER}" || true

echo "Removing container ${CONTAINER}..."
docker rm "${CONTAINER}" || true

echo "Done."