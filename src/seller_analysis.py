import numpy as np


class SellerAnalysis:

    def __init__(self, delivery_analysis, order_items):

        self.delivery_analysis = delivery_analysis
        self.order_items = order_items

    def seller_orders(self):
        seller_orders = (
            self.delivery_analysis[
                ["order_id", "delivery_type"]
            ]
            .merge(
                self.order_items[["order_id", "seller_id"]],
                on="order_id"
            )
            .drop_duplicates(["order_id", "seller_id"])
        )

        return seller_orders


    def seller_summary(self, seller_orders):
        seller_orders = seller_orders.copy()

        seller_summary = (seller_orders.groupby("seller_id")
                          .agg(
            total_orders = ("order_id","nunique"),
            late_orders = ("delivery_type",lambda x : (x=="Late").sum())
        ))

        seller_summary["late_delivery_rate"] = (
            (seller_summary["late_orders"]
                / seller_summary["total_orders"])
                * 100
        )

        seller_summary = seller_summary.sort_values(
            "late_delivery_rate",
            ascending=False
        )

        return seller_summary

    def seller_performance(self, seller_orders, reviews):

        seller_performance = (
            seller_orders
            .merge(reviews, on="order_id")
            .groupby("seller_id")
            .agg(
                total_orders=("order_id", "nunique"),
                late_orders=("delivery_type", lambda x: (x == "Late").sum()),
                avg_review_score=("review_score", "mean")
            )
        )

        seller_performance["late_delivery_rate"] = (
                seller_performance["late_orders"]
                / seller_performance["total_orders"]
                * 100
        )

        seller_performance = seller_performance.sort_values(
            "avg_review_score"
        )

        return seller_performance

    def seller_priority(self, seller_performance):

        seller_performance = seller_performance.copy()


        conditions = [
            (seller_performance["late_delivery_rate"]>15)
             & (seller_performance["avg_review_score"]>=4),
            (seller_performance["late_delivery_rate"]>15)
                & (seller_performance["avg_review_score"]<4)
        ]

        choices = ["Medium Priority","High Priority"]

        seller_performance["seller_priority"] = np.select(
            conditions,
            choices,
            default="Low Priority"
        )

        return seller_performance

    def seller_priority_summary(self, seller_performance):

        seller_priority = seller_performance["seller_priority"].value_counts()

        return seller_priority


if __name__ == "__main__":

    from pathlib import Path
    from data_loader import DataLoader
    from delivery_analysis import DeliveryAnalysis



    project_path = Path(__file__).resolve().parent.parent
    data_path = project_path / "data" / "raw"

    loader = DataLoader(data_path)

    orders = loader.load_orders()
    order_items = loader.load_order_items()
    reviews = loader.load_reviews()

    delivery_analysis = DeliveryAnalysis(orders)
    delivery_data = delivery_analysis.create_delivery_analysis()

    analysis = SellerAnalysis(delivery_data, order_items)

    result = analysis.seller_orders()

    # print(result.head())
    # print(result.shape)
    # print(result["order_id"].nunique())

    result1 = analysis.seller_summary(result)
    # print(result1.head(10))
    # print(result1.shape)

    result2 = analysis.seller_performance(result,reviews)
    # print(result2)

    result3 = analysis.seller_priority(result2)
    # print(result3)

    result4 = analysis.seller_priority_summary(result3)
    print(result4)