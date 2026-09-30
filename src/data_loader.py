import pandas as pd


class DataLoader:

    def __init__(self, data_path):
        self.data_path = data_path

    def load_csv(self, filename):
        file_path = self.data_path / filename
        return pd.read_csv(file_path)

    def load_customers(self):
        return self.load_csv("olist_customers_dataset.csv")

    def load_orders(self):
        return self.load_csv("olist_orders_dataset.csv")

    def load_order_items(self):
        return self.load_csv("olist_order_items_dataset.csv")

    def load_products(self):
        return self.load_csv("olist_products_dataset.csv")

    def load_sellers(self):
        return self.load_csv("olist_sellers_dataset.csv")

    def load_payments(self):
        return self.load_csv("olist_order_payments_dataset.csv")

    def load_reviews(self):
        return self.load_csv("olist_order_reviews_dataset.csv")

    def load_geolocation(self):
        return self.load_csv("olist_geolocation_dataset.csv")

    def load_category_translation(self):
        return self.load_csv("product_category_name_translation.csv")

    def load_all(self):
        data = {
            "customers": self.load_customers(),
            "orders": self.load_orders(),
            "order_items": self.load_order_items(),
            "products": self.load_products(),
            "sellers": self.load_sellers(),
            "payments": self.load_payments(),
            "reviews": self.load_reviews(),
            "geolocation": self.load_geolocation(),
            "category_translation": self.load_category_translation()
        }

        return data