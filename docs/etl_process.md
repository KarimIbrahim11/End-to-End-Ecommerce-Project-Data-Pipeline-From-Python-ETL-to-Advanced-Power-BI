# ⚙️ ETL Process

## 📌 Overview

This document describes the ETL (Extract, Transform, Load) pipeline implemented using Python (Pandas) to transform raw ecommerce transactional data into a structured format suitable for analytical processing.

The pipeline focuses on:

- Preserving transactional granularity
- Reducing redundancy
- Preparing a Star Schema-compatible dataset

## 🔄 1. Extract

Raw data was loaded from CSV files representing the transactional system:

* `order_items.csv` → line-level transactional data  
* `orders.csv` → order-level metadata  

```python```
- ```order_items_df = pd.read_csv('order_items.csv')```
- ```orders_df = pd.read_csv('orders.csv')```

## 🔄 2. Transform

#### 🔹 Step 1: Initial Merge (Understanding Relationships)

The first merge was performed between order_items and orders using order_id:

```Python```
- ```All_Order_Table = pd.merge(order_items_df, orders_df, on='order_id')```

#### 💡 Purpose:

- Validate relationships between tables
- Create a unified transactional view
- Understand data structure before optimization

#### 🔹 Step 2: Creating Dimension Tables
To reduce redundancy and follow Star Schema best practices, categorical columns were separated into dimension tables.

### 📊 Shipping Country Dimension
```Python```
- ``` dim_shipping_country = orders_df[['shipping_country']].drop_duplicates().reset_index(drop=True)```
- ```dim_shipping_country['country_id'] = dim_shipping_country.index + 1```

### 📊 Payment Method Dimension
```Python```
- ```dim_payment_method = orders_df[['payment_method']].drop_duplicates().reset_index(drop=True)```
- ```dim_payment_method['payment_id'] = dim_payment_method.index + 1```

#### 💡 Why This Step?

- Eliminates repeated text values in fact table
- Reduces storage size
- Improves join performance
- Aligns with dimensional modeling best practices

#### 🔹 Step 3: Replacing Text with Keys (Normalization for Analytics)
The original orders table was updated to replace categorical values with surrogate keys:

```Python```
- ```orders_df = orders_df.merge(dim_shipping_country, on='shipping_country')```
- ```orders_df = orders_df.merge(dim_payment_method, on='payment_method')```

``` Then only the required columns were selected:```
- ```orders_final = orders_df[['order_id', 'customer_id', 'order_date', 'country_id', 'payment_id']]```

#### 💡 Purpose:

- Prepare a clean fact-compatible structure
- Keep only relevant columns
- Link fact table with dimensions using IDs

#### 🔹 Step 4: Final Fact Table Construction
The final fact table was created by merging:

- ```order_items``` (lowest grain)
- ```orders_final``` (cleaned order metadata)

```Python```
- ```All_Order_Table = pd.merge(order_items_df, orders_final, on='order_id')```

#### Grain Definition:

- Each row represents a single product within an order (order-item level)

#### 🔹 Step 5: Feature Engineering
A key business metric was created:

```Python```
- ```All_Order_Table['total_amount'] = All_Order_Table['quantity'] * All_Order_Table['unit_price']```

#### 💡 Purpose:

- Enable revenue analysis
- Support KPI calculations in Power BI

## 🔄 3. Load
The transformed datasets were exported for analytical use:

```Python```
- ```All_Order_Table.to_csv('All_Order_Table.csv', index=False)```
- ```dim_payment_method.to_csv('dim_payment_method.csv', index=False)```
- ```dim_shipping_country.to_csv('dim_shipping_country.csv', index=False)```

#### 📂 Output Files
- All_Order_Table.csv → Fact Table
- dim_shipping_country.csv → Dimension
- dim_payment_method.csv → Dimension

#### 🔁 ETL Pipeline Flow:

#### 1. ↓Raw Data (CSV)
#### 2. ↓ Load into Pandas
#### 3. ↓ Initial Merge (Validation)
#### 4. ↓ Create Dimension Tables
#### 5. ↓ Replace Text with Keys
#### 6. ↓ Build Fact Table
#### 7. ↓ Feature Engineering (Revenue)
#### 8. Export Processed Data

## 📊 Outcome
The ETL pipeline produces:

- A centralized fact table aligned with business grain
- Optimized dimension tables for performance
- Clean and structured data ready for Power BI

#### 📌 Key Takeaways
- Starting from the lowest grain ensures data accuracy
- Separating dimensions improves performance and scalability
- Using surrogate keys reduces redundancy
- Proper ETL design directly impacts BI efficiency and query performance
