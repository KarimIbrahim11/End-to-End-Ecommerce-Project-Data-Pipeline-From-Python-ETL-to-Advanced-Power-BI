## 📊 Data Modeling

### 1. Entity Relationship Diagram (ERD)

The original dataset was structured as a normalized transactional system (OLTP), consisting of multiple related entities:

- **Orders**: Contains high-level transaction details (order date, customer, payment, etc.)
- **Order Items**: Represents line-level transactional data (products, quantity, price)
- **Customers**: Customer demographic and identification data
- **Products**: Product catalog and attributes
- **Product Reviews**: Customer ratings and feedback

While this structure is optimal for transactional systems, it is not suitable for analytical workloads due to heavy joins and complex relationships.

---

### 2. Data Transformation (ETL Logic)

To enable efficient analysis, the data was transformed into a centralized fact table.

#### 🔹 Grain Definition
The analytical grain was defined at the **order-item level**, meaning:
> Each row represents a single product within an order.

#### 🔹 Merge Strategy

- The transformation process starts from the **Order Items** table because it represents the **lowest level of granularity**
- The **Orders** table is then joined to enrich transactional context (date, customer, payment method)

#### 🔹 Why This Approach?

- Preserves all transactional details (no data loss)
- Handles the **one-to-many relationship** between Orders and Order Items correctly
- Ensures accurate aggregation for metrics such as Revenue and Quantity

#### 🔹 Result

This process produced the central fact table:

- **All_Order_Table**
  - Contains transactional metrics (Quantity, Price, Revenue)
  - Includes foreign keys to all dimension tables

---

### 3. Star Schema Architecture (Extended to Constellation Schema)

The final model was redesigned into a **Star Schema**, extended into a **Constellation Schema (Multi-Fact Model)** to support integrated analysis across multiple fact tables.

#### 🧾 Fact Tables

- **All_Order_Table**
  - Core transactional table
  - Contains measures such as Quantity, Price, and Revenue

- **Product_Review**
  - Stores customer feedback and ratings
  - Linked to shared dimensions (e.g., **Product_ID**)
  - Modeled as a separate fact table to enable integrated analysis between sales performance and customer satisfaction

---

#### 📊 Dimension Tables

- **Dim_Customer**
- **Dim_Product**
- **Dim_Date** *(created in Power BI and linked to Order Date)*
- **Dim_Shipping_Country**
- **Dim_Payment_Method**

---

### 4. Performance Optimization & Design Decisions

To improve performance and follow best practices in dimensional modeling:

#### 🔹 Surrogate Keys & Indexing

- Created indexed columns in the fact table for:
  - **Country**
  - **Payment Method**

- Replaced text-based fields with dimension keys by creating:
  - `Dim_Shipping_Country`
  - `Dim_Payment_Method`

#### 🔹 Why This Matters

- Reduces storage size in the fact table
- Improves join performance in Power BI
- Enables efficient filtering and slicing
- Aligns with **Star Schema best practices**

---

### 5. Time Intelligence Handling

- A dedicated **Dim_Date** table was created directly in Power BI
- Linked to the **Order Date** column in the fact table
- Enables:
  - Time-based aggregations (MoM, YoY)
  - Trend analysis
  - Seasonal insights

---

### 6. Design Considerations

- **Performance Optimization**: Reduced need for complex joins
- **Scalability**: Supports large datasets (20M+ rows)
- **Flexibility**: Enables slicing across multiple dimensions
- **Analytical Efficiency**: Simplifies DAX calculations

---

### 7. Key Takeaway

> Starting from the lowest grain (**Order Items**) and applying dimensional modeling techniques (indexing, surrogate keys, star schema design) ensured:
> - Accurate aggregation  
> - High performance  
> - Scalable analytics  

This approach follows industry best practices in data warehousing and BI modeling.
