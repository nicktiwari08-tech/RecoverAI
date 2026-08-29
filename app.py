import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="RecoverAI",
    page_icon="💰",
    layout="wide"
)

# Title
st.title("💰 RecoverAI")
st.subheader("Intelligent Revenue Recovery & Collection Strategy System")

st.write(
    "An AI-powered system that helps businesses identify payment risks, "
    "prioritize overdue customers, and recommend recovery strategies."
)
# Sidebar - CSV Upload
st.sidebar.header("📁 Data Upload")

uploaded_file = st.sidebar.file_uploader(
    "Upload Customer Data (CSV)",
    type=["csv"]
)
# Sample customer data
data = {
    "Customer": [
        "Customer A",
        "Customer B",
        "Customer C",
        "Customer D",
        "Customer E"
    ],
    "Outstanding Amount (₹)": [50000, 25000, 10000, 75000, 15000],
    "Days Overdue": [90, 45, 10, 120, 30],
    "Previous Late Payments": [5, 3, 0, 7, 1]
}

# Use uploaded CSV data if available
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("CSV uploaded successfully! ✅")
else:
    df = pd.DataFrame(data)

# Calculate risk score
df["Risk Score"] = (
    df["Days Overdue"] * 0.5
    + df["Previous Late Payments"] * 10
)

# Risk classification
def classify_risk(score):
    if score >= 80:
        return "🔴 High Risk"
    elif score >= 40:
        return "🟡 Medium Risk"
    else:
        return "🟢 Low Risk"

df["Risk Level"] = df["Risk Score"].apply(classify_risk)

# Calculate recovery priority score
df["Recovery Priority Score"] = (
    (df["Outstanding Amount (₹)"] / 1000)
    + (df["Days Overdue"] * 0.3)
    + (df["Previous Late Payments"] * 5)
)

def classify_priority(score):
    if score >= 100:
        return "🔴 Urgent"
    elif score >= 50:
        return "🟠 High"
    elif score >= 25:
        return "🟡 Medium"
    else:
        return "🟢 Low"

df["Recovery Priority"] = df[
    "Recovery Priority Score"
].apply(classify_priority)

# Recovery recommendation
def recommendation(risk):
    if "High" in risk:
        return "Immediate follow-up and personalized recovery plan"
    elif "Medium" in risk:
        return "Send reminder and schedule follow-up"
    else:
        return "Regular payment reminder"
# Personalized Recovery Strategy Engine
def recovery_strategy(row):
    amount = row["Outstanding Amount (₹)"]
    overdue = row["Days Overdue"]
    late_payments = row["Previous Late Payments"]

    if overdue >= 90 and amount >= 50000:
        return "🚨 Immediate call + personalized settlement plan + senior escalation"

    elif overdue >= 60:
        return "📞 Priority follow-up call and structured payment plan"

    elif late_payments >= 3:
        return "📩 Personalized reminder with flexible payment options"

    elif overdue >= 30:
        return "🔔 Automated reminder followed by scheduled follow-up"

    else:
        return "✅ Friendly payment reminder and regular monitoring"


df["AI Recovery Strategy"] = df.apply(recovery_strategy, axis=1)

df["Recommended Action"] = df["Risk Level"].apply(recommendation)

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))
col2.metric(
    "Total Outstanding",
    f"₹{df['Outstanding Amount (₹)'].sum():,}"
)
col3.metric(
    "High Risk Customers",
    len(df[df["Risk Level"] == "🔴 High Risk"])
)
col4.metric(
    "Medium Risk Customers",
    len(df[df["Risk Level"] == "🟡 Medium Risk"])
)

st.divider()

# Executive Summary
st.subheader("📌 Executive Recovery Summary")

total_outstanding = df["Outstanding Amount (₹)"].sum()

urgent_customers = len(
    df[df["Recovery Priority"] == "🔴 Urgent"]
)

high_risk_amount = df.loc[
    df["Risk Level"] == "🔴 High Risk",
    "Outstanding Amount (₹)"
].sum()

st.success(
    f"""
📊 **Business Overview**

💰 Total Outstanding Revenue: ₹{total_outstanding:,}

🚨 Urgent Recovery Cases: {urgent_customers}

⚠️ High-Risk Revenue Exposure: ₹{high_risk_amount:,}

🎯 RecoverAI recommends prioritizing urgent and high-risk customers
to improve recovery efficiency.
"""
)
# Risk Distribution Chart
st.subheader("📊 Risk Distribution")

risk_counts = df["Risk Level"].value_counts()

fig, ax = plt.subplots()
ax.bar(risk_counts.index, risk_counts.values)

ax.set_xlabel("Risk Level")
ax.set_ylabel("Number of Customers")
ax.set_title("Customer Risk Distribution")

st.pyplot(fig)
# Outstanding Amount by Customer
st.subheader("💰 Outstanding Amount by Customer")

fig2, ax2 = plt.subplots()

ax2.bar(
    df["Customer"],
    df["Outstanding Amount (₹)"]
)

ax2.set_xlabel("Customer")
ax2.set_ylabel("Outstanding Amount (₹)")
ax2.set_title("Outstanding Amount Analysis")

st.pyplot(fig2)
# Customer Risk Filter
st.subheader("🔍 Filter Customers")

risk_filter = st.selectbox(
    "Select Risk Level",
    ["All", "🔴 High Risk", "🟡 Medium Risk", "🟢 Low Risk"]
)

if risk_filter == "All":
    filtered_df = df
else:
    filtered_df = df[df["Risk Level"] == risk_filter]
# Customer analysis table
st.subheader("📊 Customer Revenue Recovery Analysis")
st.write(filtered_df.to_html(escape=False), unsafe_allow_html=True)
# AI Recovery Insights
st.subheader("🧠 AI Recovery Insights")

# Find the highest priority customer
top_customer = df.loc[df["Recovery Priority Score"].idxmax()]

st.info(
    f"🎯 **Top Recovery Priority:** {top_customer['Customer']}\n\n"
    f"💰 Outstanding Amount: ₹{top_customer['Outstanding Amount (₹)']:,}\n\n"
    f"📅 Days Overdue: {top_customer['Days Overdue']}\n\n"
    f"🚨 Priority Level: {top_customer['Recovery Priority']}\n\n"
    f"🤖 Recommended Action: {top_customer['Recommended Action']}"
)

# Calculate high-risk outstanding amount
high_risk_df = df[df["Risk Level"] == "🔴 High Risk"]

if not high_risk_df.empty:
    high_risk_amount = high_risk_df["Outstanding Amount (₹)"].sum()

    st.warning(
        f"⚠️ **Revenue at Risk:** ₹{high_risk_amount:,} "
        f"is associated with high-risk customers."
    )
# Recovery Action Summary
st.subheader("🚀 Recovery Action Summary")

action_counts = df["Recommended Action"].value_counts()

for action, count in action_counts.items():
    st.write(f"**{action}:** {count} customer(s)")
# Recovery recommendations
st.subheader("🤖 AI Recovery Recommendations")

for _, row in df.iterrows():
    st.write(
        f"**{row['Customer']}** — {row['Risk Level']} | "
        f"Recommendation: {row['Recommended Action']}"
    )

# Download Analysed Report
st.divider()
st.subheader("📥 Download Analysed Recovery Report")

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Complete Recovery Report",
    data=csv_data,
    file_name="RecoverAI_Analysed_Report.csv",
    mime="text/csv"
)

# Footer
st.divider()
st.caption("RecoverAI | AI Revenue Recovery System")