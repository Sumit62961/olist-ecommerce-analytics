# Olist E-Commerce Analytics

## Overview

This project analyzes the **Brazilian Olist E-Commerce dataset** to understand customer behavior, delivery performance, product/category revenue, and seller performance.

The project combines **MySQL, Python, Pandas, NumPy, Flask, and Streamlit** to perform business-focused data analysis and present the results through a REST API and interactive dashboard.

The Python analysis pipeline was refactored into a simple **object-oriented structure** to make the analysis more organized, reusable, and easier to maintain.

The project follows this architecture:

```text
Olist CSV Data
      │
      ├──────────────► MySQL
      │                  │
      │                  ▼
      │             SQL Analysis
      │
      ▼
Python / Pandas
      │
      ▼
Object-Oriented Analysis
      │
      ├──────────────► Flask REST API
      │                      │
      │                      ▼
      │                 JSON Responses
      │                      │
      │                      ▼
      │                 Streamlit Dashboard
      │
      ▼
Business Insights
```

The main goal of the project is to answer practical business questions such as:

- Which customers generate high revenue?
- What percentage of orders are delivered late?
- Which product categories generate the most revenue?
- How concentrated is revenue across product categories?
- Which sellers require greater attention based on delivery performance and customer reviews?
- How can the analysis results be exposed through an API and presented through a dashboard?

---

## Project Objectives

The main objectives of this project are:

- Analyze customer purchasing behavior and identify high-value customers.
- Measure delivery performance and identify late-delivery patterns.
- Analyze product categories based on revenue and order performance.
- Identify categories that contribute significantly to overall revenue.
- Analyze seller performance using delivery and customer review data.
- Use SQL to perform business-oriented data analysis.
- Use Python, Pandas, and NumPy for data processing and analysis.
- Organize the Python analysis into reusable classes and functions using basic object-oriented programming.
- Build a Flask REST API to expose important analytics results.
- Build a Streamlit dashboard to present business KPIs and analysis visually.
- Generate meaningful business insights that can support data-driven decision-making.

---

## Technologies Used

### Programming & Analysis

- **Python** — Data processing and analysis
- **Pandas** — Data cleaning, transformation, merging, grouping, and analysis
- **NumPy** — Numerical operations and classification
- **Matplotlib** — Data visualization
- **Jupyter Notebook** — Exploratory analysis and experimentation

### Database

- **MySQL** — Database management and SQL-based business analysis
- **mysql-connector-python** — Python connection to MySQL

### Backend & Dashboard

- **Flask** — REST API development
- **Requests** — API requests from the Streamlit dashboard
- **Streamlit** — Interactive analytics dashboard
- **python-dotenv** — Environment variable management

### Development & Version Control

- **PyCharm** — Python development
- **Git** — Version control
- **GitHub** — Repository and project management

---

## Dataset

This project uses the **Brazilian Olist E-Commerce Dataset**, which contains information about orders, customers, products, sellers, payments, reviews, and geolocation.

The raw dataset contains the following CSV files:

- `olist_customers_dataset.csv`
- `olist_geolocation_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`
- `product_category_name_translation.csv`

The dataset is used in two ways:

1. Loaded into **MySQL** for SQL-based business analysis.
2. Stored locally in `data/raw/` for the Python analysis pipeline.

---

## Dataset Handling

The raw CSV files are kept locally and are **not included in this Git repository** because some files are relatively large.

Place the downloaded CSV files inside:

```text
data/raw/
```

For example:

```text
olist-ecommerce-analytics/
└── data/
    └── raw/
        ├── olist_customers_dataset.csv
        ├── olist_orders_dataset.csv
        ├── ...
        └── product_category_name_translation.csv
```

The raw dataset is excluded from Git using `.gitignore`.

The Python pipeline automatically resolves the project root and reads the files from:

```text
data/raw/
```

---

## Project Structure

