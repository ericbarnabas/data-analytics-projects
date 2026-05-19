# ============================================
# Project 1: Data Cleaning & Preparation
# Tool: Python (Pandas)
# ============================================

import pandas as pd

# Load the raw dataset
df = pd.read_excel('Dataset for Data Analytics.xlsx', dtype={'OrderID': str, 'CustomerID': str, 'TrackingNumber': str})

# Preview the first 5 rows
print(df.head())

# Check shape - how many rows and columns
print("Shape:", df.shape)
# ============================================
# SECTION 2: Explore the Data
# ============================================

# Check column names and data types
print("\n--- Column Info ---")
print(df.dtypes)

# Check for missing values in each column
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check for duplicate rows
print("\n--- Duplicate Rows ---")
print("Total duplicates:", df.duplicated().sum())

# ============================================
# SECTION 3: Clean the Data
# ============================================

# --- Fix 1: Fill missing CouponCode values ---
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')
print("Missing CouponCode after fix:", df['CouponCode'].isnull().sum())

# --- Fix 2: Standardize Date format to YYYY-MM-DD ---
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
print("Sample dates after fix:", df['Date'].head(3).tolist())

# --- Fix 3: Strip whitespace from all text columns ---
text_cols = ['OrderID', 'CustomerID', 'Product', 'PaymentMethod',
             'OrderStatus', 'ShippingAddress', 'TrackingNumber',
             'CouponCode', 'ReferralSource']
for col in text_cols:
    df[col] = df[col].str.strip()
print("Whitespace stripped from all text columns")

# --- Fix 4: Verify no duplicate OrderIDs ---
print("Duplicate OrderIDs:", df['OrderID'].duplicated().sum())

# ============================================
# SECTION 4: Export Cleaned Data
# ============================================

# Save the cleaned dataframe to a new Excel file
df.to_excel('Cleaned_Dataset_Project1_Python.xlsx', index=False)

print("✅ Cleaned file saved successfully!")
print("Final shape:", df.shape)
print("Missing values remaining:", df.isnull().sum().sum())
print("Duplicate rows remaining:", df.duplicated().sum())