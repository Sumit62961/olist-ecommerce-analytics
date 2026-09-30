import numpy as np


class CustomerAnalysis:

    def __init__(self, customers, orders, payments):
        self.customers = customers
        self.orders = orders
        self.payments = payments

    def create_customer_analysis(self):
        customer_analysis = (
            self.customers
            .merge(self.orders, on="customer_id")
            .merge(self.payments, on="order_id")
            .groupby("customer_unique_id")
            .agg(
                order_count=("order_id", "nunique"),
                total_spending=("payment_value", "sum")
            )
            .sort_values("total_spending", ascending=False)
        )

        return customer_analysis

    def segment_customers(self, customer_analysis):

        conditions = [
            (customer_analysis["total_spending"] >= 500) &
            (customer_analysis["order_count"] >= 2),

            (customer_analysis["total_spending"] < 500) &
            (customer_analysis["order_count"] >= 2),

            (customer_analysis["total_spending"] >= 500) &
            (customer_analysis["order_count"] == 1)
        ]

        choices = [
            "Repeat High Value",
            "Repeat Low Value",
            "One-Time High Value"
        ]

        customer_analysis["customer_segment"] = np.select(
            conditions,
            choices,
            default="One-Time Low Value"
        )

        return customer_analysis

    def high_value_summary(self, customer_analysis):

        high_value = customer_analysis[customer_analysis["total_spending"] >= 500]

        summary = {
            "high_value_customers": len(high_value),
            "high_value_revenue": high_value["total_spending"].sum(),
            "average_high_value_spending": round(high_value["total_spending"].mean(), 2)
        }
        return summary


if __name__ == "__main__":

    from pathlib import Path
    from data_loader import DataLoader

    project_path = Path(__file__).resolve().parent.parent
    data_path = project_path / "data" / "raw"

    loader = DataLoader(data_path)

    data = loader.load_all()

    analysis = CustomerAnalysis(
        data["customers"],
        data["orders"],
        data["payments"]
    )

    customer_analysis = analysis.create_customer_analysis()

    print("\nCustomer Analysis:")
    print(customer_analysis.head())

    print("\nCustomer Analysis Shape:")
    print(customer_analysis.shape)

    customer_analysis = analysis.segment_customers(
        customer_analysis
    )

    print("\nCustomer Segments:")
    print(
        customer_analysis["customer_segment"]
        .value_counts()
    )

    summary = analysis.high_value_summary(customer_analysis)

    print("\nHigh Value Customer Summary:")
    print(summary)