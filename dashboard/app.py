import streamlit as st
import requests

st.set_page_config(
    layout="wide",
    page_title="Ecommerce Analytics"
)

st.title("Olist E-Commerce Analytics Dashboard")
st.write("Business insights from Olist E-Commerce data")


# API: Summary
response = requests.get(
    "http://127.0.0.1:5000/api/summary"
)
data = response.json()


# API: Customers
customer_response = requests.get(
    "http://127.0.0.1:5000/api/customers"
)
customer_data = customer_response.json()


# API: Delivery
delivery_response = requests.get(
    "http://127.0.0.1:5000/api/delivery"
)
delivery_data = delivery_response.json()


# Revenue calculation
total_revenue = data["total_revenue"]
total_revenue_millions = round(
    total_revenue / 1_000_000,
    2
)

st.subheader("Key Performance Indicators")
st.write("A quick overview of overall sales, customers, and delivery performance.")

# Main KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Orders",
        data["total_orders"]
    )

with col2:
    st.metric(
        "Delivered Orders",
        data["delivered_orders"]
    )

with col3:
    st.metric(
        "Total Revenue",
        f"₹{total_revenue_millions}M"
    )

with col4:
    st.metric(
        "Repeat Customer Rate",
        f"{customer_data['repeat_customer_rate']}%"
    )


# Delivery rate calculation
on_time_rate = round(
    (
        delivery_data["on_time_orders"]
        / delivery_data["total_delivered_orders"]
    ) * 100,
    2
)


# Delivery KPIs
col5, col6 = st.columns(2)

with col5:
    st.metric(
        "Late Delivery Rate",
        f"{delivery_data['late_delivery_rate']}%"
    )

with col6:
    st.metric(
        "On-Time Delivery Rate",
        f"{on_time_rate}%"
    )


# Customer Analysis
st.divider()
st.subheader("Customer Analysis")

customer_col1, customer_col2, customer_col3 = st.columns(3)

with customer_col1:
    st.metric(
        "Total Unique Customers",
        customer_data["total_unique_customers"]
    )

with customer_col2:
    st.metric(
        "Repeat Customers",
        customer_data["repeat_customers"]
    )

with customer_col3:
    st.metric(
        "Repeat Customer Rate",
        f"{customer_data['repeat_customer_rate']}%"
    )


# Delivery Analysis
st.divider()
st.subheader("Delivery Analysis")

delivery_col1, delivery_col2, delivery_col3 = st.columns(3)

with delivery_col1:
    st.metric(
        "Total Delivered Orders",
        delivery_data["total_delivered_orders"]
    )

with delivery_col2:
    st.metric(
        "Late Orders",
        delivery_data["late_orders"]
    )

with delivery_col3:
    st.metric(
        "On-Time Orders",
        delivery_data["on_time_orders"]
    )


# Category Analysis
st.divider()
st.subheader("Category Analysis")
st.write("Top 5 product categories by revenue.")

category_response = requests.get("http://127.0.0.1:5000/api/categories")

category_data = category_response.json()

category_names = []
category_revenue = []

for items in category_data["categories"]:
    category_names.append(items["category"])
    category_revenue.append(items["revenue"])


category_chart_data = {
    "Category": category_names,
    "Revenue": category_revenue
}

st.bar_chart(
    category_chart_data,
    x="Category",
    y="Revenue"
)


# Seller Analysis
st.divider()
st.subheader("Seller Analysis")
st.write("Top 10 sellers by number of orders.")

seller_response = requests.get("http://127.0.0.1:5000/api/sellers")

seller_data = seller_response.json()


seller_names = []
seller_orders = []
for index, items in enumerate(seller_data["sellers"], start=1):
    seller_names.append(f"Seller {index}")
    seller_orders.append(items["total_orders"])

seller_chart_data = {
    "Seller": seller_names,
    "Seller_orders": seller_orders
}

st.bar_chart(
    seller_chart_data,
    x ="Seller",
    y ="Seller_orders"
)


st.divider()

st.caption(
    "Olist E-Commerce Analytics | Built with Python, Flask, MySQL and Streamlit"
)