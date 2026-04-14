## 📊 Data Modeling

### 1. Entity Relationship Diagram (ERD)
The original source data consists of the following relational entities:
* **Orders**: General transaction headers.
* **Order Items**: Line-level details for each order.
* **Customers**: Demographic information of buyers.
* **Products**: Catalog details and pricing.
* **Product Reviews**: Customer feedback and ratings.

---

### 2. Data Transformation (ETL)
In this phase, I performed a strategic merge to create the central **Fact Table**:

* **Grain Level Alignment**: I merged the `Order Items` and `Orders` tables.
* **Join Logic**: I initiated the merge starting with the **Order Items** table because it represents the **lowest grain** (transactional line-item level). This ensures that no granular data is lost and that every individual product sold is accounted for in the final dataset.
* **Result**: This process created the `All_Order_Table`, which serves as the primary Fact table containing both transactional metrics and foreign keys for the dimensions.

---

### 3. Star Schema Architecture
The final data model is optimized into a **Star Schema** for efficient querying and reporting in Power BI:

#### **Fact Tables**
* `All_Order_Table`: Sales metrics, quantities, and prices.
* `Product_Review`: Feedback scores and sentiments.

#### **Dimension Tables**
* `Dim_Customer`: Contains customer attributes.
* `Dim_Product`: Contains product categories and names.
* `Dim_Shipping_Country`: Unique list of shipping locations.
* `Dim_Payment_Method`: Unique list of payment types used.

> **Why this matters:**
> By using the **Order Items** as the base for the merge, I handled the **one-to-many relationship** correctly. Since one order can contain multiple items, starting with the lowest grain ensures all individual product details are preserved for accurate analysis.
