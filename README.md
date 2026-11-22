# 💰 RecoverAI
![Dashboard](Screenshot%202026-11-22%20185449.png)
## Intelligent Revenue Recovery & Collection Strategy System

RecoverAI is an intelligent revenue recovery dashboard designed to help businesses identify customers with delayed payments, analyze payment risk, prioritize recovery cases, and recommend suitable recovery strategies.

The system analyzes customer payment data and converts it into actionable insights to support smarter and more efficient revenue recovery decisions.

---

## 🚀 Features

- 📁 Upload customer payment data using CSV
- 📊 Automatic customer payment analysis
- 🎯 Risk Score calculation
- 🔴 High, 🟡 Medium and 🟢 Low Risk Classification
- 🚨 Recovery Priority Score
- 🧠 Smart Recovery Insights
- 🤖 Personalized Recovery Strategy
- 💰 Revenue at Risk Analysis
- 📌 Executive Recovery Summary
- 📊 Risk Distribution Visualization
- 💵 Outstanding Amount Analysis
- 🔍 Customer Risk Filter
- 🚀 Recovery Action Summary
- 📥 Download Complete Analysed Recovery Report

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib

---

## 📂 Project Structure

RecoverAI/
- app.py
- app_backup.py
- customer_data.csv
- requirements.txt
- README.md

---

## ⚙️ Installation

Install the required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## 📊 Required CSV Format

The uploaded CSV file should contain:

- Customer
- Outstanding Amount (₹)
- Days Overdue
- Previous Late Payments

Example:

Customer,Outstanding Amount (₹),Days Overdue,Previous Late Payments

Rahul Enterprises,85000,95,6

Sharma Traders,42000,65,4

---

## 🎯 Problem Solved

Businesses often struggle to identify which overdue customers should be prioritized for recovery. Manual follow-ups can be inefficient and may not focus on customers with the highest revenue risk.

RecoverAI helps solve this problem by analyzing payment behaviour, identifying risk levels, prioritizing recovery cases, and recommending appropriate recovery strategies.

---

## 🔮 Future Improvements

- Machine Learning-based payment prediction
- Automated reminders
- Real-time payment data integration
- Advanced customer segmentation
- Smart recovery assistant

---

## 👨‍💻 Project

Developed as an AI Revenue Recovery project.