```text
olist-ecommerce-analytics/
│
├── api/
│   ├── app.py
│   └── database.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── processed/
│   └── raw/
│       ├── olist_customers_dataset.csv
│       ├── olist_geolocation_dataset.csv
│       ├── olist_order_items_dataset.csv
│       ├── olist_order_payments_dataset.csv
│       ├── olist_order_reviews_dataset.csv
│       ├── olist_orders_dataset.csv
│       ├── olist_products_dataset.csv
│       ├── olist_sellers_dataset.csv
│       └── product_category_name_translation.csv
│
├── notebooks/
│   └── sales_project2.ipynb
│
├── src/
│   ├── __init__.py
│   ├── customer_analysis.py
│   ├── data_loader.py
│   ├── delivery_analysis.py
│   ├── main.py
│   ├── product_analysis.py
│   ├── report.py
│   └── seller_analysis.py
│
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Key Business Insights

## Customer Insights

The customer analysis identifies high-value customers using spending and order-frequency criteria.

- **4,489 customers** were identified as high-value customers.
- These customers generated approximately **4.17 million** in revenue.
- The average spending of a high-value customer was approximately **929.95**.
- The average spending of other customers was approximately **129.19**.
- High-value customers therefore have significantly higher spending than the rest of the customer base.

### Business Recommendation

The business can focus on high-value customers through:

- Personalized offers
- Loyalty rewards
- Targeted promotions
- Exclusive discounts
- Customer retention strategies

Broad discounts for all customers may not be necessary when a smaller high-value segment contributes a significant amount of revenue.

---

## Delivery Insights

The delivery analysis evaluates delivery completion and compares actual delivery dates with estimated delivery dates.

- **96,476 orders** had a recorded customer delivery date.
- **7,827 orders** were classified as late.
- The overall late-delivery rate was **8.11%**.
- **88,649 orders** were delivered on time.
- On-time orders took an average of **10.42 days**.
- Late orders took an average of **31.06 days**.

Late deliveries therefore represent an important area for operational improvement.

### Business Recommendation

The business can investigate:

- Sellers with consistently high late-delivery rates
- Logistics performance
- Regional delivery delays
- Delivery-time differences between sellers and orders
- Areas where estimated delivery dates are frequently missed

---

## Product and Category Insights

Product categories were analyzed using revenue and order-level information.

The highest-revenue categories included:

1. `beleza_saude`
2. `relogios_presentes`
3. `cama_mesa_banho`
4. `esporte_lazer`
5. `informatica_acessorios`

The highest-revenue category, `beleza_saude`, generated approximately **1.26 million** in product revenue.

Additional analysis showed:

- **6 categories** individually contributed at least 5% of category revenue.
- **17 categories** were required to reach approximately 80% of cumulative category revenue.

### Business Recommendation

The company can prioritize major revenue-generating categories while continuing to monitor smaller categories for growth opportunities.

---

## Seller Insights

Seller performance was analyzed using:

- Number of orders
- Delivery performance
- Late-delivery rate
- Customer review scores

Sellers were classified into:

- Low Priority
- Medium Priority
- High Priority

The current Python analysis identified:

- **2,636 Low Priority sellers**
- **189 Medium Priority sellers**
- **265 High Priority sellers**

Combining delivery performance with customer reviews provides a more useful view of seller performance than analyzing either metric independently.

### Business Recommendation

High-priority sellers can be investigated further to understand:

- Delivery problems
- Customer satisfaction issues
- Operational bottlenecks
- Seller-specific performance patterns

---

# Python Analysis Pipeline

The Python analysis is organized into separate classes based on the analysis area.

### `DataLoader`

Responsible for loading the Olist CSV datasets from:

```text
data/raw/
```

### `CustomerAnalysis`

Responsible for:

- Customer-level metrics
- Order counts
- Customer spending
- Customer segmentation
- High-value customer analysis

### `DeliveryAnalysis`

Responsible for:

- Delivery time calculation
- Late-delivery identification
- Late-delivery rate
- On-time delivery rate
- Delivery performance
- Delivery gap analysis

### `ProductAnalysis`

Responsible for:

- Category revenue
- Category order counts
- Average order value
- Category classification
- Revenue contribution
- Cumulative revenue
- 80% revenue analysis

### `SellerAnalysis`

Responsible for:

- Seller order analysis
- Seller delivery performance
- Seller late-delivery rate
- Average customer review score
- Seller priority classification

### `Report`

Responsible for:

- Collecting analysis results
- Cleaning Python/NumPy values for output
- Printing final analysis summaries

### `main.py`

Coordinates the complete Python analysis workflow.

---

# MySQL Analysis

The project also uses **MySQL** for database-based analysis.

The Olist dataset was loaded into a MySQL database named:

```text
sales
```

SQL analysis was used to answer business questions involving:

- Revenue
- Orders
- Customers
- Product categories
- Delivery performance
- Seller performance
- Aggregations
- Grouping
- Business metrics
- Advanced SQL analysis

The MySQL database is separate from the local CSV-based Python pipeline.

---

# Flask REST API

A Flask REST API was developed to expose important analytics results as JSON.

The API connects to the MySQL database and provides analytics endpoints.

## Available Endpoints

### API Status

```text
GET /
```

Returns the API status.

Example:

```json
{
    "message": "Olist API is running",
    "status": "success"
}
```

### Overall Summary

```text
GET /api/summary
```

Provides:

- Total orders
- Delivered orders
- Total revenue

### Customer Analysis

```text
GET /api/customers
```

Provides:

- Total unique customers
- Repeat customers
- Repeat customer rate

### Delivery Analysis

```text
GET /api/delivery
```

Provides:

- Total delivered orders
- On-time orders
- Late orders
- Late-delivery rate

### Category Analysis

```text
GET /api/categories
```

Returns the top five product categories by revenue.

### Seller Analysis

```text
GET /api/sellers
```

Returns the top ten sellers by number of orders.

---

# Environment Configuration

The Flask API connects to MySQL using environment variables.

Create a local `.env` file in the project root:

```text
MYSQL_PASSWORD=your_mysql_password
```

Do **not** commit the `.env` file to GitHub.

The project `.gitignore` excludes:

```text
.env
```

This keeps database credentials outside the source code.

---

# Streamlit Dashboard

An interactive Streamlit dashboard was developed on top of the Flask REST API.

The architecture is:

```text
MySQL
   │
   ▼
