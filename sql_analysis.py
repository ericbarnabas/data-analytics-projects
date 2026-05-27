import pandas as pd
import sqlite3

# ── 1. Load the cleaned Excel dataset ──────────────────────────────────────
df = pd.read_excel("Cleaned_Dataset_Project1_Python.xlsx")

# ── 2. Create an in-memory SQLite database and load the data ───────────────
conn = sqlite3.connect(":memory:")
df.to_sql("orders", conn, index=False, if_exists="replace")

print("✅ Database loaded successfully!")
print(f"   Table 'orders' has {len(df)} rows and {len(df.columns)} columns.\n")

# ── QUERY 1: Preview the table (first 10 rows) ─────────────────────────────
print("=" * 60)
print("QUERY 1: First 10 Rows of the Orders Table")
print("=" * 60)

query1 = """
SELECT OrderID, Date, Product, Quantity, UnitPrice, OrderStatus, TotalPrice
FROM orders
LIMIT 10;
"""

result1 = pd.read_sql_query(query1, conn)
print(result1.to_string(index=False))
print()

# ── QUERY 2: Total Revenue ──────────────────────────────────────────────────
print("=" * 60)
print("QUERY 2: Total Revenue from All Orders")
print("=" * 60)

query2 = """
SELECT ROUND(SUM(TotalPrice), 2) AS Total_Revenue,
       COUNT(*) AS Total_Orders,
       ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value
FROM orders;
"""

result2 = pd.read_sql_query(query2, conn)
print(result2.to_string(index=False))
print()

# ── QUERY 3: Revenue & Orders by Product ───────────────────────────────────
print("=" * 60)
print("QUERY 3: Revenue and Order Count by Product")
print("=" * 60)

query3 = """
SELECT Product,
       COUNT(*) AS Total_Orders,
       ROUND(SUM(TotalPrice), 2) AS Total_Revenue,
       ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value
FROM orders
GROUP BY Product
ORDER BY Total_Revenue DESC;
"""

result3 = pd.read_sql_query(query3, conn)
print(result3.to_string(index=False))
print()

# ── QUERY 4: Revenue by Order Status ───────────────────────────────────────
print("=" * 60)
print("QUERY 4: Revenue Breakdown by Order Status")
print("=" * 60)

query4 = """
SELECT OrderStatus,
       COUNT(*) AS Total_Orders,
       ROUND(SUM(TotalPrice), 2) AS Total_Revenue,
       ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value
FROM orders
GROUP BY OrderStatus
ORDER BY Total_Revenue DESC;
"""

result4 = pd.read_sql_query(query4, conn)
print(result4.to_string(index=False))
print()

# ── QUERY 5: Filter - Only Delivered Orders ─────────────────────────────────
print("=" * 60)
print("QUERY 5: Delivered Orders Only (WHERE Filter)")
print("=" * 60)

query5 = """
SELECT OrderID, Product, Quantity, TotalPrice, PaymentMethod
FROM orders
WHERE OrderStatus = 'Delivered'
ORDER BY TotalPrice DESC
LIMIT 10;
"""

result5 = pd.read_sql_query(query5, conn)
print(result5.to_string(index=False))
print()

# ── QUERY 6: Average Order Value by Payment Method ──────────────────────────
print("=" * 60)
print("QUERY 6: Average Order Value by Payment Method")
print("=" * 60)

query6 = """
SELECT PaymentMethod,
       COUNT(*) AS Total_Orders,
       ROUND(AVG(TotalPrice), 2) AS Avg_Order_Value,
       ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM orders
GROUP BY PaymentMethod
ORDER BY Avg_Order_Value DESC;
"""

result6 = pd.read_sql_query(query6, conn)
print(result6.to_string(index=False))
print()

# ── QUERY 7: Monthly Revenue Trend ──────────────────────────────────────────
print("=" * 60)
print("QUERY 7: Monthly Revenue Trend")
print("=" * 60)

query7 = """
SELECT STRFTIME('%Y-%m', Date) AS Month,
       COUNT(*) AS Total_Orders,
       ROUND(SUM(TotalPrice), 2) AS Monthly_Revenue
FROM orders
GROUP BY Month
ORDER BY Month ASC;
"""

result7 = pd.read_sql_query(query7, conn)
print(result7.to_string(index=False))
print()

# ── QUERY 8: High-Value Orders (TotalPrice > 2000) ──────────────────────────
print("=" * 60)
print("QUERY 8: High-Value Orders (TotalPrice > 2000)")
print("=" * 60)

query8 = """
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice, OrderStatus
FROM orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC
LIMIT 15;
"""

result8 = pd.read_sql_query(query8, conn)
print(result8.to_string(index=False))
print()

# ── Close the database connection ───────────────────────────────────────────
conn.close()
print("=" * 60)
print("✅ All 8 SQL Queries Complete! Database connection closed.")
print("=" * 60)