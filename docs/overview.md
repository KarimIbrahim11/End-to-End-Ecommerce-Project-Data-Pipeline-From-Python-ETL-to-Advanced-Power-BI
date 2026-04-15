# 🧠 Project Overview

## 📌 Introduction

This project presents an End-to-End Data Engineering and Analytics pipeline built on a large-scale simulated Ecommerce dataset (~20M records).

The primary goal was to transform a transactional OLTP system into an optimized OLAP model using a Star Schema design, enabling efficient reporting, advanced analytics, and scalable business intelligence.

---

## 🎯 Problem Statement

The original dataset was structured as a normalized Entity Relationship Diagram (ERD), designed for transactional operations rather than analytical use.

This resulted in:

- Complex joins across multiple tables  
- Poor performance for analytical queries  
- Difficulty in building scalable dashboards  
- Limited ability to generate business insights efficiently  

---

## 💡 Solution Approach

To address these challenges, I designed a complete data pipeline that includes:

### 🔹 Data Transformation (ETL)

- Extracted raw transactional data  
- Cleaned and standardized datasets  
- Merged tables based on the correct grain (order-item level)  
- Created calculated metrics such as Revenue  

---

### 🔹 Data Modeling

- Redesigned the schema into a **Star Schema**  
- Built a central **Fact Table** (`All_Order_Table`)  
- Created multiple **Dimension Tables** for slicing and filtering  

#### Best Practices Applied:
- Using lowest grain for fact table construction  
- Creating dimension tables for categorical fields (Country, Payment Method)  
- Optimizing relationships for performance  

---

### 🔹 Business Intelligence Layer

- Built an interactive dashboard in Power BI  
- Developed DAX measures for key KPIs  
- Enabled time intelligence using a dedicated date table  
- Delivered insights on customer behavior, sales performance, and trends  

---

## 🏗️ Architecture Overview

The project follows a layered data architecture:
- Raw Data (CSV)
 ↓
- Python ETL (Pandas)
 ↓
- Processed Data (Fact + Dimensions)
 ↓
- Power BI Data Model (Star Schema)
 ↓
- Dashboard & Insights

---

## 📊 Key Capabilities

This project demonstrates:

- Data Modeling (Star Schema Design)  
- ETL Pipeline Development using Python  
- Performance optimization techniques  
- Advanced Power BI analytics  
- Business-oriented data storytelling  

---

## 🚀 Outcome

The final solution enables:

- Faster and more efficient analytical queries  
- Simplified data exploration  
- Scalable reporting structure  
- Clear and actionable business insights  

---

## 📌 Summary

This project goes beyond dashboard creation by demonstrating a full data workflow — from raw data ingestion to business insights — following industry best practices in data engineering and analytics.
