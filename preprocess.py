import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

def main():
    print("\n" + "="*50)
    print("STEP 2: DATA PREPROCESSING")
    print("="*50 + "\n")
    
    df = pd.read_csv("Data/dirty_cafe_sales.csv")
    original_rows = len(df)
    
    # ===== DATA CLEANING =====
    print("1. Data Cleaning:")
    
    # Replace ERROR/UNKNOWN with NaN
    df = df.replace(['ERROR', 'UNKNOWN'], np.nan)
    
    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"   - Duplicates removed: {before - len(df)}")
    
    # Convert to numeric
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
    df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
    
    # Drop rows with critical missing data
    before = len(df)
    df = df.dropna(subset=['Transaction Date', 'Item'])
    print(f"   - Invalid dates/items dropped: {before - len(df)}")
    
    # Item-specific price imputation
    df['Price Per Unit'] = df.groupby('Item')['Price Per Unit'].transform(
        lambda x: x.fillna(x.mean())
    )
    
    # Fill remaining nulls
    df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
    df['Total Spent'] = df['Total Spent'].fillna(df['Total Spent'].median())
    df['Payment Method'] = df['Payment Method'].fillna('Unknown')
    df['Location'] = df['Location'].fillna('Unknown')
    
    print(f"   - Final rows: {len(df)} (removed {original_rows - len(df)} total)\n")
    
    # ===== FEATURE TRANSFORMATION =====
    print("2. Feature Transformation:")
    
    # Encode categoricals
    le_payment = LabelEncoder()
    le_location = LabelEncoder()
    le_item = LabelEncoder()
    
    df['Payment_Encoded'] = le_payment.fit_transform(df['Payment Method'])
    df['Location_Encoded'] = le_location.fit_transform(df['Location'])
    df['Item_Encoded'] = le_item.fit_transform(df['Item'])
    print(f"   - Encoded: Payment ({len(le_payment.classes_)}), Location ({len(le_location.classes_)}), Item ({len(le_item.classes_)})")
    
    # Scale numerics
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[['Quantity', 'Price Per Unit', 'Total Spent']])
    df['Quantity_Scaled'] = scaled[:, 0]
    df['Price_Scaled'] = scaled[:, 1]
    df['Total_Scaled'] = scaled[:, 2]
    print(f"   - Scaled: 3 numeric features\n")
    
    # ===== DIMENSIONALITY REDUCTION =====
    print("3. Dimensionality Reduction:")
    
    selected = ['Transaction ID', 'Item', 'Quantity', 'Price Per Unit', 'Total Spent',
                'Payment Method', 'Location', 'Transaction Date', 'Payment_Encoded', 
                'Location_Encoded', 'Item_Encoded', 'Quantity_Scaled', 'Price_Scaled', 
                'Total_Scaled']
    df = df[selected]
    print(f"   - Selected {len(selected)} columns\n")
    
    # ===== DISCRETIZATION =====
    print("4. Discretization:")
    
    df['Spending_Category'] = pd.cut(df['Total Spent'], 
                                      bins=[0, 10, 25, 50, float('inf')],
                                      labels=['Low', 'Medium', 'High', 'Very High'])
    
    df['Quantity_Category'] = pd.cut(df['Quantity'], 
                                      bins=[0, 1, 3, 5, float('inf')],
                                      labels=['Single', 'Few', 'Several', 'Many'])
    print(f"   - Created: Spending_Category, Quantity_Category\n")
    
    # Save
    df.to_csv("data_preprocessed.csv", index=False)
    print("="*50)
    print(f"Saved: data_preprocessed.csv ({len(df)} rows × {len(df.columns)} cols)")
    print("="*50 + "\n")
    
    os.system("python analytics.py")

if __name__ == "__main__":
    main()
