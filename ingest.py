import pandas as pd
import sys
import os

def main():
    print("\nSTEP 1: DATA INGESTION\n")
    
    file_path = sys.argv[1]
    df = pd.read_csv(file_path)
    print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nMissing values:\n{df.isnull().sum()}\n")
    
    df.to_csv("data_raw.csv", index=False)
    print("✓ Saved copy as: data_raw.csv\n")
    
    os.system("python preprocess.py")

if __name__ == "__main__":
    main()
