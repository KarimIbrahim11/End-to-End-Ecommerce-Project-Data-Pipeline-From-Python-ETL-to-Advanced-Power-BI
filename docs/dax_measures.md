# 📊 DAX Measures

This document contains key DAX measures used in the Power BI dashboard, along with their business and technical explanations.

---

## 💰 Sales Metrics

| Measure | Description |
|--------|------------|
| **Total Sales** = SUM(All_Order_Table[total_amount]) | Calculates total revenue generated from all transactions. Core KPI for overall business performance. |
| **Total Order** = DISTINCTCOUNT(All_Order_Table[order_id]) | Counts total number of unique orders placed. |
| **Total Quantity** = SUM(All_Order_Table[quantity]) | Total number of items sold across all orders. |
| **AOV** = DIVIDE(SUM(All_Order_Table[total_amount]), DISTINCTCOUNT(All_Order_Table[order_id]), 0) | Measures the average revenue per order. Helps understand customer spending behavior.|

---

## 👥 Customer Metrics

| Measure | Description |
|--------|------------|
| **Total Customer** = COUNTROWS(customers) | Total number of customers in the dataset. |
| **Purchasing Customer** = DISTINCTCOUNT(All_Order_Table[customer_id]) | Customers who made at least one purchase. |
| **Returning Customers** = CALCULATE(DISTINCTCOUNT(customers[customer_id]), FILTER(VALUES(customers[customer_id]), CALCULATE(COUNTROWS(All_Order_Table)) > 1)) | Customers with more than one purchase (loyal customers). |
| **Lost Customers** = CALCULATE(DISTINCTCOUNT(customers[customer_id]), FILTER(VALUES(customers[customer_id]), CALCULATE(COUNTROWS(All_Order_Table)) = 1)) | Customers who made only one purchase (potential churn). |
| **Prospects Customers** = CALCULATE(DISTINCTCOUNT(customers[customer_id]), FILTER(VALUES(customers[customer_id]), CALCULATE(COUNTROWS(All_Order_Table)) = 0)) | Customers who never made a purchase. |


---

## 📉 Customer Behavior & Performance

| Measure | Description |
|--------|------------|
| **Churn Rate** = DIVIDE([Lost Customers],[Purchasing Customer],0) | Percentage of customers who purchased only once. Indicates customer retention issues. |
| **Conversion Rate** = VAR ConvertedCustomers = DISTINCTCOUNT(All_Order_Table[customer_id]) RETURN DIVIDE(ConvertedCustomers, DISTINCTCOUNT(customers[customer_id]), 0) | Measures how many total customers converted into buyers. |
| **Revenue Returning** = CALCULATE([Total Sales],FILTER(VALUES(customers[customer_id]),CALCULATE(COUNTROWS(All_Order_Table)) > 1)| Revenue generated from returning (loyal) customers. |
| **Revenue Lost** = CALCULATE( [Total Sales],FILTER( VALUES(customers[customer_id]),CALCULATE(COUNTROWS(All_Order_Table)) = 1))| Revenue generated from one-time customers. Helps identify lost value. |

---

## ⭐ Product & Review Metrics

| Measure | Description |
|--------|------------|
| **Average Rating** = AVERAGE(product_reviews[rating]) | Measures overall customer satisfaction. |
| **Review Count** = COUNTA(product_reviews[review_id]) | Total number of reviews submitted. |
| **Review Coverage %** = DIVIDE(DISTINCTCOUNT('product_reviews'[product_id]), DISTINCTCOUNT('All_Order_Table'[product_id]),0) | Percentage of products that have reviews. |
| **Customer Sentiment** = SWITCH( 'product_reviews'[rating (bins)],1, "Low Satisfaction (1-2)",2, "Low Satisfaction (1-2)",3, "Neutral (3)",4, "High Satisfaction (4-5)",5, "High Satisfaction (4-5)","Other")| Categorizes ratings into satisfaction levels (Low / Neutral / High). |
| **Sales by Satisfaction** = VAR CurrentRating = SELECTEDVALUE('product_reviews'[rating (bins)])RETURN SWITCH( TRUE(),CurrentRating >= 4, "High Satisfaction (4-5)",CurrentRating <= 2, "Low Satisfaction (1-2)","Neutral (3)")| Groups products based on rating bins for analysis of satisfaction vs sales. |

---

## 🔥 Advanced Analysis (Heatmap)

| Measure | Description |
|--------|------------|
| **Heatmap Sales** = VAR CurrentProducts = VALUES('products'[product_id]) RETURN CALCULATE(SUM('All_Order_Table'[total_amount]),KEEPFILTERS(CurrentProducts),'product_reviews' -- This forces the measure to respect the rating filter context)| Calculates sales while respecting rating filters (used in matrix/heatmaps). |
| **Heatmap Quantity** = VAR CurrentProducts = VALUES('products'[product_id]) RETURN CALCULATE(SUM('All_Order_Table'[quantity]),KEEPFILTERS(CurrentProducts),'product_reviews')| Calculates quantity sold with product-level filtering applied. |

---

## ⏱️ Time Intelligence

| Measure | Description |
|--------|------------|
| **Sales MTD** = TOTALMTD([Total Sales], 'Calendar'[Date]) | Month-to-date sales performance. |
| **Sales Previous Month**  = CALCULATE([Total Sales], PREVIOUSMONTH(Calendar[Date])) | Sales from the previous month for comparison. |
| **Sales Last Year** = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Calendar[Date])) | Sales from the same period last year. |
| **MoM Growth %**  = DIVIDE([Total Sales] - [Sales pervious Month], [Sales pervious Month], 0) | Month-over-Month growth rate. |
| **YoY Growth %** = DIVIDE([Total Sales] - [Sales per last year], [Sales per last year], 0) | Year-over-Year growth rate. |

---

## 📅 Additional Metrics

| Measure | Description |
|--------|------------|
| **Last Purchase Date** = MAX(All_Order_Table[order_date]) | Shows the most recent transaction date. Useful for recency analysis. |

---

## 📌 Key Takeaways

* **KPI & Advanced Analytics Support:** Measures are designed to support both core business KPIs and deep-dive analytical insights.
* **Behavioral Customer Segmentation:** The logic for **Prospects, Returning, and Lost** customers enables precise behavioral and retention analysis.
* **Actionable Sentiment Integration:** Linking sales data with customer reviews allows the business to identify revenue risks based on satisfaction levels.
* **Contextual Heatmap Logic:** Specialized measures ensure that complex matrix visuals remain accurate by respecting multi-dimensional filters (Product + Rating).
* **Time Intelligence & Benchmarking:** Built-in functions (MTD, MoM, YoY) provide the necessary context to evaluate current performance against historical trends.
* **Data Reliability:** Extensive use of best-practice functions like `DIVIDE` and `VAR` ensures a resilient, error-free dashboard experience.
