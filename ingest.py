import pandas as pd
import os
import shutil

def main():
    print("STEP 1: DATA INGESTION\n")
    
    local_path = "Data/dirty_cafe_sales.csv"
    
    # Download from Kaggle if not exists
    if not os.path.exists(local_path):
        import kagglehub
        download_path = kagglehub.dataset_download("ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training")
        
        for file in os.listdir(download_path):
            if file.endswith('.csv'):
                shutil.copy(os.path.join(download_path, file), local_path)
                break
    
    # Load data
    df = pd.read_csv(local_path)
    print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nMissing values:\n{df.isnull().sum()}\n")
    
    os.system("python preprocess.py")

if __name__ == "__main__":
    main()
