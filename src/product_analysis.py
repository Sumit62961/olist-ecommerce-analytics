import numpy as np


class ProductAnalysis:

    def __init__(self, order_items, products):
        self.order_items = order_items
        self.products = products

    def category_revenue(self):
        product_analysis = (
            self.order_items
            .merge(self.products, on="product_id")
            .groupby("product_category_name")
            .agg(
                revenue=("price", "sum")
            )
            .sort_values("revenue", ascending=False)
        )

        return product_analysis

    def top_categories(self, category_revenue):
        top_categories = list(
            category_revenue.head(5).index
        )

        return top_categories

    def category_summary(self):
        category_analysis = (
            self.order_items
            .merge(self.products, on="product_id")
            .groupby("product_category_name")
            .agg(
                revenue=("price", "sum"),
                order_count=("order_id", "nunique")
            )
            .sort_values("revenue", ascending=False)
        )

        return category_analysis

    def category_performance(self, category_summary):
        category_summary = category_summary.copy()

        category_summary["average_order_value"] = (
            category_summary["revenue"]
            / category_summary["order_count"]
        )

        category_summary = category_summary.sort_values(
            "average_order_value",
            ascending=False
        )

        return category_summary

    def classify_categories(self, category_performance):
        category_performance = category_performance.copy()

        conditions = [
            category_performance["average_order_value"] >= 500,

            (
                (category_performance["average_order_value"] >= 200)
                & (category_performance["average_order_value"] < 500)
            )
        ]

        choices = [
            "High Value",
            "Medium Value"
        ]

        category_performance["category_type"] = np.select(
            conditions,
            choices,
            default="Low Value"
        )

        return category_performance

    def revenue_contribution(self, category_performance):
        category_performance = category_performance.copy()

        category_performance["revenue_percentage"] = round(
            (
                category_performance["revenue"]
                / category_performance["revenue"].sum()
            ) * 100,
            2
        )

        category_performance = category_performance.sort_values(
            "revenue_percentage",
            ascending=False
        )

        return category_performance

    def revenue_coverage(self, category_performance):
        category_performance = category_performance.copy()

        category_performance["cumulative_revenue_percentage"] = (
            category_performance["revenue_percentage"].cumsum()
        )

        category_performance = category_performance.sort_values(
            "revenue_percentage",
            ascending=False
        )

        return category_performance

    def categories_for_80_percent(self, revenue_coverage):
        revenue_coverage = revenue_coverage.copy()

        categories = list(
            revenue_coverage[
                revenue_coverage["cumulative_revenue_percentage"] <= 80
                ].index
        )

        first_category_over_80 = revenue_coverage[
            revenue_coverage["cumulative_revenue_percentage"] >= 80
            ].head(1)

        if not first_category_over_80.empty:
            categories.append(first_category_over_80.index[0])

        return categories

    def revenue_80_percent_point(self, revenue_coverage):
        revenue_coverage = revenue_coverage.copy()

        category = (
            revenue_coverage[
                revenue_coverage["cumulative_revenue_percentage"] >= 80
            ]
            .head(1)
        )

        return category

    def category_revenue_share(self, category_performance):
        category_performance = category_performance.copy()

        categories = category_performance[
            category_performance["revenue_percentage"] >= 5
        ]

        return categories


if __name__ == "__main__":

    from pathlib import Path
    from data_loader import DataLoader

    project_path = Path(__file__).resolve().parent.parent
    data_path = project_path / "data" / "raw"

    loader = DataLoader(data_path)

    order_items = loader.load_order_items()
    products = loader.load_products()

    analysis = ProductAnalysis(
        order_items,
        products
    )

    category_revenue = analysis.category_revenue()

    top_categories = analysis.top_categories(
        category_revenue
    )

    category_summary = analysis.category_summary()

    category_performance = analysis.category_performance(
        category_summary
    )

    category_performance = analysis.classify_categories(
        category_performance
    )

    revenue_contribution = analysis.revenue_contribution(
        category_performance
    )

    revenue_coverage = analysis.revenue_coverage(
        revenue_contribution
    )

    categories_80 = analysis.categories_for_80_percent(
        revenue_coverage
    )

    category_80_point = analysis.revenue_80_percent_point(
        revenue_coverage
    )

    category_revenue_share = analysis.category_revenue_share(
        revenue_contribution
    )

    print("\nTop Categories:")
    print(top_categories)

    print("\nCategories For 80 Percent Revenue:")
    print(categories_80)

    print("\n80 Percent Revenue Point:")
    print(category_80_point)

    print("\nCategories With At Least 5 Percent Revenue Share:")
    print(category_revenue_share)

    print(
        "\nNumber of categories:",
        len(category_revenue_share)
    )