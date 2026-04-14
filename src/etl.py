import pandas as pd

# 1. Load the product details for each order (Order Items)
order_items_df = pd.read_csv(r'C:\Users\hb\Downloads\Synthetic E-Commerce Relational Datasets\csv\order_items.csv')

# 2. Load the general order information (Orders)
orders_df = pd.read_csv(r'C:\Users\hb\Downloads\Synthetic E-Commerce Relational Datasets\csv\orders.csv')

# 3. Initial merge of both tables based on 'order_id' to create a comprehensive view
All_Order_Table = pd.merge(order_items_df, orders_df, on='order_id')

# 4. Create a Dimension Table for shipping countries to remove redundancy and assign unique IDs
dim_shipping_country = orders_df[['shipping_country']].drop_duplicates().reset_index(drop=True)
dim_shipping_country['country_id'] = dim_shipping_country.index + 1

# 5. Create a Dimension Table for payment methods and assign unique IDs
dim_payment_method = orders_df[['payment_method']].drop_duplicates().reset_index(drop=True)
dim_payment_method['payment_id'] = dim_payment_method.index + 1

# 6. Update the main orders dataframe to link it with the new Dimension Tables (IDs)
orders_df = orders_df.merge(dim_shipping_country, on='shipping_country')
orders_df = orders_df.merge(dim_payment_method, on='payment_method')

# 7. Select the final required columns for the Orders table (Preparing the Fact Table)
orders_final = orders_df[['order_id', 'customer_id', 'order_date', 'country_id', 'payment_id']]

# 8. Merge the cleaned order data back with order items
All_Order_Table = pd.merge(order_items_df, orders_final, on='order_id')

# 9. Feature Engineering: Calculate total amount per item (Quantity * Unit Price)
All_Order_Table['total_amount'] = All_Order_Table['quantity'] * All_Order_Table['unit_price']

# 10. Export the final cleaned tables to CSV for further use in Power BI or Analysis
All_Order_Table.to_csv(r'C:\Users\hb\Downloads\Synthetic E-Commerce Relational Datasets\csv\All_Order_Table.csv', index=False)
dim_payment_method.to_csv(r'C:\Users\hb\Downloads\Synthetic E-Commerce Relational Datasets\csv\dim_payment_method.csv', index=False)
dim_shipping_country.to_csv(r'C:\Users\hb\Downloads\Synthetic E-Commerce Relational Datasets\csv\dim_shipping_country.csv', index=False)

print("ETL process finished successfully.")