Flask REST API
   │
   │ JSON
   ▼
Streamlit Dashboard
```

The dashboard displays:

### Key Performance Indicators

- Total Orders
- Delivered Orders
- Total Revenue
- Repeat Customer Rate
- Late Delivery Rate
- On-Time Delivery Rate

### Customer Analysis

- Total Unique Customers
- Repeat Customers
- Repeat Customer Rate

### Delivery Analysis

- Total Delivered Orders
- Late Orders
- On-Time Orders

### Category Analysis

- Top 5 product categories by revenue
- Revenue visualization

### Seller Analysis

- Top 10 sellers by number of orders
- Seller order visualization

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone <repository-url>
cd olist-ecommerce-analytics
```

Replace `<repository-url>` with the GitHub repository URL.

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
pandas
numpy
matplotlib
flask
mysql-connector-python
python-dotenv
streamlit
requests
```

---

## 4. Add the Dataset

Download the Brazilian Olist E-Commerce Dataset.

Place the CSV files inside:

```text
data/raw/
```

---

## 5. Configure MySQL

Create the required MySQL database:

```text
sales
```

Load the Olist dataset tables into the database.

Make sure the MySQL password is configured in the `.env` file:

```text
MYSQL_PASSWORD=your_mysql_password
```

---

# Running the Python Analysis

From the project root directory:

```bash
python src/main.py
```

The program loads the datasets and performs:

- Customer analysis
- Delivery analysis
- Product/category analysis
- Seller analysis

The final results are printed in the terminal.

---

# Running the Flask API

From the project root directory:

```bash
python -m api.app
```

The API will normally be available at:

```text
http://127.0.0.1:5000
```

You can test the API status by opening:

```text
http://127.0.0.1:5000/
```

---

# Running the Streamlit Dashboard

The Flask API must be running first.

In another terminal, activate the virtual environment and run:

```bash
streamlit run dashboard/app.py
```

Streamlit will provide a local URL, usually similar to:

```text
http://localhost:8501
```

Open the URL in a browser to view the dashboard.

---

# Running the Complete Application

The recommended workflow is:

### Terminal 1 — Flask API

```bash
python -m api.app
```

### Terminal 2 — Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

The Streamlit dashboard requests analytics data from the Flask API, while the Flask API retrieves the required information from MySQL.

---

# Git and Data Handling

The project uses Git and GitHub for version control.

Large raw dataset files are excluded from the repository using `.gitignore`.

The following local files/directories are excluded:

```text
.venv/
.idea/
data/raw/
.env
__pycache__/
*.py[cod]
.ipynb_checkpoints/
```

This keeps the repository focused on:

- Source code
- API code
- Dashboard code
- Notebook
- Documentation
- Project configuration

The project follows a development workflow where new features are developed on the `development` branch and merged into `main` through pull requests.

---

# Project Development Workflow

The project was developed incrementally through the following stages:

```text
1. Dataset Exploration
        ↓
2. MySQL Database & SQL Analysis
        ↓
3. Python / Pandas Analysis
        ↓
4. Object-Oriented Refactoring
        ↓
5. Flask REST API
        ↓
6. Streamlit Dashboard
        ↓
7. Final Testing & Documentation
```

This approach separates data analysis, backend API development, and dashboard presentation.

---

# Future Improvements

Potential future improvements include:

- Add an ML-based feature such as delivery-delay prediction or low-review-risk prediction.
- Add automated tests for the analysis classes and API endpoints.
- Add more advanced dashboard filters and interactive visualizations.
- Add additional business KPIs.
- Improve API error handling and response validation.
- Add deployment support for the Flask API and Streamlit dashboard.

---

# Project Status

## Completed

- Olist dataset exploration
- MySQL database analysis
- SQL business analysis
- Python/Pandas analysis
- NumPy-based classification
- Customer analysis
- Delivery analysis
- Product/category analysis
- Seller analysis
- Basic object-oriented project refactoring
- Reusable Python analysis classes
- Result reporting system
- Flask REST API
- MySQL-to-API integration
- Streamlit analytics dashboard
- API-to-dashboard integration
- Environment variable configuration
- Dependency management
- Git version control
- GitHub repository setup
- Development branch workflow
- Pull request workflow
- Project documentation

## Planned

- Machine learning feature
- Automated testing
- Additional dashboard improvements
- Optional deployment

---

# Conclusion

The Olist E-Commerce Analytics project demonstrates an end-to-end analytics workflow using **SQL, Python, Pandas, NumPy, Flask, and Streamlit**.

The project moves from raw e-commerce data to:

```text
Raw Data
   ↓
MySQL / SQL Analysis
   ↓
Python Data Analysis
   ↓
Object-Oriented Analytics
   ↓
Flask REST API
   ↓
Streamlit Dashboard
   ↓
Business Insights
```

The resulting system provides a practical foundation for analyzing e-commerce operations, customer behavior, delivery performance, product categories, and seller performance while demonstrating skills relevant to **Data Analyst and Data Science roles**.
