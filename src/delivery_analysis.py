import pandas as pd


class DeliveryAnalysis:

    def __init__(self, orders):
        self.orders = orders

    def create_delivery_analysis(self):

        orders = self.orders.copy()

        orders["order_purchase_timestamp"] = pd.to_datetime(
            orders["order_purchase_timestamp"]
        )

        orders["order_delivered_customer_date"] = pd.to_datetime(
            orders["order_delivered_customer_date"]
        )

        orders["order_estimated_delivery_date"] = pd.to_datetime(
            orders["order_estimated_delivery_date"]
        )

        orders["delivery_days"] = (
            orders["order_delivered_customer_date"]
            - orders["order_purchase_timestamp"]
        ).dt.days

        orders["delivery_type"] = orders.apply(
            lambda row: (
                "Late"
                if row["order_delivered_customer_date"]
                > row["order_estimated_delivery_date"]
                else "On Time"
            ),
            axis=1
        )

        return orders


    def delivery_summary(self, delivery_analysis):

        delivered_orders = delivery_analysis[delivery_analysis["order_delivered_customer_date"].notna()]

        total_orders = len(delivered_orders)

        late_orders = (delivered_orders["delivery_type"] == "Late").sum()

        on_time_orders = (delivered_orders["delivery_type"] == "On Time").sum()

        late_rate = (late_orders / total_orders ) *100

        average_delivery_days = delivered_orders["delivery_days"].mean()

        summary = {
            "total_delivered_orders": total_orders,
            "late_orders": late_orders,
            "on_time_orders": on_time_orders,
            "late_delivery_rate": round(late_rate, 2),
            "average_delivery_days": round(average_delivery_days, 2)
        }

        return summary

    def delivery_type_summary(self, delivery_analysis):

        delivered_orders = delivery_analysis[
            delivery_analysis["order_delivered_customer_date"].notna()
        ]

        late_orders = (delivered_orders["delivery_type"] == "Late").sum()

        on_time_orders = (delivered_orders['delivery_type'] == "On Time").sum()

        late_orders_percentage = (late_orders/delivered_orders["delivery_type"].count())*100

        on_time_orders_percentage = (on_time_orders/delivered_orders["delivery_type"].count())*100

        summary = {
            "On Time":{
                "orders": on_time_orders,
                "percentage": round(on_time_orders_percentage,2)
            },
            "Late":{
                "orders": late_orders,
                "percentage": round(late_orders_percentage, 2)
            }
        }

        return summary

    def delivery_performance(self, delivery_analysis):

        delivered_orders = delivery_analysis[
            delivery_analysis["order_delivered_customer_date"].notna()
        ]

        late_orders = delivered_orders[
            delivered_orders["delivery_type"] == "Late"
            ]

        on_time_orders = delivered_orders[
            delivered_orders["delivery_type"] == "On Time"
            ]

        avg_late_delivery = late_orders["delivery_days"].mean()
        avg_on_time_delivery = on_time_orders["delivery_days"].mean()

        result = {
            "On Time" : round(avg_on_time_delivery,2),
            "Late": round(avg_late_delivery,2)
        }

        return result

    def delivery_gap_analysis(self, delivery_analysis):


        delivered_orders = delivery_analysis[
            delivery_analysis["order_delivered_customer_date"].notna()
        ].copy()

        delivered_orders["delivery_gap"] = (delivered_orders["order_delivered_customer_date"]
                                            - delivered_orders["order_estimated_delivery_date"]).dt.days

        late_orders = delivered_orders[
            delivered_orders["delivery_type"] == "Late"
            ]

        on_time_orders = delivered_orders[
            delivered_orders["delivery_type"] == "On Time"
            ]

        late_delivery_gap = late_orders["delivery_gap"].mean()
        on_time_delivery_gap = on_time_orders["delivery_gap"].mean()

        result = {
            "On Time": round(on_time_delivery_gap, 2),
            "Late": round(late_delivery_gap, 2)
        }

        return result



if __name__ == "__main__":

    from pathlib import Path
    from data_loader import DataLoader

    project_path = Path(__file__).resolve().parent.parent
    data_path = project_path / "data" / "raw"

    loader = DataLoader(data_path)

    data = loader.load_all()

    analysis = DeliveryAnalysis(data["orders"])

    delivery_analysis = analysis.create_delivery_analysis()

    summary = analysis.delivery_summary(delivery_analysis)
    print("\nDelivery Summary:")
    print(summary)

    summary = analysis.delivery_type_summary(delivery_analysis)
    print("\nDelivery Type Summary:")
    print(summary)

    result = analysis.delivery_performance(delivery_analysis)
    print("\nAvg Delivery Days:")
    print(result)

    result = analysis.delivery_gap_analysis(delivery_analysis)
    print("\nDelivery Gap:")
    print(result)