from flask import Flask, jsonify, request

app = Flask(__name__)

# 模擬資料庫
products = [
    {"id": 1, "name": "iPhone 15", "price": 30000},
    {"id": 2, "name": "MacBook Pro", "price": 60000}
]
orders = []
users = [{"id": 1, "name": "Jack"}]

# ✅ 新增首頁路由
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello, API is running!"})

# 取得所有商品
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

# 取得單一商品
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# 新增商品（管理者）
@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

# 刪除商品（管理者）
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

# 創建新訂單
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    order = {
        "id": len(orders) + 1,
        "user_id": data["user_id"],
        "product_id": data["product_id"],
        "status": "pending"
    }
    orders.append(order)
    return jsonify(order), 201

# 取得所有訂單
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

# 取得單一訂單
@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=8080)
