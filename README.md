```markdown
# Customer Analytics Pipeline

## Team Members
- [Shahd Hamdy Ragab]
- [Hana Hatem Elgabry]
- [Khetam Mohamed]
- [Noor Akram alzoghby]

---

## Project Overview

This project implements a complete data analytics pipeline for cafe sales data using Docker. The pipeline performs data ingestion, preprocessing, analytics, visualization, and clustering on a dirty dataset containing 10,000 cafe transactions.

**Dataset Source:** [Kaggle - Cafe Sales Dirty Data](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training)

---

## Project Structure

```
customer-analytics/
├── Dockerfile              # Docker container configuration
├── ingest.py              # Data ingestion script
├── preprocess.py          # Data cleaning and preprocessing
├── analytics.py           # Generate textual insights
├── visualize.py           # Create correlation heatmap
├── cluster.py             # K-Means clustering
├── summary.sh             # Export results from container
├── README.md              # This file
├── Data/
│   └── dirty_cafe_sales.csv
└── results/               # Output files (generated)
    ├── data_preprocessed.csv
    ├── insight1.txt
    ├── insight2.txt
    ├── insight3.txt
    ├── summary_plot.png
    └── clusters.txt
```

---

## Pipeline Workflow

```
Data Ingestion → Preprocessing → Analytics → Visualization → Clustering
```

### 1. Data Ingestion (`ingest.py`)
- Downloads/loads raw cafe sales data
- Saves to Data folder
- **Output:** Raw dataset loaded

### 2. Preprocessing (`preprocess.py`)
- **Data Cleaning:** Handles missing values, removes duplicates, fixes data types
- **Feature Transformation:** Encodes categorical variables, scales numeric features
- **Dimensionality Reduction:** Selects 14 relevant columns
- **Discretization:** Creates spending and quantity categories
- **Output:** `data_preprocessed.csv` (8,613 clean rows)

### 3. Analytics (`analytics.py`)
- Generates 3 textual insights without visualizations
- **Output:** `insight1.txt`, `insight2.txt`, `insight3.txt`

### 4. Visualization (`visualize.py`)
- Creates correlation heatmap of numeric features
- **Output:** `summary_plot.png`

### 5. Clustering (`cluster.py`)
- Applies K-Means clustering (3 clusters) on scaled features
- **Output:** `clusters.txt`

---

## Installation & Setup

### Prerequisites
- Docker installed ([Get Docker](https://www.docker.com/get-started))
- Git (optional, for cloning)

### Step 1: Build Docker Image

```
cd customer-analytics
docker build -t customer-analytics .
```

**Expected output:**
```
Successfully built <image_id>
Successfully tagged customer-analytics:latest
```

---

## Execution

### Step 2: Run Docker Container

```
docker run -it --name analytics-container customer-analytics
```

This starts an interactive bash shell inside the container.

### Step 3: Run the Pipeline

Inside the container, execute:

```
python ingest.py Data/dirty_cafe_sales.csv
```

The pipeline will automatically run all scripts in sequence:
- `ingest.py` → `preprocess.py` → `analytics.py` → `visualize.py` → `cluster.py`

**Expected output:**
```
STEP 1: DATA INGESTION
STEP 2: DATA PREPROCESSING
STEP 3: ANALYTICS
STEP 4: VISUALIZATION
STEP 5: CLUSTERING
Pipeline execution finished!
```

### Step 4: Exit Container

```
exit
```

### Step 5: Extract Results

Run the summary script on your host machine:

**Linux/Mac:**
```
chmod +x summary.sh
./summary.sh
```

**Windows (Git Bash/WSL):**
```
bash summary.sh
```

This will:
- Copy all outputs to `./results/` folder
- Stop and remove the container

---

## Sample Outputs

### Data Statistics
- **Original rows:** 10,000
- **Clean rows:** 8,613 (removed 1,387 invalid records)
- **Features:** 16 columns (after preprocessing)
- **Missing values:** Handled using median/mode imputation

### Insights Generated
1. **Top Selling Items** - Coffee, Sandwich, Smoothie analysis
2. **Payment Preferences** - Distribution across payment methods
3. **Location Revenue** - Revenue breakdown by location

### Clustering Results
- **3 clusters** identified based on spending patterns
- Cluster characteristics included in `clusters.txt`

---

## Docker Commands Reference

| Command | Purpose |
|---------|---------|
| `docker build -t customer-analytics .` | Build the image |
| `docker images` | List images |
| `docker run -it --name analytics-container customer-analytics` | Run container |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop analytics-container` | Stop container |
| `docker rm analytics-container` | Remove container |
| `docker rmi customer-analytics` | Remove image |

---

## Technologies Used

- **Python 3.11**
- **pandas** - Data manipulation
- **numpy** - Numerical operations
- **scikit-learn** - Machine learning (K-Means, preprocessing)
- **matplotlib** - Visualization
- **seaborn** - Statistical visualization
- **Docker** - Containerization

---

## Troubleshooting

**Container already exists:**
```
docker rm analytics-container
```

**Port conflicts:**
```
docker ps
docker stop <container_id>
```

**Permission denied (summary.sh):**
```
chmod +x summary.sh
```

---

## License

This project is submitted as part of CSCI461 coursework at Nile University, Fall 2025.

---

## Acknowledgments

- Dataset: Ahmed Mohamed (Kaggle)
- Course Instructor: [Ebrahim Zaghloul Abdelbaky]
- Nile University - CSCI461 Course

---

**Submission Date:** October 26, 2025  
**Team Leader:** [Shahd Hamdy]
