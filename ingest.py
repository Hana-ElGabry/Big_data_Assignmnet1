import pandas as pd
import os

def main():
    print("\nSTEP 1: DATA INGESTION\n")
    
    local_path = "Data/dirty_cafe_sales.csv"
    
    df = pd.read_csv(local_path)
    print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nMissing values:\n{df.isnull().sum()}\n")
    
    os.system("python preprocess.py")

if __name__ == "__main__":
    main()
