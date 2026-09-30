from pathlib import Path

from data_loader import DataLoader
from customer_analysis import CustomerAnalysis
from delivery_analysis import DeliveryAnalysis
from product_analysis import ProductAnalysis
from seller_analysis import SellerAnalysis
from report import Report


# Customer Analysis
def run_customer_analysis(data, report):
    customer_analysis = CustomerAnalysis(
        data["customers"],
        data["orders"],
        data["payments"]
    )

    customer_data = customer_analysis.create_customer_analysis()

    customer_data = customer_analysis.segment_customers(
        customer_data
    )

    customer_summary = customer_analysis.high_value_summary(
        customer_data
    )

    report.add_result(
        "customer_summary",
        customer_summary
    )


# Delivery Analysis
def run_delivery_analysis(data, report):
    delivery_analysis = DeliveryAnalysis(
        data["orders"]
    )

    delivery_data = delivery_analysis.create_delivery_analysis()

    delivery_summary = delivery_analysis.delivery_summary(
        delivery_data
    )

    report.add_result(
        "delivery_summary",
        delivery_summary
    )

    delivery_type_summary = delivery_analysis.delivery_type_summary(
        delivery_data
    )

    report.add_result(
        "delivery_type_summary",
        delivery_type_summary
    )

    delivery_performance = delivery_analysis.delivery_performance(
        delivery_data
    )

    report.add_result(
        "delivery_performance",
        delivery_performance
    )

    delivery_gap = delivery_analysis.delivery_gap_analysis(
        delivery_data
    )

    report.add_result(
        "delivery_gap",
        delivery_gap
    )

    return delivery_data


# Product Analysis
def run_product_analysis(data, report):
    product_analysis = ProductAnalysis(
        data["order_items"],
        data["products"]
    )

    category_revenue = product_analysis.category_revenue()

    top_categories = product_analysis.top_categories(
        category_revenue
    )

    report.add_result(
        "top_categories",
        top_categories
    )

    category_summary = product_analysis.category_summary()

    category_performance = product_analysis.category_performance(
        category_summary
    )

    category_performance = product_analysis.classify_categories(
        category_performance
    )

    revenue_contribution = product_analysis.revenue_contribution(
        category_performance
    )

    revenue_coverage = product_analysis.revenue_coverage(
        revenue_contribution
    )

    categories_80 = product_analysis.categories_for_80_percent(
        revenue_coverage
    )

    report.add_result(
        "categories_for_80_percent_revenue",
        categories_80
    )

    category_80_point = product_analysis.revenue_80_percent_point(
        revenue_coverage
    )

    report.add_result(
        "80_percent_revenue_point",
        category_80_point
    )

    category_revenue_share = product_analysis.category_revenue_share(
        revenue_contribution
    )

    report.add_result(
        "category_revenue",
        category_revenue_share
    )


# Seller Analysis
def run_seller_analysis(data, delivery_data, report):
    seller_analysis = SellerAnalysis(
        delivery_data,
        data["order_items"]
    )

    seller_orders = seller_analysis.seller_orders()

    seller_performance = seller_analysis.seller_performance(
        seller_orders,
        data["reviews"]
    )

    seller_performance = seller_analysis.seller_priority(
        seller_performance
    )

    seller_priority_summary = seller_analysis.seller_priority_summary(
        seller_performance
    )

    report.add_result(
        "seller_priority_summary",
        seller_priority_summary
    )


# Main Program
def main():
    project_path = Path(__file__).resolve().parent.parent
    data_path = project_path / "data" / "raw"

    loader = DataLoader(data_path)

    data = loader.load_all()

    report = Report()

    run_customer_analysis(
        data,
        report
    )

    delivery_data = run_delivery_analysis(
        data,
        report
    )

    run_product_analysis(
        data,
        report
    )

    run_seller_analysis(
        data,
        delivery_data,
        report
    )

    report.print_summary()


if __name__ == "__main__":
    main()