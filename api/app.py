from flask import Flask

from api.database import Database


app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Olist API is running",
        "status": "success"
    }


@app.route("/api/summary")
def summary():

    db = Database()

    if not db.connect():
        return {
            "status": "error",
            "message": "Database connection failed"
        }, 500

    db.cursor.execute("""
        SELECT COUNT(*)
        FROM orders
    """)
    total_orders = db.cursor.fetchone()[0]

    db.cursor.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE order_status = 'delivered'
    """)
    delivered_orders = db.cursor.fetchone()[0]

    db.cursor.execute("""
        SELECT SUM(payment_value)
        FROM order_payments
    """)
    total_revenue = db.cursor.fetchone()[0]

    db.close()

    return {
        "total_orders": total_orders,
        "delivered_orders": delivered_orders,
        "total_revenue": float(total_revenue)
    }


@app.route("/api/customers")
def customers():

    db = Database()

    if not db.connect():
        return {
            "status": "error",
            "message": "Database connection failed"
        }, 500

    db.cursor.execute("""
        SELECT COUNT(DISTINCT customer_unique_id)
        FROM customers
    """)
    unique_customers = db.cursor.fetchone()[0]

    db.cursor.execute("""
        SELECT COUNT(*)
        FROM (
            SELECT t1.customer_unique_id
            FROM customers t1
            JOIN orders t2
                ON t1.customer_id = t2.customer_id
            GROUP BY t1.customer_unique_id
            HAVING COUNT(t2.order_id) > 1
        ) AS t
    """)
    repeat_customers = db.cursor.fetchone()[0]

    repeat_customer_rate = (
        repeat_customers / unique_customers
    ) * 100

    db.close()

    return {
        "total_unique_customers": unique_customers,
        "repeat_customers": repeat_customers,
        "repeat_customer_rate": round(repeat_customer_rate, 2)
    }


@app.route("/api/delivery")
def delivery():

    db = Database()

    if not db.connect():
        return {
            "status": "error",
            "message": "Database connection failed"
        }, 500

    db.cursor.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE order_status = 'delivered'
    """)
    delivered_orders = db.cursor.fetchone()[0]

    db.cursor.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE order_status = 'delivered'
        AND order_delivered_customer_date <= order_estimated_delivery_date
    """)
    on_time_orders = db.cursor.fetchone()[0]

    db.cursor.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE order_status = 'delivered'
        AND order_delivered_customer_date > order_estimated_delivery_date
    """)
    late_orders = db.cursor.fetchone()[0]

    late_delivery_rate = (
        late_orders / delivered_orders
    ) * 100

    db.close()

    return {
        "total_delivered_orders": delivered_orders,
        "on_time_orders": on_time_orders,
        "late_orders": late_orders,
        "late_delivery_rate": round(late_delivery_rate, 2)
    }


@app.route("/api/categories")
def categories():

    db = Database()

    if not db.connect():
        return {
            "status": "error",
            "message": "Database connection failed"
        }, 500

    db.cursor.execute("""
        SELECT
            product_category_name,
            SUM(price) AS revenue
        FROM order_items t1
        JOIN products t2
            ON t1.product_id = t2.product_id
        GROUP BY product_category_name
        ORDER BY revenue DESC
        LIMIT 5
    """)

    categories_data = db.cursor.fetchall()

    db.close()

    return {
        "categories": [
            {
                "category": row[0],
                "revenue": float(row[1])
            }
            for row in categories_data
        ]
    }


@app.route("/api/sellers")
def sellers():

    db = Database()

    if not db.connect():
        return {
            "status": "error",
            "message": "Database connection failed"
        }, 500

    db.cursor.execute("""
        SELECT
            seller_id,
            COUNT(DISTINCT order_id) AS total_orders
        FROM order_items
        GROUP BY seller_id
        ORDER BY total_orders DESC
        LIMIT 10
    """)

    sellers_data = db.cursor.fetchall()

    db.close()

    return {
        "sellers": [
            {
                "seller_id": row[0],
                "total_orders": int(row[1])
            }
            for row in sellers_data
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)