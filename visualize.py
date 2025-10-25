import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    print("\n" + "="*50)
    print("STEP 4: VISUALIZATION")
    print("="*50 + "\n")
    
    df = pd.read_csv("data_preprocessed.csv")
    
    print("Creating correlation heatmap...")
    
    # Select numeric columns for correlation
    numeric_cols = ['Quantity', 'Price Per Unit', 'Total Spent', 
                    'Payment_Encoded', 'Location_Encoded', 'Item_Encoded']
    
    # Create correlation matrix
    corr_matrix = df[numeric_cols].corr()
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    
    plt.title('Feature Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('summary_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("   ✓ Saved: summary_plot.png\n")
    
    print("="*50)
    print("Visualization complete!")
    print("="*50 + "\n")
    
    os.system("python cluster.py")

if __name__ == "__main__":
    main()
