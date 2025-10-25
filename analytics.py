import pandas as pd
import os
import subprocess
import sys
def main():
    print("\n" + "="*50)
    print("STEP 3: ANALYTICS")
    print("="*50 + "\n")
    
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <data_preprocessed.csv>")
        sys.exit(1)

    in_path = sys.argv[1]
    if not os.path.exists(in_path):
        print(f"ERROR: file not found: {in_path}")
        sys.exit(2)
    
    df = pd.read_csv(in_path)
    
    # ===== INSIGHT 1: Top Items Analysis =====
    print("Generating Insight 1: Top Selling Items...")
    
    top_items = df['Item'].value_counts().head(5)
    total_trans = len(df)
    
    insight1 = f"""INSIGHT 1: TOP SELLING ITEMS
{'='*50}

Total Transactions Analyzed: {total_trans}

Top 5 Best-Selling Items:
"""
    for i, (item, count) in enumerate(top_items.items(), 1):
        pct = (count / total_trans) * 100
        insight1 += f"{i}. {item}: {count} transactions ({pct:.1f}%)\n"
    
    insight1 += f"\nKey Finding:\n'{top_items.index[0]}' is the most popular item, accounting for {(top_items.values[0]/total_trans)*100:.1f}% of all transactions."
    
    with open("insight1.txt", "w") as f:
        f.write(insight1)
    print("   ✓ Saved: insight1.txt\n")
    
    # ===== INSIGHT 2: Payment Method Preferences =====
    print("Generating Insight 2: Payment Methods...")
    
    payment = df['Payment Method'].value_counts()
    payment_pct = (payment / len(df) * 100).round(1)
    
    insight2 = f"""INSIGHT 2: PAYMENT METHOD PREFERENCES
{'='*50}

Payment Method Distribution:
"""
    for method, count in payment.items():
        pct = payment_pct[method]
        insight2 += f"- {method}: {count} transactions ({pct}%)\n"
    
    most_used = payment.index[0]
    insight2 += f"\nKey Finding:\n'{most_used}' is the preferred payment method used in {payment_pct[most_used]}% of transactions."
    
    with open("insight2.txt", "w") as f:
        f.write(insight2)
    print("   ✓ Saved: insight2.txt\n")
    
    # ===== INSIGHT 3: Location & Revenue Analysis =====
    print("Generating Insight 3: Location Revenue...")
    
    location_revenue = df.groupby('Location')['Total Spent'].agg(['sum', 'mean', 'count'])
    location_revenue = location_revenue.sort_values('sum', ascending=False)
    
    insight3 = f"""INSIGHT 3: LOCATION REVENUE ANALYSIS
{'='*50}

Revenue by Location:
"""
    for loc in location_revenue.index:
        total = location_revenue.loc[loc, 'sum']
        avg = location_revenue.loc[loc, 'mean']
        count = int(location_revenue.loc[loc, 'count'])
        insight3 += f"\n{loc}:\n"
        insight3 += f"  - Total Revenue: ${total:,.2f}\n"
        insight3 += f"  - Avg Transaction: ${avg:.2f}\n"
        insight3 += f"  - Transactions: {count}\n"
    
    top_loc = location_revenue.index[0]
    top_revenue = location_revenue.loc[top_loc, 'sum']
    insight3 += f"\nKey Finding:\n'{top_loc}' generates the highest revenue at ${top_revenue:,.2f}, representing {(top_revenue/df['Total Spent'].sum()*100):.1f}% of total sales."
    
    with open("insight3.txt", "w") as f:
        f.write(insight3)
    print("   ✓ Saved: insight3.txt\n")
    
    print("="*50)
    print("All insights generated successfully!")
    print("="*50 + "\n")
    for i, text in enumerate(["Insight 1", "Insight 2", "Insight 3"], start=1):
        with open(f"/app/pipeline/insight{i}.txt", "w") as f:
            f.write(text)
        print(f"✓ Saved: insight{i}.txt")
    os.system("python visualize.py")
    subprocess.run(["python", "visualize.py", in_path], check=True)


if __name__ == "__main__":
    main()
