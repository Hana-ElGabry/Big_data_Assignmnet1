import pandas as pd
from sklearn.cluster import KMeans

def main():
    print("\n" + "="*50)
    print("STEP 5: CLUSTERING")
    print("="*50 + "\n")
    
    df = pd.read_csv("data_preprocessed.csv")
    
    print("Applying K-Means clustering...")
    
    # Select scaled features for clustering
    features = df[['Quantity_Scaled', 'Price_Scaled', 'Total_Scaled']]
    
    # Apply K-Means with 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(features)
    
    print("   ✓ Clustering complete\n")
    
    # Count samples per cluster
    cluster_counts = df['Cluster'].value_counts().sort_index()
    
    # Generate output text
    output = f"""K-MEANS CLUSTERING RESULTS
{'='*50}

Configuration:
- Algorithm: K-Means
- Number of Clusters: 3
- Features Used: Quantity, Price Per Unit, Total Spent (scaled)
- Total Samples: {len(df)}

Cluster Distribution:
"""
    
    for cluster_id, count in cluster_counts.items():
        percentage = (count / len(df)) * 100
        output += f"\nCluster {cluster_id}:\n"
        output += f"  - Samples: {count}\n"
        output += f"  - Percentage: {percentage:.1f}%\n"
    
    # Add cluster characteristics
    output += f"\n{'='*50}\nCluster Characteristics:\n"
    
    for cluster_id in cluster_counts.index:
        cluster_data = df[df['Cluster'] == cluster_id]
        output += f"\nCluster {cluster_id}:\n"
        output += f"  - Avg Quantity: {cluster_data['Quantity'].mean():.2f}\n"
        output += f"  - Avg Price: ${cluster_data['Price Per Unit'].mean():.2f}\n"
        output += f"  - Avg Spending: ${cluster_data['Total Spent'].mean():.2f}\n"
    
    # Save to file
    with open("clusters.txt", "w") as f:
        f.write(output)
    
    print("   ✓ Saved: clusters.txt\n")
    
    print("="*50)
    print("Clustering complete!")
    print("="*50 + "\n")
    
    print("Pipeline execution finished!\n")

if __name__ == "__main__":
    main()
