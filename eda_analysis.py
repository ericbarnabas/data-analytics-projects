# ============================================
# Project 2: Exploratory Data Analysis (EDA)
# Tool: Python (Pandas)
# ============================================

import pandas as pd

# Load the cleaned dataset from Project 1
df = pd.read_excel('Cleaned_Dataset_Project1_Python.xlsx')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Quick preview
print("Shape:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))

# ============================================
# SECTION 2: Descriptive Statistics
# ============================================

print("\n--- Basic Statistics ---")
print("Total Orders:", len(df))
print("Total Revenue: ₦{:,.2f}".format(df['TotalPrice'].sum()))
print("Mean Order Value: ₦{:,.2f}".format(df['TotalPrice'].mean()))
print("Median Order Value: ₦{:,.2f}".format(df['TotalPrice'].median()))
print("Highest Order: ₦{:,.2f}".format(df['TotalPrice'].max()))
print("Lowest Order: ₦{:,.2f}".format(df['TotalPrice'].min()))
print("Avg Quantity per Order: {:.2f}".format(df['Quantity'].mean()))

print("\n--- Full Statistical Summary ---")
print(df[['Quantity', 'UnitPrice', 'TotalPrice']].describe())

# ============================================
# SECTION 3: Trend Analysis
# ============================================

# --- Revenue by Product ---
print("\n--- Revenue by Product ---")
product_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
print(product_revenue)

# --- Revenue by OrderStatus ---
print("\n--- Revenue by Order Status ---")
status_revenue = df.groupby('OrderStatus')['TotalPrice'].sum().sort_values(ascending=False)
print(status_revenue)

# --- Orders by Payment Method ---
print("\n--- Orders by Payment Method ---")
payment_counts = df.groupby('PaymentMethod')['OrderID'].count().sort_values(ascending=False)
print(payment_counts)

# --- Revenue by Month ---
print("\n--- Revenue by Month ---")
df['Month'] = df['Date'].dt.strftime('%b')
df['MonthNum'] = df['Date'].dt.month
monthly = df.groupby(['MonthNum','Month'])['TotalPrice'].sum().reset_index()
monthly = monthly.sort_values('MonthNum')
print(monthly[['Month','TotalPrice']])

# ============================================
# SECTION 4: Outlier Detection (IQR Method)
# ============================================

print("\n--- Outlier Detection: TotalPrice ---")
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]

print(f"Q1: ₦{Q1:.2f}")
print(f"Q3: ₦{Q3:.2f}")
print(f"IQR: ₦{IQR:.2f}")
print(f"Lower Bound: ₦{lower_bound:.2f}")
print(f"Upper Bound: ₦{upper_bound:.2f}")
print(f"Number of Outliers: {len(outliers)}")

# ============================================
# SECTION 5: Correlation Analysis
# ============================================

print("\n--- Correlation Analysis ---")
corr = df[['Quantity', 'UnitPrice', 'TotalPrice']].corr()
print(corr)

# ============================================
# SECTION 6: Export Summary
# ============================================

summary = {
    'Metric': ['Total Orders','Total Revenue','Mean Order','Median Order',
               'Highest Order','Lowest Order','Outliers Found'],
    'Value': [len(df), df['TotalPrice'].sum(), df['TotalPrice'].mean(),
              df['TotalPrice'].median(), df['TotalPrice'].max(),
              df['TotalPrice'].min(), len(outliers)]
}

summary_df = pd.DataFrame(summary)
summary_df.to_excel('EDA_Summary_Project2.xlsx', index=False)
print("\n✅ EDA Summary exported successfully!")