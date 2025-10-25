import sys
import os
import pandas as pd
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <Data\dirty_cafe_sales.csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"ERROR: file not found: {input_path}")
        sys.exit(2)

    print(f"Reading dataset from: {input_path}")
    df = pd.read_csv(input_path)
    out_path = "/app/pipeline/data_raw.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved raw data to: {out_path}")

    # call next stage
    subprocess.run(["python", "preprocess.py", out_path], check=True)

if __name__ == "__main__":
    main()
    