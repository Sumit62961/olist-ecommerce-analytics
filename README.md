# Olist E-Commerce Analytics

## Overview

This project analyzes the **Brazilian Olist e-commerce dataset** to understand customer behavior, delivery performance, product/category revenue, and seller performance.

The project combines **MySQL, Python, Pandas, NumPy, and Matplotlib** to perform data analysis and generate business-focused insights.

The Python analysis pipeline was later refactored into a simple **object-oriented structure** to make the project more organized, reusable, and easier to maintain.

The main goal of the project is to answer practical business questions such as:

- Which customers generate high revenue?
- How many orders are delivered late?
- Which product categories contribute the most revenue?
- Which categories account for most of the total revenue?
- Which sellers require greater attention based on delivery performance and customer reviews?

## Project Objectives

The main objectives of this project are:

- Analyze customer purchasing behavior and identify high-value customers.
- Measure delivery performance and identify late-delivery patterns.
- Analyze product categories based on revenue and order performance.
- Identify categories that contribute significantly to overall revenue.
- Analyze seller performance using delivery and customer review data.
- Use SQL to perform business-oriented data analysis.
- Use Python, Pandas, and NumPy to perform data processing and analysis.
- Organize the Python analysis into reusable classes and functions using basic object-oriented programming.
- Generate meaningful business insights that can support data-driven decision-making.

## Technologies Used

- **Python** — Data processing and analysis
- **Pandas** — Data cleaning, transformation, merging, grouping, and analysis
- **NumPy** — Numerical operations and customer/category classification
- **Matplotlib** — Data visualization
- **MySQL** — Database management and SQL-based business analysis
- **Jupyter Notebook** — Exploratory analysis and experimentation
- **PyCharm** — Python development and project management
- **Git & GitHub** — Version control and project management

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

The dataset was loaded into MySQL for SQL-based analysis and is also used locally by the Python analysis pipeline.

### Dataset Handling

The raw CSV files are kept locally and are **not included in this Git repository** because some files are relatively large.

Place the downloaded CSV files inside:

```text
data/raw/
```

For example, on the development machine used for this project:

```text
C:\Users\pauls\PycharmProjects\olist-ecommerce-analytics\data\raw\
```

The absolute Windows path above is only an example for the local development environment. When cloning the project on another computer, use that computer's project directory and keep the CSV files inside `data/raw/`.

## Project Structure

```text
olist-ecommerce-analytics/
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

## Key Business Insights

### Customer Insights

- 4,489 customers were identified as high-value customers based on spending of at least 500 and the defined customer segmentation criteria.
- These high-value customers generated approximately **4.17 million** in revenue.
- The average spending of a high-value customer was approximately **929.95**, compared with approximately **129.19** for other customers.
- The analysis shows that a relatively small group of high-value customers contributes a significant amount of revenue.

### Delivery Insights

- 96,476 orders had a recorded customer delivery date.
- 7,827 delivered orders were classified as late.
- The overall late-delivery rate was **8.11%**.
- On-time orders took an average of **10.42 days**, while late orders took an average of **31.06 days**.
- Late deliveries therefore represent an important area for operational improvement.

### Product and Category Insights

- `beleza_saude` was the highest-revenue category, generating approximately **1.26 million** in product revenue.
- The top five categories were `beleza_saude`, `relogios_presentes`, `cama_mesa_banho`, `esporte_lazer`, and `informatica_acessorios`.
- Six categories individually contributed at least 5% of category revenue.
- **17 categories** were required to reach approximately 80% of cumulative category revenue.

### Seller Insights

- Seller performance was analyzed using order delivery performance and customer review scores.
- Sellers were classified into **Low, Medium, and High Priority** groups.
- The current Python analysis identified **265 High Priority**, **189 Medium Priority**, and **2,636 Low Priority** sellers in the seller-performance dataset.
- Combining delivery performance with customer reviews provides a more useful view of seller performance than looking at either metric independently.

## How to Run the Project

### 1. Clone the Repository

After creating the GitHub repository, clone it using:

```bash
git clone <repository-url>
cd olist-ecommerce-analytics
```

Replace `<repository-url>` with the actual GitHub repository URL.

### 2. Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The current Python analysis requires:

- pandas
- numpy
- matplotlib

### 4. Add the Dataset

Download the Brazilian Olist E-Commerce Dataset and place all required CSV files inside:

```text
data/raw/
```

The raw dataset is intentionally excluded from Git because of its file size.

### 5. Run the Python Analysis

From the project root directory, run:

```bash
python src/main.py
```

The program loads the datasets, performs the customer, delivery, product, and seller analyses, and prints the generated business summaries in the terminal.

## MySQL Analysis

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
- Aggregations and business metrics

The MySQL database is separate from the local CSV-based Python pipeline.

## Python Analysis Pipeline

The Python analysis is organized into separate classes based on the analysis area:

- `DataLoader` — Loads the Olist CSV datasets.
- `CustomerAnalysis` — Creates customer-level metrics and customer segments.
- `DeliveryAnalysis` — Calculates delivery time, late-delivery rate, delivery performance, and delivery gaps.
- `ProductAnalysis` — Analyzes category revenue, category performance, revenue contribution, and cumulative revenue.
- `SellerAnalysis` — Analyzes seller delivery performance and customer review scores.
- `Report` — Collects and prints the final analysis results.
- `main.py` — Coordinates the complete analysis workflow.

## Git and Data Handling

The project uses Git for version control.

Large raw dataset files are excluded from the repository using `.gitignore`.

The following local files/directories are also excluded:

- `.venv/`
- `.idea/`
- `data/raw/`
- Python cache files
- Jupyter checkpoint files

This keeps the repository focused on the source code, notebook, documentation, and project configuration.

## Future Improvements

Planned extensions for the project include:

- Build a Flask REST API to expose analysis results.
- Build an interactive Streamlit dashboard.
- Add an ML-based feature such as delivery-delay prediction or low-review-risk analysis.
- Add automated tests for the analysis classes.
- Improve the project with additional business KPIs and visualizations.

## Project Status

Current completed components:

- Olist dataset analysis
- MySQL business analysis
- Python/Pandas analysis
- Customer analysis
- Delivery analysis
- Product/category analysis
- Seller analysis
- Basic object-oriented project refactoring
- Project documentation
- Python dependency management
- Git version control setup

Future components such as the Flask API, Streamlit dashboard, and ML feature are planned extensions and are not yet included in the current implementation.
