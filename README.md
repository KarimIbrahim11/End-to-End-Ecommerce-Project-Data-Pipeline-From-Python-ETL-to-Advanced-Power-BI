# 📊 End-to-End E-Commerce Project Data Engineering & Analytics Pipeline

## 🧠 Project Overview

This project demonstrates a complete End-to-End Data Engineering and Analytics pipeline built on a large-scale simulated Ecommerce dataset (~20M records).

The goal of this project is to transform a complex OLTP (Online Transactional Processing) system into an optimized OLAP (Online Analytical Processing) data model using a Star Schema design, enabling efficient analytics, scalable reporting, and business intelligence.

---

## 🔎 Explore the Project

- 📊 **[Dashboard](powerbi/dashboard.pbix)** → Open Power BI file  
- 🧱 **[Data Modeling Docs](docs/data_modeling.md)** → Detailed explanation of ERD to Star Schema  
- 🧠 **[ETL Pipeline](src/etl.py)** → Python transformation code (ERD → Star Schema)  
- 📂 **[Full Documentation](docs/)** → Full project explanation (Modeling + DAX + Analysis)  
- 🖼️ **[Images & Visuals](images/)** → ERD, Star Schema, and Dashboard screenshots  
- 📦 **[Raw Data](https://www.kaggle.com/datasets/naelaqel/synthetic-e-commerce-relational-dataset/data)** → Source dataset you can download

## 🎯 Objectives

* Convert normalized ERD (OLTP) into Star Schema (OLAP)
* Build a scalable and efficient data model
* Develop an ETL pipeline using Python
* Enable advanced analytics using Power BI
* Extract actionable business insights

---

## 🏗️ Data Architecture & Modeling

### 🔹 Raw Data Sources (ERD)

The dataset includes multiple transactional and descriptive tables:

* Orders
* Order Items
* Customers
* Products
* Product Reviews

These tables were originally highly normalized and optimized for transactional operations, not analytics.

---

### 🔹 Star Schema Design

To support analytical workloads, the data model was redesigned into a Star Schema:

#### 🧾 Fact Table

* **Fact_Sales**

  * Built by merging Orders + Order Items
  * Includes calculated metrics (Total_amount)
 
* **Product_Review**

#### 📊 Dimension Tables

* **Dim_Customer**
* **Dim_Product**
* **Dim_Date**
* **Dim_Country**
* **Dim_Payment_Method**

This structure enables:

* Efficient filtering
* Faster aggregations
* Simplified analytical queries

---

## ⚙️ ETL Pipeline (Python)

The ETL process was implemented using Python (Pandas) and includes:

### 🔄 Extract

* Loaded raw CSV data from multiple sources

### 🧹 Transform

* Data cleaning and standardization
* Handling missing values
* Merging transactional tables (Order item + Order table)
* Creating derived columns:

  * Total_amount = Quantity × Price

### 💾 Load

* Final data stored for analytical use

---

## 📊 Business Intelligence (Power BI)

An interactive dashboard was built using Power BI on top of the Star Schema model.

---

### 📈 Key KPIs

#### 💰 Sales Metrics

* Total Revenue
* Total Orders
* Total Quantity Sold
* Average Order Value (AOV)

#### 👥 Customer Metrics

* Total Customers
* Active Customers
* Returning Customers
* New Customers
* Churned Customers
* Customer Retention Rate (%)
* Customer Churn Rate (%)

#### 📊 Performance Metrics

* Conversion Rate (%)
* Revenue by Category
* Revenue by Country
* Revenue by Payment Method

#### ⏱️ Time Intelligence

* Month-over-Month Growth (%)
* Year-over-Year Growth (%)
* Revenue Trends Over Time

---

## 📊 Dashboard Features

* Customer segmentation (New vs Returning vs Churned)
* Geographic sales distribution
* Product performance analysis
* Sales vs Rating correlation
* Time-based trend analysis
* Category-level performance breakdown

---

## 📌 Key Insights

* A small percentage of customers contributes to a large portion of total revenue (Pareto principle)
* Returning customers generate significantly higher value than new customers
* Certain categories (e.g., Electronics, Clothing) consistently outperform others
* Geographic distribution reveals high-performing regions with strong sales concentration
* Product ratings have a limited direct correlation with sales volume
* Seasonal trends impact revenue performance across months

---

## 🚀 Business Impact

This transformation enabled:

* Faster analytical queries compared to OLTP structure
* Simplified data exploration for business users
* Scalable reporting model
* Better decision-making through clear KPIs and insights

---

## 🛠️ Tech Stack

* Python (Pandas)
* Power BI
* Data Modeling (Star Schema)
* ETL Pipeline Design

---

## 📁 Project Structure

```
End-to-End-Ecommerce-Data-Pipeline/
│
├── src/
│   └── etl.py
│
├── docs/
│   └── data_modeling.md
│
├── images/
│
├── powerbi/
│   └── dashboard.pbix
│
└── README.md
```
---

## 👤 Author

This project was built as a portfolio case study to demonstrate:

* Data Engineering skills
* Data Modeling expertise
* Business Intelligence capabilities
* End-to-End alytics pipeline developmentan

---

⭐ If you found this project useful, feel free to star the repository!
